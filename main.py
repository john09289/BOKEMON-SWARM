"""
BOKEMON SWARM: The Black Sun Chronicles
Main entry point
"""

import pygame
import sys

try:
    from constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLORS, calculate_hj, ENERGY_REFILL_PER_TURN
    from sacred_audio import init_audio, play_overworld_theme, play_battle_theme, play_victory_jingle, play_menu_select
    from sacred_voxel import generate_sprite, save_sprites_to_disk
    from game.player import Player
    from game.world import World
    from game.battle import BattleSystem
    from game.ui import UI
    from game.tutorial import Tutorial
    from game.seraphim import get_seraphim
except ImportError as e:
    print(f"Import error: {e}")
    sys.exit(1)

# Initialize Pygame
try:
    pygame.init()
    init_audio()
except Exception as e:
    print(f"Pygame init error: {e}")
    sys.exit(1)

# Create screen
try:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("BOKEMON SWARM: The Black Sun Chronicles")
except Exception as e:
    print(f"Display error: {e}")
    print("No video device found. Try running in a different environment.")
    sys.exit(1)

# Game state
class GameState:
    def __init__(self):
        self.state = "tutorial"
        self.player = Player("LX")
        self.world = World()
        self.ui = UI()
        self.tutorial = Tutorial(self.ui)
        self.battle: BattleSystem = None
        self.clock = pygame.time.Clock()
        self.running = True
        
    def start_battle(self, enemy_name: str):
        """Start a battle with the given enemy"""
        enemy = get_seraphim(enemy_name)
        if enemy and self.player.active_seraphim:
            self.battle = BattleSystem(self.player.active_seraphim, enemy)
            self.state = "battle"
            play_battle_theme()
            
    def update(self):
        """Update game state"""
        if self.state == "overworld":
            self.player.update_energy(ENERGY_REFILL_PER_TURN)
            
    def handle_events(self):
        """Handle all input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            elif self.state == "tutorial":
                if self.tutorial.handle_input(event):
                    if self.tutorial.completed:
                        self.player.add_seraphim("KILO")
                        self.state = "overworld"
                        play_overworld_theme()
                        
            elif self.state == "overworld":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = "menu"
                    elif event.key == pygame.K_SPACE:
                        encounter = self.world.check_encounter()
                        if encounter:
                            self.start_battle(encounter)
                            
            elif self.state == "battle":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and self.battle.carrier_lock_active:
                        self.battle.carrier_lock_success()
                    elif event.key == pygame.K_UP:
                        self.ui.navigate_menu(-1)
                    elif event.key == pygame.K_DOWN:
                        self.ui.navigate_menu(1)
                    elif event.key == pygame.K_RETURN:
                        selected = self.ui.get_selected_menu()
                        if selected == "Attack" and self.player.active_seraphim:
                            move = self.player.active_seraphim.moves[0]
                            if self.player.can_afford_move(move.hj_cost):
                                self.player.update_energy(-move.hj_cost)
                                self.battle.player_attack(move)
                        elif selected == "Run":
                            self.state = "overworld"
                            play_overworld_theme()
                            
    def draw(self):
        """Draw current state"""
        screen.fill(COLORS['black'])
        
        if self.state == "tutorial":
            self.tutorial.draw(screen)
            
        elif self.state == "overworld":
            self.world.draw(screen)
            self.player.draw(screen)
            self.ui.draw_hud(screen, self.player, self.player.active_seraphim)
            
        elif self.state == "battle":
            if self.battle:
                self.battle.draw(screen)
                self.ui.draw_menu(screen)
                
        elif self.state == "menu":
            self.ui.draw_hud(screen, self.player, self.player.active_seraphim)
            self.ui.show_dialogue("PAUSED - ESC to resume")
            self.ui.draw_dialogue(screen)
            
        pygame.display.flip()

# Main game loop
def main():
    print("BOKEMON SWARM initializing...")
    game = GameState()
    game.tutorial.start()
    
    try:
        save_sprites_to_disk()
    except Exception as e:
        print(f"Sprite generation note: {e}")
    
    print("BOKEMON SWARM running. Press SPACE to advance tutorial, arrow keys to move.")
    
    while game.running:
        game.handle_events()
        game.update()
        game.draw()
        game.clock.tick(60)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()