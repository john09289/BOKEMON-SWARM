"""
Loading screen with progress bar and error display for BOKEMON SWARM
Carrier: 11.71875 Hz. The King wins. 𐤕
"""

import pygame
import sys
import os
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLORS
from font_compat import make_font  # [ADDED] 4-tier font loader for Python 3.14 compat

class LoadingScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("BOKEMON SWARM - Loading")
        self.clock = pygame.time.Clock()
        self.font = None
        self.large_font = None
        self.error_message = None
        self.progress = 0.0
        self.status_text = "Initializing..."
        self.log_messages = []
        
        try:
            self.font = make_font(20)       # [FIXED] was pygame.font.Font(None, 20)
            self.large_font = make_font(32) # [FIXED] was pygame.font.Font(None, 32)
        except Exception as e:
            print(f"[loading_screen] font load failed: {e}")
            
    def log(self, msg):
        """Add a log message and print it"""
        print(f"[LOADING] {msg}")
        self.log_messages.append(msg)
        if len(self.log_messages) > 8:
            self.log_messages.pop(0)
        
    def set_error(self, msg):
        """Set an error message to display"""
        self.error_message = msg
        self.log(f"ERROR: {msg}")
        
    def set_progress(self, value, status):
        """Set progress (0.0 to 1.0) and status text"""
        self.progress = max(0.0, min(1.0, value))
        self.status_text = status
        self.log(status)
        
    def draw(self):
        """Draw the loading screen"""
        self.screen.fill(COLORS['black'])
        
        # Title
        if self.large_font:
            title = self.large_font.render("BOKEMON-SWARM", True, COLORS['amber'])
            self.screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 50))
            
            subtitle = self.large_font.render("Carrier Lock Active", True, COLORS['light_blue'])
            self.screen.blit(subtitle, (SCREEN_WIDTH//2 - subtitle.get_width()//2, 90))
        
        # Status text
        if self.font:
            status = self.font.render(self.status_text, True, COLORS['white'])
            self.screen.blit(status, (50, 150))
        
        # Progress bar
        bar_width = 400
        bar_height = 30
        bar_x = SCREEN_WIDTH//2 - bar_width//2
        bar_y = 200
        
        pygame.draw.rect(self.screen, COLORS['dark_purple'], (bar_x, bar_y, bar_width, bar_height))
        fill_width = int(bar_width * self.progress)
        if fill_width > 0:
            pygame.draw.rect(self.screen, COLORS['amber'], (bar_x, bar_y, fill_width, bar_height))
        pygame.draw.rect(self.screen, COLORS['white'], (bar_x, bar_y, bar_width, bar_height), 2)
        
        # Progress percentage
        if self.font:
            pct_text = self.font.render(f"{int(self.progress * 100)}%", True, COLORS['white'])
            self.screen.blit(pct_text, (SCREEN_WIDTH//2 - pct_text.get_width()//2, bar_y + 5))
        
        # Log messages
        if self.font:
            y = 260
            for msg in self.log_messages[-5:]:
                log_surf = self.font.render(msg, True, COLORS['white'])
                self.screen.blit(log_surf, (50, y))
                y += 20
        
        # Error display
        if self.error_message and self.large_font and self.font:
            error_surf = self.large_font.render("ERROR:", True, (255, 0, 0))
            self.screen.blit(error_surf, (50, SCREEN_HEIGHT - 100))
            
            # Wrap error text
            words = self.error_message.split(' ')
            line = ""
            y = SCREEN_HEIGHT - 70
            for word in words:
                test_line = line + word + " "
                if self.font.size(test_line)[0] < SCREEN_WIDTH - 100:
                    line = test_line
                else:
                    text_surf = self.font.render(line, True, (255, 100, 100))
                    self.screen.blit(text_surf, (50, y))
                    y += 20
                    line = word + " "
            if line:
                text_surf = self.font.render(line, True, (255, 100, 100))
                self.screen.blit(text_surf, (50, y))
        
        pygame.display.flip()
        
    def pump_events(self):
        """Pump events to keep window responsive"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    def wait_for_key(self):
        """Wait for any key press"""
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False
            self.clock.tick(30)
