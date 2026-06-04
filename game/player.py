"""
Player class for BOKEMON SWARM
"""

import pygame
from typing import List, Optional
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, PLAYER_SPEED, calculate_hj
from .seraphim import Seraphim, get_seraphim

class Player:
    def __init__(self, name: str = "LX"):
        self.name = name
        self.x = 400
        self.y = 300
        self.width = 32
        self.height = 32
        self.speed = PLAYER_SPEED
        self.seraphim_party: List[Seraphim] = []
        self.active_seraphim: Optional[Seraphim] = None
        self.energy_bank = calculate_hj(50)
        self.max_energy = calculate_hj(100)
        self.mercy_shards = 0
        self.victory_sparks = 0
        self.correction_crystals = 0
        
    def add_seraphim(self, seraphim_name: str):
        """Add a Seraphim to the player's party"""
        seraphim = get_seraphim(seraphim_name)
        if seraphim and len(self.seraphim_party) < 6:
            self.seraphim_party.append(seraphim)
            if not self.active_seraphim:
                self.active_seraphim = seraphim
                
    def set_active_seraphim(self, index: int):
        """Set the active Seraphim by party index"""
        if 0 <= index < len(self.seraphim_party):
            self.active_seraphim = self.seraphim_party[index]
            
    def update_energy(self, amount: float):
        """Update energy bank, clamped to max"""
        self.energy_bank = min(self.max_energy, max(0, self.energy_bank + amount))
        
    def can_afford_move(self, hj_cost: float) -> bool:
        """Check if player can afford a move"""
        return self.energy_bank >= hj_cost
        
    def get_allies(self) -> List[Seraphim]:
        """Get all party members except the active one"""
        return [s for s in self.seraphim_party if s != self.active_seraphim]

    def update(self):
        """Update player state"""
        pass
        
    def move(self, dx: int, dy: int, world_bounds: tuple):
        """Move player within world bounds"""
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed
        
        self.x = max(0, min(SCREEN_WIDTH - self.width, new_x))
        self.y = max(0, min(SCREEN_HEIGHT - self.height, new_y))
        
    def draw(self, screen: pygame.Surface):
        """Draw player as simple rectangle"""
        color = (255, 176, 0)  # Amber
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (255, 255, 255), rect, 2)