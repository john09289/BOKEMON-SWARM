"""
Generate all BOKEMON SWARM sprites
Including procedurally generated Poptropica-Complete Seraphim
"""

import pygame
import json
import os
import numpy as np
from sacred_voxel import generate_all_sprites, save_sprites_to_disk, SERAPHIM_VOXELS, COLORS, render_voxel_model

MANIFEST_PATH = "data/poptropica_islands.json"

def generate_placeholder_voxels(name, color_name='white'):
    """Generate a simple placeholder voxel model for a new Seraphim"""
    base_color = COLORS.get(color_name, COLORS['white'])
    # Simple 8x8x8 cube with some variation
    voxels = []
    for y in range(8, 14):
        for x in range(6, 10):
            for z in range(6, 10):
                if (x, y, z) in [(7, 8, 7), (8, 8, 7), (7, 9, 7), (8, 9, 7)]:
                    voxels.append((x, y, z, 'white'))  # head
                elif y >= 10 and y <= 12:
                    voxels.append((x, y, z, base_color))  # body
                else:
                    voxels.append((x, y, z, base_color))
    return voxels

def load_manifest_seraphim():
    """Load Seraphim from Poptropica manifest and add to voxel registry"""
    if not os.path.exists(MANIFEST_PATH):
        return []
    
    with open(MANIFEST_PATH, 'r') as f:
        manifest = json.load(f)
    
    new_seraphim = []
    for island in manifest['islands']:
        name = island['seraphim_name']
        if name not in SERAPHIM_VOXELS:
            # Generate placeholder voxels based on type
            type_color = {
                'Water': 'blue_core',
                'Fire': 'red',
                'Dark': 'dark_purple',
                'Psychic': 'light_blue',
                'Steel': 'grey',
                'Electric': 'gold',
                'Grass': 'green',
                'Ghost': 'white',
                'Fighting': 'amber',
                'Dragon': 'indigo',
                'Flying': 'light_blue',
                'Fairy': 'pink',
                'Ground': 'brown',
                'Ice': 'light_blue',
                'Poison': 'green',
                'Normal': 'white',
                'Light': 'gold'
            }.get(island['seraphim_type'][0], 'white')
            
            voxels = generate_placeholder_voxels(name, type_color)
            SERAPHIM_VOXELS[name] = voxels
            new_seraphim.append(name)
    
    return new_seraphim

def main():
    pygame.init()
    
    # Load manifest and add new Seraphim
    new_names = load_manifest_seraphim()
    if new_names:
        print(f"Added {len(new_names)} new Seraphim from manifest: {new_names}")
    
    count = save_sprites_to_disk()
    print(f"Generated {count} sprites for all Seraphim")
    pygame.quit()

if __name__ == "__main__":
    main()
