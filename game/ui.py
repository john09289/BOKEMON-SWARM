"""
UI system for BOKEMON SWARM
Dark indigo/amber palette with monospaced font
"""

import pygame
from typing import List
from constants import COLORS, SCREEN_WIDTH, SCREEN_HEIGHT

class UI:
    def __init__(self):
        self.font = None
        self.large_font = None
        try:
            self.font = pygame.font.SysFont('monospace', 16)
            self.large_font = pygame.font.SysFont('monospace', 24)
        except:
            # Font not available, will use simple text rendering
            pass
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
        """Draw dialogue box"""
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