import pygame
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CARRIER
from sacred_audio import play_overworld_theme, play_menu_select, play_carrier_lock_success
from sacred_voxel import generate_all_sprites, SERAPHIM_VOXELS
from game.world import World
from game.player import Player
from game.ui import UI
from game.tutorial import Tutorial

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("BOKEMON SWARM")
    clock = pygame.time.Clock()

    # Generate sprites
    sprites = generate_all_sprites()
    print(f"Generated {len(sprites)} sprites")

    # Initialize systems
    world = World()
    player = Player("LX")
    ui = UI()
    tutorial = Tutorial(ui)

    # Start audio
    play_overworld_theme()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    play_menu_select()

        world.update()
        player.update()
        ui.update()
        tutorial.update()

        screen.fill((0, 0, 0))
        world.draw(screen)
        player.draw(screen)
        ui.draw(screen)
        tutorial.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
