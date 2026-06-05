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

# HEIDI ANDERSON CHRIST - Fighting/Fairy gymnast
HEIDI_VOXELS = [
    # Head (pink leotard)
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Torso (pink leotard)
    (6, 10, 7, 'white'), (7, 10, 7, 'white'), (8, 10, 7, 'white'), (9, 10, 7, 'white'),
    (6, 11, 7, 'white'), (7, 11, 7, 'white'), (8, 11, 7, 'white'), (9, 11, 7, 'white'),
    (6, 12, 7, 'white'), (7, 12, 7, 'white'), (8, 12, 7, 'white'), (9, 12, 7, 'white'),
    # Legs (leotard)
    (6, 13, 7, 'white'), (7, 13, 7, 'white'), (8, 13, 7, 'white'), (9, 13, 7, 'white'),
    (6, 14, 7, 'white'), (7, 14, 7, 'white'), (8, 14, 7, 'white'), (9, 14, 7, 'white'),
    # Arms (raised in backflip pose)
    (5, 10, 6, 'white'), (4, 10, 5, 'white'),
    (10, 10, 8, 'white'), (11, 10, 9, 'white'),
    # Fairy wings (gold sparkle)
    (5, 9, 6, 'gold'), (6, 9, 5, 'gold'),
    (10, 9, 8, 'gold'), (9, 9, 9, 'gold'),
    # Hair (blonde)
    (6, 8, 6, 'gold'), (7, 8, 6, 'gold'), (8, 8, 6, 'gold'), (9, 8, 6, 'gold'),
]

# TRUMP - Normal/Fire
TRUMP_VOXELS = [
    # Head (skin tone)
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Hair (blonde)
    (6, 8, 6, 'gold'), (7, 8, 6, 'gold'), (8, 8, 6, 'gold'), (9, 8, 6, 'gold'),
    # Suit (dark blue)
    (6, 10, 7, 'blue_core'), (7, 10, 7, 'blue_core'), (8, 10, 7, 'blue_core'), (9, 10, 7, 'blue_core'),
    (6, 11, 7, 'blue_core'), (7, 11, 7, 'blue_core'), (8, 11, 7, 'blue_core'), (9, 11, 7, 'blue_core'),
    (6, 12, 7, 'blue_core'), (7, 12, 7, 'blue_core'), (8, 12, 7, 'blue_core'), (9, 12, 7, 'blue_core'),
    # Red tie
    (7, 10, 7, 'red'), (7, 11, 7, 'red'),
    # Legs
    (6, 13, 7, 'blue_core'), (7, 13, 7, 'blue_core'), (8, 13, 7, 'blue_core'), (9, 13, 7, 'blue_core'),
    (6, 14, 7, 'grey'), (7, 14, 7, 'grey'), (8, 14, 7, 'grey'), (9, 14, 7, 'grey'),
]

# BARRON - Normal/Psychic
BARRON_VOXELS = [
    # Head (tall, pale)
    (7, 7, 7, 'white'), (8, 7, 7, 'white'),
    (6, 8, 7, 'white'), (7, 8, 7, 'white'), (8, 8, 7, 'white'), (9, 8, 7, 'white'),
    # Hair (blonde, neat)
    (6, 7, 6, 'gold'), (7, 7, 6, 'gold'), (8, 7, 6, 'gold'), (9, 7, 6, 'gold'),
    # Suit (dark)
    (6, 9, 7, 'grey'), (7, 9, 7, 'grey'), (8, 9, 7, 'grey'), (9, 9, 7, 'grey'),
    (6, 10, 7, 'grey'), (7, 10, 7, 'grey'), (8, 10, 7, 'grey'), (9, 10, 7, 'grey'),
    (6, 11, 7, 'grey'), (7, 11, 7, 'grey'), (8, 11, 7, 'grey'), (9, 11, 7, 'grey'),
    # Legs
    (6, 12, 7, 'grey'), (7, 12, 7, 'grey'), (8, 12, 7, 'grey'), (9, 12, 7, 'grey'),
    (6, 13, 7, 'grey'), (7, 13, 7, 'grey'), (8, 13, 7, 'grey'), (9, 13, 7, 'grey'),
]

