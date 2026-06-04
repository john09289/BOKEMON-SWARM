"""
UI system for BOKEMON SWARM
Dark indigo/amber palette with monospaced font

[FIXED] 4-tier font loading so text always renders on any Python/pygame build:
  TIER 1: pygame.font.SysFont('monospace', 16) — standard path
  TIER 2: pygame.font.Font(None, 16)           — built-in pygame fallback
  TIER 3: pygame._freetype C extension directly — bypasses broken font.py
           wrapper (Python 3.14 builds where font.cpython-*.so is absent)
  TIER 4: _SurfaceFont stub                    — pure pygame, never crashes
[ADDED] print()-based logging at every font tier so any model/runner can trace
        which tier resolved and why.
[FIXED] draw_dialogue always draws a visible indigo/amber box even when font
        is None — prevents the black/grey screen during tutorial state.
"""

import pygame
from typing import List
from constants import COLORS, SCREEN_WIDTH, SCREEN_HEIGHT


# ── [ADDED] Font compatibility shims ─────────────────────────────────────────

class _FreetypeAdapter:
    """
    [ADDED] Wraps pygame._freetype.Font to expose the same
    .render(text, antialias, color) -> Surface  API as pygame.font.Font.
    Required because _freetype.Font.render() returns (Surface, Rect), not Surface.
    """
    def __init__(self, ft_font):
        self._ft = ft_font

    def render(self, text: str, antialias: bool, color, background=None) -> pygame.Surface:
        try:
            surf, _ = self._ft.render(text, color, background)
            return surf
        except Exception:
            # [ADDED] Return a 1x1 transparent surface rather than crash
            return pygame.Surface((1, 1), pygame.SRCALPHA)

    def __repr__(self):
        return f"<_FreetypeAdapter>"


