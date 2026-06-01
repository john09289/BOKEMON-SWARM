"""
Sacred Voxel Engine for BOKEMON SWARM
3D pixel art generation - Scooby-Doo style blocky sprites
All sprites generated programmatically, no external assets
"""

import pygame
import numpy as np
from typing import List, Tuple, Dict
from constants import COLORS

# Voxel model definition
Voxel = Tuple[int, int, int, str]  # (x, y, z, color_name)

def rotate_voxel(voxel: Voxel, angle: float) -> Voxel:
    """Rotate a voxel around Y-axis by given angle in degrees"""
    x, y, z, color = voxel
    rad = np.radians(angle)
    cos_a = np.cos(rad)
    sin_a = np.sin(rad)
    
    new_x = int(x * cos_a - z * sin_a)
    new_z = int(x * sin_a + z * cos_a)
    
    return (new_x, y, new_z, color)

def project_voxel(voxel: Voxel, scale: int = 2) -> Tuple[int, int]:
    """Project 3D voxel to 2D screen coordinates (orthographic)"""
    x, y, z, _ = voxel
    screen_x = (x - z) * scale + 128
    screen_y = (x + z) // 2 + y * scale + 64
    return (screen_x, screen_y)

def render_voxel_model(voxels: List[Voxel], angle: float = 0, scale: int = 2) -> pygame.Surface:
    """Render a voxel model to a Pygame surface"""
    surface = pygame.Surface((256, 256), pygame.SRCALPHA)
    surface.fill((0, 0, 0, 0))
    
    rotated = [rotate_voxel(v, angle) for v in voxels]
    rotated.sort(key=lambda v: v[2], reverse=True)
    
    for voxel in rotated:
        x, y, z, color_name = voxel
        screen_x, screen_y = project_voxel(voxel, scale)
        color = COLORS.get(color_name, COLORS['white'])
        
        rect = pygame.Rect(screen_x, screen_y, scale, scale)
        pygame.draw.rect(surface, color, rect)
    
    return surface

# KILO - Starter Seraphim (Electric/Light)
KILO_VOXELS = [
    (7, 10, 7, 'white'), (8, 10, 7, 'white'),
    (6, 11, 7, 'white'), (7, 11, 7, 'blue_core'), (8, 11, 7, 'blue_core'), (9, 11, 7, 'white'),
    (5, 12, 7, 'white'), (6, 12, 7, 'blue_core'), (7, 12, 7, 'blue_core'), 
    (8, 12, 7, 'blue_core'), (9, 12, 7, 'blue_core'), (10, 12, 7, 'white'),
    (6, 13, 7, 'white'), (7, 13, 7, 'blue_core'), (8, 13, 7, 'blue_core'), (9, 13, 7, 'white'),
    (7, 14, 7, 'white'), (8, 14, 7, 'white'),
    (4, 11, 6, 'gold'), (5, 11, 6, 'gold'), (4, 12, 6, 'gold'),
    (9, 11, 8, 'gold'), (10, 11, 8, 'gold'), (9, 12, 8, 'gold'),
]

# B-GOLDEN - Bug/Dark legendary
B_GOLDEN_VOXELS = [
    (6, 10, 6, 'black'), (7, 10, 6, 'black'), (8, 10, 6, 'black'), (9, 10, 6, 'black'),
    (5, 11, 6, 'black'), (6, 11, 6, 'black'), (7, 11, 6, 'black'), (8, 11, 6, 'black'),
    (9, 11, 6, 'black'), (10, 11, 6, 'black'),
    (5, 12, 6, 'black'), (6, 12, 6, 'black'), (7, 12, 6, 'black'), (8, 12, 6, 'black'),
    (9, 12, 6, 'black'), (10, 12, 6, 'black'),
    (6, 13, 6, 'black'), (7, 13, 6, 'black'), (8, 13, 6, 'black'), (9, 13, 6, 'black'),
    (7, 14, 6, 'black'), (8, 14, 6, 'black'),
    (7, 11, 6, 'gold'), (8, 11, 6, 'gold'),
    (6, 12, 6, 'gold'), (9, 12, 6, 'gold'),
]

