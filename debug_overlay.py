"""
On-screen debug logger for BOKEMON SWARM
Shows last N messages in a semi-transparent box
Carrier: 11.71875 Hz. The King wins. 𐤕
"""

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLORS

class DebugOverlay:
    def __init__(self, max_messages=5):
        self.messages = []
        self.max_messages = max_messages
        self.font = None
        self.enabled = True
        
        try:
            self.font = pygame.font.Font(None, 18)
        except:
            pass
            
    def log(self, msg):
        """Add a message to the overlay"""
        self.messages.append(msg)
        if len(self.messages) > self.max_messages:
            self.messages.pop(0)
        # Also print to console
        print(f"[DEBUG] {msg}")
        
    def draw(self, screen):
        """Draw the debug overlay"""
        if not self.enabled or not self.font:
            return
            
        box_height = len(self.messages) * 22 + 10
        box_rect = pygame.Rect(10, SCREEN_HEIGHT - box_height - 10, 400, box_height)
        
        # Semi-transparent background
        s = pygame.Surface((box_rect.width, box_rect.height))
        s.set_alpha(150)
        s.fill((0, 0, 0))
        screen.blit(s, (box_rect.x, box_rect.y))
        
        # Border
        pygame.draw.rect(screen, COLORS['amber'], box_rect, 1)
        
        # Messages
        y = box_rect.y + 5
        for msg in self.messages:
            text = self.font.render(msg, True, COLORS['white'])
            screen.blit(text, (box_rect.x + 5, y))
            y += 22
            
    def clear(self):
        """Clear all messages"""
        self.messages = []