# SAMBA QUEEN - Fighting/Fire
SAMBA_QUEEN_VOXELS = [
    # Head
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Hair (flowing, dark)
    (5, 8, 6, 'black'), (6, 8, 6, 'black'), (9, 8, 8, 'black'), (10, 8, 8, 'black'),
    # Dress (red/orange)
    (6, 10, 7, 'red'), (7, 10, 7, 'red'), (8, 10, 7, 'red'), (9, 10, 7, 'red'),
    (5, 11, 7, 'red'), (6, 11, 7, 'red'), (7, 11, 7, 'red'), (8, 11, 7, 'red'), (9, 11, 7, 'red'), (10, 11, 7, 'red'),
    (5, 12, 7, 'red'), (6, 12, 7, 'red'), (7, 12, 7, 'red'), (8, 12, 7, 'red'), (9, 12, 7, 'red'), (10, 12, 7, 'red'),
    # Legs
    (6, 13, 7, 'white'), (7, 13, 7, 'white'), (8, 13, 7, 'white'), (9, 13, 7, 'white'),
]

# CAPOEIRA MASTER - Fighting/Grass
CAPOEIRA_MASTER_VOXELS = [
    # Head
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Hair (dark, in bun)
    (7, 8, 6, 'black'), (8, 8, 6, 'black'),
    # Outfit (green/yellow)
    (6, 10, 7, 'green'), (7, 10, 7, 'green'), (8, 10, 7, 'green'), (9, 10, 7, 'green'),
    (6, 11, 7, 'green'), (7, 11, 7, 'green'), (8, 11, 7, 'green'), (9, 11, 7, 'green'),
    (6, 12, 7, 'green'), (7, 12, 7, 'green'), (8, 12, 7, 'green'), (9, 12, 7, 'green'),
    # Belt (yellow)
    (6, 12, 7, 'gold'), (7, 12, 7, 'gold'), (8, 12, 7, 'gold'), (9, 12, 7, 'gold'),
    # Legs
    (6, 13, 7, 'white'), (7, 13, 7, 'white'), (8, 13, 7, 'white'), (9, 13, 7, 'white'),
]

# SUMO CHAMPION - Ground/Fighting
SUMO_CHAMPION_VOXELS = [
    # Head (large)
    (6, 8, 6, 'white'), (7, 8, 6, 'white'), (8, 8, 6, 'white'), (9, 8, 6, 'white'),
    (6, 9, 6, 'white'), (7, 9, 6, 'white'), (8, 9, 6, 'white'), (9, 9, 6, 'white'),
    # Hair (topknot)
    (7, 7, 7, 'black'), (8, 7, 7, 'black'),
    # Massive body
    (5, 10, 6, 'white'), (6, 10, 6, 'white'), (7, 10, 6, 'white'), (8, 10, 6, 'white'), (9, 10, 6, 'white'), (10, 10, 6, 'white'),
    (5, 11, 6, 'white'), (6, 11, 6, 'white'), (7, 11, 6, 'white'), (8, 11, 6, 'white'), (9, 11, 6, 'white'), (10, 11, 6, 'white'),
    (5, 12, 6, 'white'), (6, 12, 6, 'white'), (7, 12, 6, 'white'), (8, 12, 6, 'white'), (9, 12, 6, 'white'), (10, 12, 6, 'white'),
    # Mawashi (belt)
    (5, 13, 6, 'black'), (6, 13, 6, 'black'), (7, 13, 6, 'black'), (8, 13, 6, 'black'), (9, 13, 6, 'black'), (10, 13, 6, 'black'),
    # Legs
    (6, 14, 6, 'white'), (7, 14, 6, 'white'), (8, 14, 6, 'white'), (9, 14, 6, 'white'),
]