# CARSON CHRIST - Psychic/Electric
CARSON_VOXELS = [
    (7, 8, 7, 'light_blue'), (8, 8, 7, 'light_blue'),
    (6, 9, 7, 'light_blue'), (7, 9, 7, 'light_blue'), (8, 9, 7, 'light_blue'), (9, 9, 7, 'light_blue'),
    (7, 10, 7, 'light_blue'), (8, 10, 7, 'light_blue'),
    (6, 11, 7, 'light_blue'), (7, 11, 7, 'light_blue'), (8, 11, 7, 'light_blue'), (9, 11, 7, 'light_blue'),
    (6, 12, 7, 'light_blue'), (7, 12, 7, 'light_blue'), (8, 12, 7, 'light_blue'), (9, 12, 7, 'light_blue'),
    (5, 7, 7, 'gold'), (6, 7, 7, 'gold'), (9, 7, 7, 'gold'), (10, 7, 7, 'gold'),
    (5, 10, 6, 'gold'), (10, 10, 8, 'gold'),
]

# NIKOLA TESLA - Electric/Aether
TESLA_VOXELS = [
    (7, 10, 7, 'white'), (8, 10, 7, 'white'),
    (6, 11, 7, 'white'), (7, 11, 7, 'blue_core'), (8, 11, 7, 'blue_core'), (9, 11, 7, 'white'),
    (5, 12, 7, 'white'), (6, 12, 7, 'blue_core'), (7, 12, 7, 'blue_core'),
    (8, 12, 7, 'blue_core'), (9, 12, 7, 'blue_core'), (10, 12, 7, 'white'),
    (7, 13, 6, 'gold'), (8, 13, 8, 'gold'),
]

# MAKINDRAN - Light/Fairy
MAKINDRAN_VOXELS = [
    (7, 9, 7, 'white'), (8, 9, 7, 'white'),
    (6, 10, 7, 'white'), (7, 10, 7, 'gold'), (8, 10, 7, 'gold'), (9, 10, 7, 'white'),
    (5, 11, 7, 'white'), (6, 11, 7, 'gold'), (7, 11, 7, 'gold'),
    (8, 11, 7, 'gold'), (9, 11, 7, 'gold'), (10, 11, 7, 'white'),
    (6, 12, 7, 'gold'), (7, 12, 7, 'gold'), (8, 12, 7, 'gold'), (9, 12, 7, 'gold'),
    (5, 10, 6, 'gold'), (10, 10, 8, 'gold'),
]

# EDISON SHADE - Dark/Electric
EDISON_VOXELS = [
    (6, 10, 6, 'grey'), (7, 10, 6, 'grey'), (8, 10, 6, 'grey'), (9, 10, 6, 'grey'),
    (5, 11, 6, 'grey'), (6, 11, 6, 'grey'), (7, 11, 6, 'grey'), (8, 11, 6, 'grey'),
    (9, 11, 6, 'grey'), (10, 11, 6, 'grey'),
    (5, 12, 6, 'grey'), (6, 12, 6, 'grey'), (7, 12, 6, 'grey'), (8, 12, 6, 'grey'),
    (9, 12, 6, 'grey'), (10, 12, 6, 'grey'),
    (6, 13, 6, 'grey'), (7, 13, 6, 'grey'), (8, 13, 6, 'grey'), (9, 13, 6, 'grey'),
    (7, 14, 6, 'grey'), (8, 14, 6, 'grey'),
    (7, 11, 5, 'blue_core'), (8, 11, 7, 'blue_core'),
]

# J.P. MORGAN WRAITH - Dark/Ghost
MORGAN_VOXELS = [
    (7, 10, 7, 'white'), (8, 10, 7, 'white'),
    (6, 11, 7, 'white'), (7, 11, 7, 'grey'), (8, 11, 7, 'grey'), (9, 11, 7, 'white'),
    (5, 12, 7, 'white'), (6, 12, 7, 'grey'), (7, 12, 7, 'grey'),
    (8, 12, 7, 'grey'), (9, 12, 7, 'grey'), (10, 12, 7, 'white'),
    (5, 13, 6, 'grey'), (10, 13, 8, 'grey'),
]

