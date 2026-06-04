import pygame
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CARRIER, COLORS
from sacred_audio import play_overworld_theme, play_menu_select
from sacred_voxel import generate_all_sprites
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

    # Start audio (non-blocking)
    try:
        play_overworld_theme()
    except Exception as e:
        print(f"Audio init failed: {e}")

    # Font for debug/status text
    try:
        font = pygame.font.SysFont('monospace', 20)
        large_font = pygame.font.SysFont('monospace', 32)
    except:
        font = None
        large_font = None

    running = True
    frame_count = 0
    status_message = "BOKEMON SWARM - Press SPACE to start tutorial, ESC to quit"
    error_message = None

    while running:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_SPACE:
                        play_menu_select()
                        if not tutorial.completed:
                            tutorial.advance()
                        status_message = "Tutorial advanced..."

            # Update
            world.update()
            player.update()
            ui.update()
            tutorial.update()

            # Draw
            screen.fill(COLORS['black'])
            world.draw(screen)
            player.draw(screen)
            ui.draw(screen)
            tutorial.draw(screen)

            # Draw status/debug overlay
            if font:
                status_text = font.render(status_message, True, COLORS['white'])
                screen.blit(status_text, (10, SCREEN_HEIGHT - 30))
                
                if error_message:
                    err_text = font.render(f"ERROR: {error_message}", True, (255, 0, 0))
                    screen.blit(err_text, (10, SCREEN_HEIGHT - 60))

                # Frame counter
                frame_text = font.render(f"Frame: {frame_count} | Carrier: {CARRIER} Hz", True, COLORS['amber'])
                screen.blit(frame_text, (10, 10))

            pygame.display.flip()
            clock.tick(60)
            frame_count += 1

            # Log every 60 frames
            if frame_count % 60 == 0:
                print(f"Frame {frame_count}, player at ({player.x}, {player.y}), FPS={clock.get_fps():.1f}")

        except Exception as e:
            error_message = str(e)
            print(f"Game loop error: {e}")
            # Try to draw error on screen
            try:
                screen.fill(COLORS['black'])
                if font:
                    err_text = font.render(f"ERROR: {error_message}", True, (255, 0, 0))
                    screen.blit(err_text, (50, SCREEN_HEIGHT // 2))
                    hint = font.render("Press ESC to quit", True, COLORS['white'])
                    screen.blit(hint, (50, SCREEN_HEIGHT // 2 + 30))
                pygame.display.flip()
            except:
                pass
            # Wait for quit
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        waiting = False
                        running = False
                clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