# KUNG FU MASTER - Fighting/Psychic
KUNG_FU_MASTER_VOXELS = [
    # Head
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Hair (topknot)
    (7, 8, 6, 'black'), (8, 8, 6, 'black'),
    # Robe (light blue)
    (6, 10, 7, 'light_blue'), (7, 10, 7, 'light_blue'), (8, 10, 7, 'light_blue'), (9, 10, 7, 'light_blue'),
    (6, 11, 7, 'light_blue'), (7, 11, 7, 'light_blue'), (8, 11, 7, 'light_blue'), (9, 11, 7, 'light_blue'),
    (6, 12, 7, 'light_blue'), (7, 12, 7, 'light_blue'), (8, 12, 7, 'light_blue'), (9, 12, 7, 'light_blue'),
    # Sash (red)
    (7, 12, 7, 'red'), (8, 12, 7, 'red'),
    # Legs
    (6, 13, 7, 'light_blue'), (7, 13, 7, 'light_blue'), (8, 13, 7, 'light_blue'), (9, 13, 7, 'light_blue'),
]

# BALLET DIVA - Fairy/Psychic
BALLET_DIVA_VOXELS = [
    # Head
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Hair (bun)
    (7, 8, 6, 'gold'), (8, 8, 6, 'gold'),
    # Tutu (pink)
    (5, 10, 7, 'pink'), (6, 10, 7, 'pink'), (7, 10, 7, 'pink'), (8, 10, 7, 'pink'), (9, 10, 7, 'pink'), (10, 10, 7, 'pink'),
    (5, 11, 7, 'pink'), (6, 11, 7, 'pink'), (7, 11, 7, 'pink'), (8, 11, 7, 'pink'), (9, 11, 7, 'pink'), (10, 11, 7, 'pink'),
    # Bodice
    (6, 10, 7, 'pink'), (7, 10, 7, 'pink'), (8, 10, 7, 'pink'), (9, 10, 7, 'pink'),
    # Legs (tights)
    (6, 12, 7, 'white'), (7, 12, 7, 'white'), (8, 12, 7, 'white'), (9, 12, 7, 'white'),
    (6, 13, 7, 'white'), (7, 13, 7, 'white'), (8, 13, 7, 'white'), (9, 13, 7, 'white'),
    # Ballet shoes
    (6, 14, 7, 'pink'), (7, 14, 7, 'pink'), (8, 14, 7, 'pink'), (9, 14, 7, 'pink'),
]

# HIP HOP LEGEND - Normal/Dark
HIP_HOP_LEGEND_VOXELS = [
    # Head
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Hat (backwards cap)
    (6, 8, 6, 'red'), (7, 8, 6, 'red'), (8, 8, 6, 'red'), (9, 8, 6, 'red'),
    # Hoodie (dark)
    (5, 10, 6, 'dark_purple'), (6, 10, 6, 'dark_purple'), (7, 10, 6, 'dark_purple'), (8, 10, 6, 'dark_purple'), (9, 10, 6, 'dark_purple'), (10, 10, 6, 'dark_purple'),
    (5, 11, 6, 'dark_purple'), (6, 11, 6, 'dark_purple'), (7, 11, 6, 'dark_purple'), (8, 11, 6, 'dark_purple'), (9, 11, 6, 'dark_purple'), (10, 11, 6, 'dark_purple'),
    # Chain (gold)
    (7, 11, 6, 'gold'), (8, 11, 6, 'gold'),
    # Pants (baggy)
    (6, 12, 6, 'dark_purple'), (7, 12, 6, 'dark_purple'), (8, 12, 6, 'dark_purple'), (9, 12, 6, 'dark_purple'),
    (6, 13, 6, 'dark_purple'), (7, 13, 6, 'dark_purple'), (8, 13, 6, 'dark_purple'), (9, 13, 6, 'dark_purple'),
    # Shoes
    (6, 14, 6, 'white'), (7, 14, 6, 'white'), (8, 14, 6, 'white'), (9, 14, 6, 'white'),
]