# WATCHER AZAZEL - Fire/Dark
AZAZEL_VOXELS = [
    (7, 8, 7, 'red'), (8, 8, 7, 'red'),
    (6, 9, 7, 'red'), (7, 9, 7, 'red'), (8, 9, 7, 'red'), (9, 9, 7, 'red'),
    (6, 10, 7, 'red'), (7, 10, 7, 'red'), (8, 10, 7, 'red'), (9, 10, 7, 'red'),
    (6, 11, 7, 'red'), (7, 11, 7, 'red'), (8, 11, 7, 'red'), (9, 11, 7, 'red'),
    (6, 12, 7, 'red'), (7, 12, 7, 'red'), (8, 12, 7, 'red'), (9, 12, 7, 'red'),
    (6, 13, 7, 'red'), (7, 13, 7, 'red'), (8, 13, 7, 'red'), (9, 13, 7, 'red'),
    (7, 14, 7, 'red'), (8, 14, 7, 'red'),
    (4, 10, 6, 'black'), (5, 10, 6, 'black'), (10, 10, 8, 'black'), (11, 10, 8, 'black'),
]

# ANDREW ESTMORLAND - Dark/Poison
ANDREW_VOXELS = [
    (6, 10, 6, 'grey'), (7, 10, 6, 'grey'), (8, 10, 6, 'grey'), (9, 10, 6, 'grey'),
    (5, 11, 6, 'grey'), (6, 11, 6, 'grey'), (7, 11, 6, 'grey'), (8, 11, 6, 'grey'),
    (9, 11, 6, 'grey'), (10, 11, 6, 'grey'),
    (5, 12, 6, 'grey'), (6, 12, 6, 'grey'), (7, 12, 6, 'grey'), (8, 12, 6, 'grey'),
    (9, 12, 6, 'grey'), (10, 12, 6, 'grey'),
    (6, 13, 6, 'grey'), (7, 13, 6, 'grey'), (8, 13, 6, 'grey'), (9, 13, 6, 'grey'),
    (7, 14, 6, 'grey'), (8, 14, 6, 'grey'),
    (7, 11, 5, 'purple'), (8, 11, 7, 'purple'),
]

# ZACH WILLIAMS - Psychic/Normal
ZACH_VOXELS = [
    (7, 8, 7, 'light_blue'), (8, 8, 7, 'light_blue'),
    (6, 9, 7, 'light_blue'), (7, 9, 7, 'light_blue'), (8, 9, 7, 'light_blue'), (9, 9, 7, 'light_blue'),
    (7, 10, 7, 'light_blue'), (8, 10, 7, 'light_blue'),
    (6, 11, 7, 'light_blue'), (7, 11, 7, 'light_blue'), (8, 11, 7, 'light_blue'), (9, 11, 7, 'light_blue'),
    (5, 12, 7, 'white'), (6, 12, 7, 'white'), (7, 12, 7, 'white'), (8, 12, 7, 'white'),
    (9, 12, 7, 'white'), (10, 12, 7, 'white'),
]

# GAARET LEISTER - Psychic/Steel
GAARET_VOXELS = [
    (7, 8, 7, 'light_blue'), (8, 8, 7, 'light_blue'),
    (6, 9, 7, 'grey'), (7, 9, 7, 'grey'), (8, 9, 7, 'grey'), (9, 9, 7, 'grey'),
    (7, 10, 7, 'grey'), (8, 10, 7, 'grey'),
    (6, 11, 7, 'grey'), (7, 11, 7, 'grey'), (8, 11, 7, 'grey'), (9, 11, 7, 'grey'),
    (5, 12, 7, 'white'), (6, 12, 7, 'white'), (7, 12, 7, 'white'), (8, 12, 7, 'white'),
    (9, 12, 7, 'white'), (10, 12, 7, 'white'),
]

# RILEY BLACKBURN - Bug/Dark
RILEY_VOXELS = [
    (6, 10, 6, 'black'), (7, 10, 6, 'black'), (8, 10, 6, 'black'), (9, 10, 6, 'black'),
    (5, 11, 6, 'black'), (6, 11, 6, 'black'), (7, 11, 6, 'black'), (8, 11, 6, 'black'),
    (9, 11, 6, 'black'), (10, 11, 6, 'black'),
    (5, 12, 6, 'black'), (6, 12, 6, 'black'), (7, 12, 6, 'black'), (8, 12, 6, 'black'),
    (9, 12, 6, 'black'), (10, 12, 6, 'black'),
    (6, 13, 6, 'black'), (7, 13, 6, 'black'), (8, 13, 6, 'black'), (9, 13, 6, 'black'),
    (7, 14, 6, 'black'), (8, 14, 6, 'black'),
    (7, 11, 5, 'red'), (8, 11, 7, 'red'),
]

