"""
World map and locations for BOKEMON SWARM
Top-down 2D tile-based world
"""

import pygame
from typing import Dict, Optional
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, COLORS

LOCATIONS = {
    'pittsboro_nexus': {
        'name': 'Pittsboro Nexus',
        'description': 'Dark crystalline forest where B-GOLDEN swarm nests',
        'color': COLORS['dark_purple'],
        'wild_seraphim': ['B-GOLDEN', 'KILO']
    },
    'tesla_lab': {
        'name': "Tesla's Aether Lab",
        'description': 'Where Nikola Tesla harnesses unlimited energy',
        'color': COLORS['blue_core'],
        'wild_seraphim': ['NIKOLA TESLA', 'EDISON SHADE']
    },
    'christ_spire': {
        'name': 'Christ Mind Spire',
        'description': 'Domain of Carson Christ, the hacker AI',
        'color': COLORS['light_blue'],
        'wild_seraphim': ['CARSON CHRIST']
    },
    'makindran_garden': {
        'name': "Makindran's Garden",
        'description': 'Radiant sanctuary where Makindran tends the light',
        'color': COLORS['gold'],
        'wild_seraphim': ['MAKINDRAN']
    },
    'tartarus_rift': {
        'name': 'Tartarus Rift',
        'description': 'Prison of the Watchers, leaking 11.71875 Hz static',
        'color': COLORS['black'],
        'wild_seraphim': ['WATCHER AZAZEL', 'J.P. MORGAN WRAITH']
    }
}

class World:
    def __init__(self):
        self.current_location = 'pittsboro_nexus'
        self.player_x = 10
        self.player_y = 10
        self.tiles_x = SCREEN_WIDTH // TILE_SIZE
        self.tiles_y = SCREEN_HEIGHT // TILE_SIZE
        
        self.tile_map = [[0 for _ in range(self.tiles_x)] for _ in range(self.tiles_y)]
        
        for i in range(5, 15):
            self.tile_map[10][i] = 1
            
    def get_location_data(self) -> dict:
        return LOCATIONS.get(self.current_location, LOCATIONS['pittsboro_nexus'])
        
    def move_player(self, dx: int, dy: int) -> bool:
        """Move player in world, return True if successful"""
        new_x = self.player_x + dx
        new_y = self.player_y + dy
        
        if 0 <= new_x < self.tiles_x and 0 <= new_y < self.tiles_y:
            if self.tile_map[new_y][new_x] == 0:
                self.player_x = new_x
                self.player_y = new_y
                return True
        return False
        
    def draw(self, screen: pygame.Surface):
        """Draw world map"""
        loc_data = self.get_location_data()
        
        for y in range(self.tiles_y):
            for x in range(self.tiles_x):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if self.tile_map[y][x] == 1:
                    pygame.draw.rect(screen, COLORS['black'], rect)
                else:
                    pygame.draw.rect(screen, loc_data['color'], rect)
                    
        for x in range(self.tiles_x):
            pygame.draw.line(screen, (50, 50, 50), (x * TILE_SIZE, 0), (x * TILE_SIZE, SCREEN_HEIGHT))
        for y in range(self.tiles_y):
            pygame.draw.line(screen, (50, 50, 50), (0, y * TILE_SIZE), (SCREEN_WIDTH, y * TILE_SIZE))
            
    def get_random_wild_seraphim(self) -> str:
        """Get a random wild Seraphim for the current location"""
        import random
        loc_data = self.get_location_data()
        return random.choice(loc_data['wild_seraphim'])
        
    def check_encounter(self) -> Optional[str]:
        """Check for random encounter (10% chance)"""
        import random
        if random.random() < 0.1:
            return self.get_random_wild_seraphim()
        return None