# METALHEAD - Dark/Rock
METALHEAD_VOXELS = [
    # Head
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Long hair (black)
    (5, 9, 6, 'black'), (6, 9, 6, 'black'), (9, 9, 8, 'black'), (10, 9, 8, 'black'),
    (5, 10, 6, 'black'), (6, 10, 6, 'black'), (9, 10, 8, 'black'), (10, 10, 8, 'black'),
    # Leather jacket (black)
    (5, 10, 6, 'black'), (6, 10, 6, 'black'), (7, 10, 6, 'black'), (8, 10, 6, 'black'), (9, 10, 6, 'black'), (10, 10, 6, 'black'),
    (5, 11, 6, 'black'), (6, 11, 6, 'black'), (7, 11, 6, 'black'), (8, 11, 6, 'black'), (9, 11, 6, 'black'), (10, 11, 6, 'black'),
    # Band patches
    (6, 11, 6, 'red'), (9, 11, 6, 'red'),
    # Pants
    (6, 12, 6, 'black'), (7, 12, 6, 'black'), (8, 12, 6, 'black'), (9, 12, 6, 'black'),
    (6, 13, 6, 'black'), (7, 13, 6, 'black'), (8, 13, 6, 'black'), (9, 13, 6, 'black'),
    # Boots
    (6, 14, 6, 'black'), (7, 14, 6, 'black'), (8, 14, 6, 'black'), (9, 14, 6, 'black'),
]

# DISCO KING - Fire/Psychic
DISCO_KING_VOXELS = [
    # Head
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Hair (afro, gold)
    (5, 8, 6, 'gold'), (6, 8, 6, 'gold'), (7, 8, 6, 'gold'), (8, 8, 6, 'gold'), (9, 8, 6, 'gold'), (10, 8, 6, 'gold'),
    (5, 9, 6, 'gold'), (6, 9, 6, 'gold'), (9, 9, 8, 'gold'), (10, 9, 8, 'gold'),
    # Suit (flared, colorful)
    (5, 10, 6, 'red'), (6, 10, 6, 'red'), (7, 10, 6, 'red'), (8, 10, 6, 'red'), (9, 10, 6, 'red'), (10, 10, 6, 'red'),
    (5, 11, 6, 'red'), (6, 11, 6, 'red'), (7, 11, 6, 'red'), (8, 11, 6, 'red'), (9, 11, 6, 'red'), (10, 11, 6, 'red'),
    # Platform shoes
    (6, 13, 6, 'white'), (7, 13, 6, 'white'), (8, 13, 6, 'white'), (9, 13, 6, 'white'),
    (6, 14, 6, 'white'), (7, 14, 6, 'white'), (8, 14, 6, 'white'), (9, 14, 6, 'white'),
]

# JOHNNY ELBOWS - Fighting/Dark
JOHNNY_ELBOWS_VOXELS = [
    # Head
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Hair (spiky)
    (6, 8, 6, 'black'), (7, 8, 6, 'black'), (8, 8, 6, 'black'), (9, 8, 6, 'black'),
    # Tank top (black)
    (6, 10, 7, 'black'), (7, 10, 7, 'black'), (8, 10, 7, 'black'), (9, 10, 7, 'black'),
    (6, 11, 7, 'black'), (7, 11, 7, 'black'), (8, 11, 7, 'black'), (9, 11, 7, 'black'),
    # Elbow pads (red)
    (5, 11, 6, 'red'), (10, 11, 8, 'red'),
    # Pants
    (6, 12, 7, 'black'), (7, 12, 7, 'black'), (8, 12, 7, 'black'), (9, 12, 7, 'black'),
    (6, 13, 7, 'black'), (7, 13, 7, 'black'), (8, 13, 7, 'black'), (9, 13, 7, 'black'),
    # Boots
    (6, 14, 7, 'red'), (7, 14, 7, 'red'), (8, 14, 7, 'red'), (9, 14, 7, 'red'),
]

