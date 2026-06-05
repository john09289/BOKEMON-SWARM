"""
Bokeball NBA Jam mini-game
A simple basketball shooting game with Bokemon-style flair
Carrier: 11.71875 Hz
"""

import pygame
import random
import math
from constants import COLORS, SCREEN_WIDTH, SCREEN_HEIGHT, CARRIER


class BokeballJam:
    def __init__(self, screen, player_seraphim):
        self.screen = screen
        self.player = player_seraphim
        self.state = "aiming"  # aiming, shooting, result
        self.clock = pygame.time.Clock()
        
        # Ball physics
        self.ball_x = SCREEN_WIDTH // 2
        self.ball_y = SCREEN_HEIGHT - 100
        self.ball_radius = 15
        self.ball_vx = 0
        self.ball_vy = 0
        self.ball_launched = False
        
        # Hoop position
        self.hoop_x = SCREEN_WIDTH // 2 + random.randint(-100, 100)
        self.hoop_y = 150
        self.hoop_radius = 40
        
        # Aiming
        self.aim_angle = -math.pi / 4  # 45 degrees up
        self.aim_power = 15
        self.max_power = 25
        self.min_power = 5
        
        # Score
        self.score = 0
        self.shots = 0
        self.made = 0
        
        # Timer
        self.time_left = 60  # 60 seconds
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 1000)
        
        # Font
        self.font = pygame.font.SysFont('monospace', 24)
        self.large_font = pygame.font.SysFont('monospace', 36)
        
    def handle_event(self, event):
        if self.state == "aiming":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.aim_angle -= 0.05
                elif event.key == pygame.K_RIGHT:
                    self.aim_angle += 0.05
                elif event.key == pygame.K_UP:
                    self.aim_power = min(self.max_power, self.aim_power + 0.5)
                elif event.key == pygame.K_DOWN:
                    self.aim_power = max(self.min_power, self.aim_power - 0.5)
                elif event.key == pygame.K_SPACE:
                    self.shoot()
                elif event.key == pygame.K_ESCAPE:
                    return "exit"
        elif self.state == "result":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.reset_shot()
                elif event.key == pygame.K_ESCAPE:
                    return "exit"
        
        if event.type == self.timer_event:
            self.time_left -= 1
            if self.time_left <= 0:
                return "time_up"
        
        return None
    
    def shoot(self):
        self.ball_vx = math.cos(self.aim_angle) * self.aim_power
        self.ball_vy = math.sin(self.aim_angle) * self.aim_power
        self.ball_launched = True
        self.state = "shooting"
        self.shots += 1
    
    def reset_shot(self):
        self.ball_x = SCREEN_WIDTH // 2
        self.ball_y = SCREEN_HEIGHT - 100
        self.ball_vx = 0
        self.ball_vy = 0
        self.ball_launched = False
        self.hoop_x = SCREEN_WIDTH // 2 + random.randint(-100, 100)
        self.state = "aiming"
    
    def update(self):
        if self.state == "shooting" and self.ball_launched:
            # Gravity
            self.ball_vy += 0.5
            self.ball_x += self.ball_vx
            self.ball_y += self.ball_vy
            
            # Check if ball goes off screen
            if self.ball_y > SCREEN_HEIGHT + 50 or self.ball_x < -50 or self.ball_x > SCREEN_WIDTH + 50:
                self.state = "result"
                self.result_text = "MISS!"
                self.result_color = COLORS['red']
            
            # Check hoop collision
            dx = self.ball_x - self.hoop_x
            dy = self.ball_y - self.hoop_y
            dist = math.sqrt(dx*dx + dy*dy)
            
            if dist < self.hoop_radius + self.ball_radius:
                # Ball went through hoop!
                self.made += 1
                self.score += 2  # 2 points per basket
                self.state = "result"
                self.result_text = "SWISH! +2"
                self.result_color = COLORS['gold']
            
            # Check if ball hits rim
            rim_dist = abs(dist - self.hoop_radius)
            if rim_dist < self.ball_radius and dist > 0:
                # Bounce off rim
                nx = dx / dist
                ny = dy / dist
                dot = self.ball_vx * nx + self.ball_vy * ny
                self.ball_vx = (self.ball_vx - 2 * dot * nx) * 0.7
                self.ball_vy = (self.ball_vy - 2 * dot * ny) * 0.7
    
    def draw(self):
        self.screen.fill(COLORS['black'])
        
        # Draw court
        court_rect = pygame.Rect(50, SCREEN_HEIGHT - 150, SCREEN_WIDTH - 100, 100)
        pygame.draw.rect(self.screen, (50, 50, 50), court_rect)
        pygame.draw.rect(self.screen, COLORS['amber'], court_rect, 3)
        
        # Draw three-point line (arc)
        pygame.draw.arc(self.screen, COLORS['amber'], 
                       pygame.Rect(100, SCREEN_HEIGHT - 300, SCREEN_WIDTH - 200, 200),
                       math.pi, 0, 3)
        
        # Draw hoop
        pygame.draw.circle(self.screen, COLORS['red'], (int(self.hoop_x), int(self.hoop_y)), self.hoop_radius, 4)
        pygame.draw.circle(self.screen, COLORS['white'], (int(self.hoop_x), int(self.hoop_y)), 5)
        
        # Draw backboard
        bb_rect = pygame.Rect(self.hoop_x - 40, self.hoop_y - 60, 80, 10)
        pygame.draw.rect(self.screen, COLORS['white'], bb_rect)
        
        # Draw ball
        if not self.ball_launched or self.state != "result":
            pygame.draw.circle(self.screen, COLORS['orange'], (int(self.ball_x), int(self.ball_y)), self.ball_radius)
            # Ball lines
            pygame.draw.line(self.screen, COLORS['black'], 
                           (self.ball_x - self.ball_radius, self.ball_y),
                           (self.ball_x + self.ball_radius, self.ball_y), 2)
            pygame.draw.line(self.screen, COLORS['black'],
                           (self.ball_x, self.ball_y - self.ball_radius),
                           (self.ball_x, self.ball_y + self.ball_radius), 2)
        
        # Draw aim line
        if self.state == "aiming":
            aim_end_x = self.ball_x + math.cos(self.aim_angle) * 50
            aim_end_y = self.ball_y + math.sin(self.aim_angle) * 50
            pygame.draw.line(self.screen, COLORS['gold'], 
                           (self.ball_x, self.ball_y),
                           (aim_end_x, aim_end_y), 3)
            
            # Power bar
            bar_width = 200
            bar_height = 20
            bar_x = SCREEN_WIDTH // 2 - bar_width // 2
            bar_y = SCREEN_HEIGHT - 30
            pygame.draw.rect(self.screen, COLORS['grey'], (bar_x, bar_y, bar_width, bar_height))
            fill_width = int((self.aim_power / self.max_power) * bar_width)
            pygame.draw.rect(self.screen, COLORS['amber'], (bar_x, bar_y, fill_width, bar_height))
            pygame.draw.rect(self.screen, COLORS['white'], (bar_x, bar_y, bar_width, bar_height), 2)
        
        # Draw HUD
        score_text = self.font.render(f"Score: {self.score}", True, COLORS['white'])
        shots_text = self.font.render(f"Shots: {self.shots}  Made: {self.made}", True, COLORS['white'])
        time_text = self.font.render(f"Time: {self.time_left}", True, COLORS['amber'] if self.time_left > 10 else COLORS['red'])
        player_text = self.font.render(f"{self.player.name}", True, COLORS['blue_core'])
        
        self.screen.blit(score_text, (20, 20))
        self.screen.blit(shots_text, (20, 50))
        self.screen.blit(time_text, (SCREEN_WIDTH - 150, 20))
        self.screen.blit(player_text, (SCREEN_WIDTH - 200, 50))
        
        # Draw instructions
        if self.state == "aiming":
            inst_text = self.font.render("← → Aim   ↑ ↓ Power   SPACE Shoot   ESC Exit", True, COLORS['grey'])
            self.screen.blit(inst_text, (SCREEN_WIDTH // 2 - inst_text.get_width() // 2, SCREEN_HEIGHT - 80))
        
        # Draw result
        if self.state == "result":
            result_surf = self.large_font.render(self.result_text, True, self.result_color)
            self.screen.blit(result_surf, (SCREEN_WIDTH // 2 - result_surf.get_width() // 2, SCREEN_HEIGHT // 2))
            cont_text = self.font.render("SPACE to continue   ESC to exit", True, COLORS['white'])
            self.screen.blit(cont_text, (SCREEN_WIDTH // 2 - cont_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        
        # Draw carrier frequency
        carrier_text = self.font.render(f"Carrier: {CARRIER} Hz", True, COLORS['indigo'])
        self.screen.blit(carrier_text, (20, SCREEN_HEIGHT - 30))
    
    def run(self):
        """Run the mini-game, return final score"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.score
                result = self.handle_event(event)
                if result == "exit":
                    return self.score
                if result == "time_up":
                    self.state = "result"
                    self.result_text = f"TIME UP! Final: {self.made}/{self.shots}"
                    self.result_color = COLORS['amber']
            
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        
        return self.score
