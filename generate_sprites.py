"""
Generate all BOKEMON SWARM sprites
"""

import pygame
from sacred_voxel import generate_all_sprites, save_sprites_to_disk

def main():
    pygame.init()
    count = save_sprites_to_disk()
    print(f"Generated {count} sprites for all Seraphim")
    pygame.quit()

if __name__ == "__main__":
    main()