# MEME LORD - Psychic/Dark
MEME_LORD_VOXELS = [
    # Head
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Hair (messy)
    (5, 8, 6, 'black'), (6, 8, 6, 'black'), (7, 8, 6, 'black'), (8, 8, 6, 'black'), (9, 8, 6, 'black'), (10, 8, 6, 'black'),
    # Hoodie (dark purple)
    (5, 10, 6, 'dark_purple'), (6, 10, 6, 'dark_purple'), (7, 10, 6, 'dark_purple'), (8, 10, 6, 'dark_purple'), (9, 10, 6, 'dark_purple'), (10, 10, 6, 'dark_purple'),
    (5, 11, 6, 'dark_purple'), (6, 11, 6, 'dark_purple'), (7, 11, 6, 'dark_purple'), (8, 11, 6, 'dark_purple'), (9, 11, 6, 'dark_purple'), (10, 11, 6, 'dark_purple'),
    # Glasses
    (6, 9, 7, 'blue_core'), (9, 9, 7, 'blue_core'),
    # Pants
    (6, 12, 6, 'grey'), (7, 12, 6, 'grey'), (8, 12, 6, 'grey'), (9, 12, 6, 'grey'),
    (6, 13, 6, 'grey'), (7, 13, 6, 'grey'), (8, 13, 6, 'grey'), (9, 13, 6, 'grey'),
    # Shoes
    (6, 14, 6, 'white'), (7, 14, 6, 'white'), (8, 14, 6, 'white'), (9, 14, 6, 'white'),
]

# BOKEBALL MVP - Flying/Psychic
BOKEBALL_MVP_VOXELS = [
    # Head
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Hair (short)
    (6, 8, 6, 'gold'), (7, 8, 6, 'gold'), (8, 8, 6, 'gold'), (9, 8, 6, 'gold'),
    # Jersey (orange/blue)
    (6, 10, 7, 'orange'), (7, 10, 7, 'orange'), (8, 10, 7, 'orange'), (9, 10, 7, 'orange'),
    (6, 11, 7, 'orange'), (7, 11, 7, 'orange'), (8, 11, 7, 'orange'), (9, 11, 7, 'orange'),
    # Number 23
    (7, 11, 7, 'blue_core'), (8, 11, 7, 'blue_core'),
    # Shorts
    (6, 12, 7, 'blue_core'), (7, 12, 7, 'blue_core'), (8, 12, 7, 'blue_core'), (9, 12, 7, 'blue_core'),
    # Legs
    (6, 13, 7, 'white'), (7, 13, 7, 'white'), (8, 13, 7, 'white'), (9, 13, 7, 'white'),
    # Shoes
    (6, 14, 7, 'orange'), (7, 14, 7, 'orange'), (8, 14, 7, 'orange'), (9, 14, 7, 'orange'),
]

# POINT GUARD - Psychic/Normal
POINT_GUARD_VOXELS = [
    # Head
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Headband
    (6, 8, 7, 'red'), (7, 8, 7, 'red'), (8, 8, 7, 'red'), (9, 8, 7, 'red'),
    # Jersey (white)
    (6, 10, 7, 'white'), (7, 10, 7, 'white'), (8, 10, 7, 'white'), (9, 10, 7, 'white'),
    (6, 11, 7, 'white'), (7, 11, 7, 'white'), (8, 11, 7, 'white'), (9, 11, 7, 'white'),
    # Shorts
    (6, 12, 7, 'blue_core'), (7, 12, 7, 'blue_core'), (8, 12, 7, 'blue_core'), (9, 12, 7, 'blue_core'),
    # Legs
    (6, 13, 7, 'white'), (7, 13, 7, 'white'), (8, 13, 7, 'white'), (9, 13, 7, 'white'),
    # Shoes
    (6, 14, 7, 'red'), (7, 14, 7, 'red'), (8, 14, 7, 'red'), (9, 14, 7, 'red'),
]

