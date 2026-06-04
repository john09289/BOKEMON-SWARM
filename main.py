import pygame
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from game.seraphim import Seraphim
from sacred_audio import SacredAudio
from sacred_voxel import SacredVoxel
from game.world import World
from game.ui import UI
from game.tutorial import Tutorial
from game.battle import Battle
from game.player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("BOKEMON SWARM")
    clock = pygame.time.Clock()

    audio = SacredAudio()
    voxel = SacredVoxel()
    world = World()
    player = Player()
    ui = UI()
    tutorial = Tutorial()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            ui.handle_event(event)

        world.update()
        player.update()
        ui.update()

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