class _SurfaceFont:
    """
    [ADDED] Pure-pygame font stub — last resort.
    Draws coloured rectangles scaled to text length.
    Guarantees draw_dialogue/draw_menu always render something visible.
    """
    def __init__(self, size: int):
        self._size = size
        self._char_w = max(4, size // 2)

    def render(self, text: str, antialias: bool, color, background=None) -> pygame.Surface:
        w = max(4, len(text) * self._char_w)
        h = self._size
        surf = pygame.Surface((w, h))
        bg = background if background else (30, 30, 30)
        surf.fill(bg)
        pygame.draw.rect(surf, color, (1, h // 3, w - 2, h // 3))
        return surf

    def __repr__(self):
        return f"<_SurfaceFont size={self._size}>"


class UI:
    def __init__(self):
        self.font = None
        self.large_font = None

        # ── TIER 1: pygame.font.SysFont ───────────────────────────────────────
        # [ADDED] Explicit font.init() call before SysFont — fixes Python 3.14
        #         circular-import that silently leaves self.font = None.
        print("[ui] UI.__init__: calling pygame.font.init() explicitly")
        try:
            pygame.font.init()
        except Exception as e:
            print(f"[ui] UI.__init__: pygame.font.init() failed: {e}")

        print("[ui] UI.__init__: [TIER 1] trying SysFont('monospace', 16)")
        try:
            self.font = pygame.font.SysFont('monospace', 16)
            self.large_font = pygame.font.SysFont('monospace', 24)
            print("[ui] UI.__init__: [TIER 1] SysFont OK")
        except Exception as e:
            print(f"[ui] UI.__init__: [TIER 1] SysFont failed: {e}")

            # ── TIER 2: pygame.font.Font(None, size) ──────────────────────────
            print("[ui] UI.__init__: [TIER 2] trying Font(None, 16)")
            try:
                self.font = pygame.font.Font(None, 16)
                self.large_font = pygame.font.Font(None, 24)
                print("[ui] UI.__init__: [TIER 2] Font(None) OK")
            except Exception as e2:
                print(f"[ui] UI.__init__: [TIER 2] Font(None) failed: {e2}")

                # ── TIER 3: pygame._freetype C extension directly ──────────────
                # [ADDED] On Python 3.14 builds where font.cpython-*.so was NOT
                # compiled, pygame/font.py has a circular import.  The _freetype
                # C extension IS compiled and can be imported directly.
                print("[ui] UI.__init__: [TIER 3] importing pygame._freetype directly")
                try:
                    import pygame._freetype as _ft
                    _ft.init()
                    self.font = _FreetypeAdapter(_ft.Font(None, 16))
                    self.large_font = _FreetypeAdapter(_ft.Font(None, 24))
                    print("[ui] UI.__init__: [TIER 3] _freetype adapter OK")
                except Exception as e3:
                    print(f"[ui] UI.__init__: [TIER 3] _freetype failed: {e3}")

                    # ── TIER 4: pure-pygame surface stub ──────────────────────
                    # [ADDED] Never raises, always returns a Surface.
                    print("[ui] UI.__init__: [TIER 4] installing _SurfaceFont stub")
                    self.font = _SurfaceFont(14)
                    self.large_font = _SurfaceFont(22)

        print(f"[ui] UI.__init__: final font={self.font!r}")

        self.dialogue_active = False
        self.dialogue_text = ""
        self.dialogue_lq_translation = ""
        self.menu_active = False
        self.menu_options = ["Attack", "Seraphim", "Item", "Run"]
        self.selected_menu_index = 0
        
    def draw_hud(self, screen: pygame.Surface, player, seraphim):
        """Draw the main HUD"""
        bar_width = 200
        bar_height = 20
        bar_x = 10
        bar_y = 10
        
        pygame.draw.rect(screen, COLORS['black'], (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(screen, COLORS['white'], (bar_x, bar_y, bar_width, bar_height), 2)
        
        if seraphim:
            energy_ratio = player.energy_bank / player.max_energy
            energy_width = int(bar_width * energy_ratio)
            pygame.draw.rect(screen, COLORS['amber'], (bar_x, bar_y, energy_width, bar_height))
            
        if self.font:
            energy_text = self.font.render(f"HJ: {int(player.energy_bank)}/{int(player.max_energy)}", 
                                          True, COLORS['white'])
            screen.blit(energy_text, (bar_x + 5, bar_y + 2))
            
            shard_text = self.font.render(f"Mercy Shards: {player.mercy_shards}", 
                                         True, COLORS['gold'])
            screen.blit(shard_text, (bar_x + 220, bar_y + 2))
            
            if seraphim:
                name_text = self.font.render(f"Active: {seraphim.name}", 
                                           True, COLORS['light_blue'])
                screen.blit(name_text, (bar_x, bar_y + 30))
            
    def draw_dialogue(self, screen: pygame.Surface):
        """
        Draw dialogue box.
        [FIXED] Always draws a visible indigo/amber box — even when self.font is None.
                Previously returned early on no-font, leaving tutorial state as a
                plain black screen (the grey/black freeze the user reported).
        """
        if not self.dialogue_active:
            return
            
        box_rect = pygame.Rect(50, SCREEN_HEIGHT - 150, SCREEN_WIDTH - 100, 140)
        pygame.draw.rect(screen, COLORS['indigo'], box_rect)
        pygame.draw.rect(screen, COLORS['amber'], box_rect, 3)
        
        if self.font:
            lines = self.dialogue_text.split('\n')
            for i, line in enumerate(lines[:4]):
                text = self.font.render(line, True, COLORS['white'])
                screen.blit(text, (60, SCREEN_HEIGHT - 140 + i * 20))
                
            if self.dialogue_lq_translation:
                lq_text = self.font.render(f"LQ: {self.dialogue_lq_translation}", 
                                          True, COLORS['gold'])
                screen.blit(lq_text, (60, SCREEN_HEIGHT - 140 + 100))
        else:
            # [ADDED] No-font fallback: coloured bars so the box is never empty
            for i in range(3):
                pygame.draw.rect(screen, COLORS['grey'],
                                 (65, SCREEN_HEIGHT - 140 + i * 22, SCREEN_WIDTH - 150, 14))
            # [ADDED] Amber bar as SPACE/proceed indicator
            pygame.draw.rect(screen, COLORS['amber'],
                             (SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT - 30, 80, 14))
            
    def draw_menu(self, screen: pygame.Surface):
        """Draw battle menu"""
        if not self.menu_active:
            return
            
        menu_rect = pygame.Rect(SCREEN_WIDTH - 150, SCREEN_HEIGHT - 150, 140, 140)
        pygame.draw.rect(screen, COLORS['indigo'], menu_rect)
        pygame.draw.rect(screen, COLORS['amber'], menu_rect, 2)
        
        if self.font:
            for i, option in enumerate(self.menu_options):
                color = COLORS['amber'] if i == self.selected_menu_index else COLORS['white']
                text = self.font.render(option, True, color)
                screen.blit(text, (SCREEN_WIDTH - 140, SCREEN_HEIGHT - 140 + i * 25))
            
    def show_dialogue(self, text: str, lq_translation: str = ""):
        """Show a dialogue box"""
        self.dialogue_active = True
        self.dialogue_text = text
        self.dialogue_lq_translation = lq_translation
        
    def hide_dialogue(self):
        """Hide dialogue box"""
        self.dialogue_active = False
        self.dialogue_text = ""
        self.dialogue_lq_translation = ""
        
    def show_menu(self):
        """Show battle menu"""
        self.menu_active = True
        
    def hide_menu(self):
        """Hide battle menu"""
        self.menu_active = False
        
    def navigate_menu(self, direction: int):
        """Navigate menu up/down"""
        self.selected_menu_index = (self.selected_menu_index + direction) % len(self.menu_options)
        
    def get_selected_menu(self) -> str:
        """Get currently selected menu option"""
        return self.menu_options[self.selected_menu_index]