# CENTER - Steel/Fighting
CENTER_VOXELS = [
    # Head (large)
    (6, 8, 6, 'white'), (7, 8, 6, 'white'), (8, 8, 6, 'white'), (9, 8, 6, 'white'),
    (6, 9, 6, 'white'), (7, 9, 6, 'white'), (8, 9, 6, 'white'), (9, 9, 6, 'white'),
    # Jersey (grey/steel)
    (5, 10, 6, 'grey'), (6, 10, 6, 'grey'), (7, 10, 6, 'grey'), (8, 10, 6, 'grey'), (9, 10, 6, 'grey'), (10, 10, 6, 'grey'),
    (5, 11, 6, 'grey'), (6, 11, 6, 'grey'), (7, 11, 6, 'grey'), (8, 11, 6, 'grey'), (9, 11, 6, 'grey'), (10, 11, 6, 'grey'),
    # Shorts
    (6, 12, 6, 'grey'), (7, 12, 6, 'grey'), (8, 12, 6, 'grey'), (9, 12, 6, 'grey'),
    # Massive legs
    (6, 13, 6, 'grey'), (7, 13, 6, 'grey'), (8, 13, 6, 'grey'), (9, 13, 6, 'grey'),
    (6, 14, 6, 'grey'), (7, 14, 6, 'grey'), (8, 14, 6, 'grey'), (9, 14, 6, 'grey'),
]

# HYPEBEAST DEALER - Dark/Steel
HYPEBEAST_DEALER_VOXELS = [
    # Head
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Hoodie (black)
    (5, 10, 6, 'black'), (6, 10, 6, 'black'), (7, 10, 6, 'black'), (8, 10, 6, 'black'), (9, 10, 6, 'black'), (10, 10, 6, 'black'),
    (5, 11, 6, 'black'), (6, 11, 6, 'black'), (7, 11, 6, 'black'), (8, 11, 6, 'black'), (9, 11, 6, 'black'), (10, 11, 6, 'black'),
    # Logo (white box logo)
    (7, 11, 6, 'white'), (8, 11, 6, 'white'),
    # Pants (ripped jeans)
    (6, 12, 6, 'blue_core'), (7, 12, 6, 'blue_core'), (8, 12, 6, 'blue_core'), (9, 12, 6, 'blue_core'),
    (6, 13, 6, 'blue_core'), (7, 13, 6, 'blue_core'), (8, 13, 6, 'blue_core'), (9, 13, 6, 'blue_core'),
    # Shoes ( Jordans)
    (6, 14, 6, 'red'), (7, 14, 6, 'red'), (8, 14, 6, 'red'), (9, 14, 6, 'red'),
]

# GRAIL HUNTER - Psychic/Normal
GRAIL_HUNTER_VOXELS = [
    # Head
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Cap (backwards)
    (6, 8, 6, 'blue_core'), (7, 8, 6, 'blue_core'), (8, 8, 6, 'blue_core'), (9, 8, 6, 'blue_core'),
    # Jacket (brown leather)
    (5, 10, 6, 'brown'), (6, 10, 6, 'brown'), (7, 10, 6, 'brown'), (8, 10, 6, 'brown'), (9, 10, 6, 'brown'), (10, 10, 6, 'brown'),
    (5, 11, 6, 'brown'), (6, 11, 6, 'brown'), (7, 11, 6, 'brown'), (8, 11, 6, 'brown'), (9, 11, 6, 'brown'), (10, 11, 6, 'brown'),
    # Pants
    (6, 12, 6, 'grey'), (7, 12, 6, 'grey'), (8, 12, 6, 'grey'), (9, 12, 6, 'grey'),
    (6, 13, 6, 'grey'), (7, 13, 6, 'grey'), (8, 13, 6, 'grey'), (9, 13, 6, 'grey'),
    # Boots
    (6, 14, 6, 'brown'), (7, 14, 6, 'brown'), (8, 14, 6, 'brown'), (9, 14, 6, 'brown'),
]

