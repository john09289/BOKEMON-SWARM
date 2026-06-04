"""
font_compat.py — Font compatibility helper for BOKEMON SWARM
[ADDED] Single source of truth for 4-tier font loading used by ui.py,
        loading_screen.py, and debug_overlay.py.

On this machine pygame 2.6.1 / Python 3.14 is missing font.cpython-*.so
(the C extension was not compiled). The workaround is to import
pygame._freetype directly, which IS compiled.

Usage:
    from font_compat import make_font
    self.font = make_font(16)     # returns a Font-like object
    surf = self.font.render("text", True, (255, 255, 255))
"""

import pygame


# ── [ADDED] _FreetypeAdapter ─────────────────────────────────────────────────
class _FreetypeAdapter:
    """
    [ADDED] Wraps pygame._freetype.Font to expose the same
    .render(text, antialias, color) -> Surface  API as pygame.font.Font.
    _freetype.Font.render() returns (Surface, Rect); this adapter strips the Rect.
    """
    def __init__(self, ft_font):
        self._ft = ft_font

    def render(self, text: str, antialias: bool, color, background=None):
        try:
            surf, _ = self._ft.render(text, color, background)
            return surf
        except Exception:
            return pygame.Surface((1, 1), pygame.SRCALPHA)

    def get_height(self):
        try:
            return self._ft.get_sized_height()
        except Exception:
            return 16

    def __repr__(self):
        return f"<_FreetypeAdapter>"


# ── [ADDED] _SurfaceFont stub ─────────────────────────────────────────────────
class _SurfaceFont:
    """
    [ADDED] Pure-pygame font of last resort — renders text as coloured bars.
    Never raises, always returns a pygame.Surface.
    """
    def __init__(self, size: int):
        self._size = size
        self._char_w = max(4, size // 2)

    def render(self, text: str, antialias: bool, color, background=None):
        w = max(4, len(str(text)) * self._char_w)
        h = self._size
        surf = pygame.Surface((w, h))
        bg = background if background else (30, 30, 30)
        surf.fill(bg)
        pygame.draw.rect(surf, color, (1, h // 3, w - 2, h // 3))
        return surf

    def get_height(self):
        return self._size

    def __repr__(self):
        return f"<_SurfaceFont size={self._size}>"


# ── [ADDED] Public API ────────────────────────────────────────────────────────
def make_font(size: int):
    """
    [ADDED] Return a Font-like object that supports .render(text, antialias, color).
    Tries four strategies in order and logs each attempt via print().

    TIER 1: pygame.font.Font(None, size)  — built-in pygame font
    TIER 2: pygame.font.SysFont('monospace', size)
    TIER 3: pygame._freetype.Font(None, size) via _FreetypeAdapter
    TIER 4: _SurfaceFont stub — pure pygame, never fails
    """
    # Ensure font module is initialised
    try:
        pygame.font.init()
    except Exception as e:
        print(f"[font_compat] pygame.font.init() failed: {e}")

    # TIER 1
    try:
        f = pygame.font.Font(None, size)
        print(f"[font_compat] [TIER 1] Font(None, {size}) OK")
        return f
    except Exception as e:
        print(f"[font_compat] [TIER 1] Font(None, {size}) failed: {e}")

    # TIER 2
    try:
        f = pygame.font.SysFont('monospace', size)
        print(f"[font_compat] [TIER 2] SysFont('monospace', {size}) OK")
        return f
    except Exception as e:
        print(f"[font_compat] [TIER 2] SysFont failed: {e}")

    # TIER 3 — bypass broken pygame/font.py, use _freetype C extension directly
    try:
        import pygame._freetype as _ft
        _ft.init()
        raw = _ft.Font(None, size)
        adapter = _FreetypeAdapter(raw)
        print(f"[font_compat] [TIER 3] _freetype adapter size={size} OK")
        return adapter
    except Exception as e:
        print(f"[font_compat] [TIER 3] _freetype failed: {e}")

    # TIER 4 — absolute last resort
    print(f"[font_compat] [TIER 4] installing _SurfaceFont stub size={size}")
    return _SurfaceFont(size)