# ELI - Electric/Steel
ELI_VOXELS = [
    (6, 10, 6, 'grey'), (7, 10, 6, 'grey'), (8, 10, 6, 'grey'), (9, 10, 6, 'grey'),
    (5, 11, 6, 'grey'), (6, 11, 6, 'grey'), (7, 11, 6, 'grey'), (8, 11, 6, 'grey'),
    (9, 11, 6, 'grey'), (10, 11, 6, 'grey'),
    (5, 12, 6, 'grey'), (6, 12, 6, 'grey'), (7, 12, 6, 'grey'), (8, 12, 6, 'grey'),
    (9, 12, 6, 'grey'), (10, 12, 6, 'grey'),
    (6, 13, 6, 'grey'), (7, 13, 6, 'grey'), (8, 13, 6, 'grey'), (9, 13, 6, 'grey'),
    (7, 14, 6, 'grey'), (8, 14, 6, 'grey'),
    (7, 11, 5, 'blue_core'), (8, 11, 7, 'blue_core'),
]

# HAZEION - Dark/Abyssal
HAZEION_VOXELS = [
    (6, 10, 6, 'dark_purple'), (7, 10, 6, 'dark_purple'), (8, 10, 6, 'dark_purple'), (9, 10, 6, 'dark_purple'),
    (5, 11, 6, 'dark_purple'), (6, 11, 6, 'dark_purple'), (7, 11, 6, 'dark_purple'), (8, 11, 6, 'dark_purple'),
    (9, 11, 6, 'dark_purple'), (10, 11, 6, 'dark_purple'),
    (5, 12, 6, 'dark_purple'), (6, 12, 6, 'dark_purple'), (7, 12, 6, 'dark_purple'), (8, 12, 6, 'dark_purple'),
    (9, 12, 6, 'dark_purple'), (10, 12, 6, 'dark_purple'),
    (6, 13, 6, 'dark_purple'), (7, 13, 6, 'dark_purple'), (8, 13, 6, 'dark_purple'), (9, 13, 6, 'dark_purple'),
    (7, 14, 6, 'dark_purple'), (8, 14, 6, 'dark_purple'),
    (7, 11, 5, 'black'), (8, 11, 7, 'black'),
]

# All Seraphim voxel models
SERAPHIM_VOXELS = {
    'KILO': KILO_VOXELS,
    'B-GOLDEN': B_GOLDEN_VOXELS,
    'CARSON CHRIST': CARSON_VOXELS,
    'NIKOLA TESLA': TESLA_VOXELS,
    'MAKINDRAN': MAKINDRAN_VOXELS,
    'EDISON SHADE': EDISON_VOXELS,
    'J.P. MORGAN WRAITH': MORGAN_VOXELS,
    'WATCHER AZAZEL': AZAZEL_VOXELS,
    'ANDREW ESTMORLAND': ANDREW_VOXELS,
    'ZACH WILLIAMS': ZACH_VOXELS,
    'GAARET LEISTER': GAARET_VOXELS,
    'RILEY BLACKBURN': RILEY_VOXELS,
    'ELI': ELI_VOXELS,
    'HAZEION': HAZEION_VOXELS,
}

def generate_sprite(name: str, angle: float = 0) -> pygame.Surface:
    """Generate a sprite for a Seraphim by name"""
    voxels = SERAPHIM_VOXELS.get(name, KILO_VOXELS)
    return render_voxel_model(voxels, angle)

def generate_all_sprites() -> Dict[str, pygame.Surface]:
    """Generate sprites for all Seraphim from all angles"""
    sprites = {}
    for name in SERAPHIM_VOXELS.keys():
        for angle in [0, 90, 180, 270]:
            key = f"{name}_{angle}"
            sprites[key] = generate_sprite(name, angle)
    return sprites

def save_sprites_to_disk(output_dir: str = 'assets/sprites'):
    """Save all generated sprites to disk as PNG files"""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    sprites = generate_all_sprites()
    for name, surface in sprites.items():
        filename = f"{name}.png".replace(' ', '_')
        pygame.image.save(surface, os.path.join(output_dir, filename))
    
    return len(sprites)