# MAGA CHAMPION - Normal/Fire
MAGA_CHAMPION_VOXELS = [
    # Head
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Hair (red, white, blue streaks)
    (6, 8, 6, 'red'), (7, 8, 6, 'white'), (8, 8, 6, 'blue_core'), (9, 8, 6, 'red'),
    # Suit (red, white, blue)
    (6, 10, 7, 'red'), (7, 10, 7, 'white'), (8, 10, 7, 'blue_core'), (9, 10, 7, 'red'),
    (6, 11, 7, 'red'), (7, 11, 7, 'white'), (8, 11, 7, 'blue_core'), (9, 11, 7, 'red'),
    (6, 12, 7, 'red'), (7, 12, 7, 'white'), (8, 12, 7, 'blue_core'), (9, 12, 7, 'red'),
    # Tie (red)
    (7, 10, 7, 'red'), (7, 11, 7, 'red'),
    # Pants
    (6, 13, 7, 'blue_core'), (7, 13, 7, 'blue_core'), (8, 13, 7, 'blue_core'), (9, 13, 7, 'blue_core'),
    # Shoes
    (6, 14, 7, 'red'), (7, 14, 7, 'red'), (8, 14, 7, 'red'), (9, 14, 7, 'red'),
]

# PATRIOT - Normal/Steel
PATRIOT_VOXELS = [
    # Head
    (7, 8, 7, 'white'), (8, 8, 7, 'white'),
    (6, 9, 7, 'white'), (7, 9, 7, 'white'), (8, 9, 7, 'white'), (9, 9, 7, 'white'),
    # Hat (flag pattern)
    (6, 8, 6, 'red'), (7, 8, 6, 'white'), (8, 8, 6, 'blue_core'), (9, 8, 6, 'red'),
    # Jacket (military style)
    (5, 10, 6, 'green'), (6, 10, 6, 'green'), (7, 10, 6, 'green'), (8, 10, 6, 'green'), (9, 10, 6, 'green'), (10, 10, 6, 'green'),
    (5, 11, 6, 'green'), (6, 11, 6, 'green'), (7, 11, 6, 'green'), (8, 11, 6, 'green'), (9, 11, 6, 'green'), (10, 11, 6, 'green'),
    # Badge
    (7, 11, 6, 'gold'), (8, 11, 6, 'gold'),
    # Pants
    (6, 12, 6, 'green'), (7, 12, 6, 'green'), (8, 12, 6, 'green'), (9, 12, 6, 'green'),
    (6, 13, 6, 'green'), (7, 13, 6, 'green'), (8, 13, 6, 'green'), (9, 13, 6, 'green'),
    # Boots
    (6, 14, 6, 'brown'), (7, 14, 6, 'brown'), (8, 14, 6, 'brown'), (9, 14, 6, 'brown'),
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
    'HEIDI ANDERSON CHRIST': HEIDI_VOXELS,
    'TRUMP': TRUMP_VOXELS,
    'BARRON': BARRON_VOXELS,
    'SAMBA QUEEN': SAMBA_QUEEN_VOXELS,
    'CAPOEIRA MASTER': CAPOEIRA_MASTER_VOXELS,
    'SUMO CHAMPION': SUMO_CHAMPION_VOXELS,
    'KUNG FU MASTER': KUNG_FU_MASTER_VOXELS,
    'BALLET DIVA': BALLET_DIVA_VOXELS,
    'HIP HOP LEGEND': HIP_HOP_LEGEND_VOXELS,
    'METALHEAD': METALHEAD_VOXELS,
    'DISCO KING': DISCO_KING_VOXELS,
    'JOHNNY ELBOWS': JOHNNY_ELBOWS_VOXELS,
    'MEME LORD': MEME_LORD_VOXELS,
    'BOKEBALL MVP': BOKEBALL_MVP_VOXELS,
    'POINT GUARD': POINT_GUARD_VOXELS,
    'CENTER': CENTER_VOXELS,
    'HYPEBEAST DEALER': HYPEBEAST_DEALER_VOXELS,
    'GRAIL HUNTER': GRAIL_HUNTER_VOXELS,
    'MAGA CHAMPION': MAGA_CHAMPION_VOXELS,
    'PATRIOT': PATRIOT_VOXELS,
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