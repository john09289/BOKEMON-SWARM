"""
Battle system for BOKEMON SWARM
Turn-based Pokémon-style combat
"""

import pygame
import random
from typing import Optional, List
from constants import COLORS, PHI, CARRIER
from .seraphim import Seraphim, Move

class BattleSystem:
    def __init__(self, player_seraphim: Seraphim, enemy_seraphim: Seraphim):
        self.player = player_seraphim
        self.enemy = enemy_seraphim
        self.player_hp = player_seraphim.max_hp
        self.enemy_hp = enemy_seraphim.max_hp
        self.turn = "player"
        self.battle_log: List[str] = []
        self.carrier_lock_active = False
        self.carrier_lock_timer = 0
        
    def player_attack(self, move: Move) -> bool:
        """Execute player's move, return True if successful"""
        if self.player_hp <= 0 or self.enemy_hp <= 0:
            return False
            
        if move.hj_cost > 0:
            if move.name == "Carrier Lock":
                self.carrier_lock_active = True
                self.carrier_lock_timer = 180
                self.battle_log.append("Press W to lock onto target!")
                return True
                
            damage = int(move.power * (1 if random.random() > 0.1 else 0.5))
            self.enemy_hp = max(0, self.enemy_hp - damage)
            self.battle_log.append(f"{self.player.name} used {move.name}! Dealt {damage} damage.")
            
        self.turn = "enemy"
        return True
        
    def carrier_lock_success(self) -> bool:
        """Called when player successfully hits Carrier Lock timing"""
        if self.carrier_lock_active:
            self.carrier_lock_active = False
            damage = int(80 * PHI)
            self.enemy_hp = max(0, self.enemy_hp - damage)
            self.battle_log.append(f"Carrier Lock successful! Dealt {damage} damage (x{PHI:.2f} bonus).")
            self.turn = "enemy"
            return True
        return False
        
    def enemy_turn(self):
        """Enemy AI takes its turn"""
        if self.enemy_hp <= 0:
            return
            
        for move in self.enemy.moves:
            if move.hj_cost > 0:
                damage = int(move.power * (0.8 + random.random() * 0.4))
                self.player_hp = max(0, self.player_hp - damage)
                self.battle_log.append(f"{self.enemy.name} used {move.name}! Dealt {damage} damage.")
                break
                
        self.turn = "player"
        
    def is_battle_over(self) -> bool:
        """Check if battle has ended"""
        return self.player_hp <= 0 or self.enemy_hp <= 0
        
    def get_winner(self) -> Optional[str]:
        """Return winner name or None if ongoing"""
        if self.enemy_hp <= 0:
            return "player"
        elif self.player_hp <= 0:
            return "enemy"
        return None
        
    def draw(self, screen: pygame.Surface):
        """Draw battle interface"""
        screen.fill(COLORS['indigo'])
        
        enemy_rect = pygame.Rect(400, 50, 128, 128)
        pygame.draw.rect(screen, COLORS['white'], enemy_rect, 2)
        
        hp_width = 200
        hp_height = 20
        enemy_hp_width = int(hp_width * (self.enemy_hp / self.enemy.max_hp))
        hp_rect = pygame.Rect(350, 180, hp_width, hp_height)
        pygame.draw.rect(screen, COLORS['red'], hp_rect)
        pygame.draw.rect(screen, COLORS['white'], (350, 180, enemy_hp_width, hp_height))
        
        player_rect = pygame.Rect(100, 350, 128, 128)
        pygame.draw.rect(screen, COLORS['amber'], player_rect, 2)
        
        player_hp_width = int(hp_width * (self.player_hp / self.player.max_hp))
        player_hp_rect = pygame.Rect(90, 480, hp_width, hp_height)
        pygame.draw.rect(screen, COLORS['red'], player_hp_rect)
        pygame.draw.rect(screen, COLORS['white'], (90, 480, player_hp_width, hp_height))
        
        font = pygame.font.SysFont('monospace', 14)
        for i, log in enumerate(self.battle_log[-5:]):
            text = font.render(log, True, COLORS['white'])
            screen.blit(text, (50, 520 + i * 20))
            
        if self.carrier_lock_active:
            pulse = int(255 * (0.5 + 0.5 * abs(pygame.time.get_ticks() % 1000 - 500) / 500))
            lock_text = font.render("PRESS W NOW!", True, (pulse, pulse, 0))
            screen.blit(lock_text, (300, 250))