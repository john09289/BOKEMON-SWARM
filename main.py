"""
BOKEMON SWARM: The Black Sun Chronicles
Main entry point
Carrier: 11.71875 Hz. The King wins. 𐤕
"""

import pygame
import sys
import asyncio

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
        self.poptropi_con_unlocked = False
        self.golden_egg = False
        self.bloon_phoenix_captured = False
        
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
                    elif event.key == pygame.K_e:
                        # Interact with NPC / enter location
                        self.handle_interaction()
                    elif event.key == pygame.K_SPACE:
                        encounter = self.world.check_encounter()
                        if encounter:
                            self.start_battle(encounter)
                    elif event.key == pygame.K_m:
                        # Map / fast travel
                        self.show_map()
                            
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
                            
    def handle_interaction(self):
        """Handle NPC / location interaction"""
        loc = self.world.current_location
        if loc == 'pittsboro_nexus':
            if not self.poptropi_con_unlocked:
                self.poptropi_con_unlocked = True
                self.ui.show_dialogue("BALLOON GUIDE: Welcome to Poptropi-Con! Press M to open the map and travel to the islands.")
            else:
                self.ui.show_dialogue("BALLOON GUIDE: Choose an island from your map (M key).")
        elif loc == 'early_dome_island':
            if not self.golden_egg:
                self.ui.show_dialogue("You sense the Purple Watcher's glitch nearby. Defeat it to claim the Golden Egg!")
            else:
                self.ui.show_dialogue("The Golden Egg glows in your pack. The final island awaits.")
        elif loc == 'golden_egg_summit':
            if self.golden_egg and not self.bloon_phoenix_captured:
                self.ui.show_dialogue("BLOON-PHOENIX: Free me with the Conditional Prayer... (simulated rhythm mini-game)")
                # Simulate rhythm mini-game success
                self.bloon_phoenix_captured = True
                self.player.add_seraphim("BLOON-PHOENIX")
                self.ui.show_dialogue("You captured BLOON-PHOENIX! Poptropi-Con mount unlocked.")
        else:
            self.ui.show_dialogue(f"You are at {self.world.get_location_data()['name']}.")
            
    def show_map(self):
        """Show map / fast travel menu"""
        if not self.poptropi_con_unlocked:
            self.ui.show_dialogue("Map locked. Find the BALLOON GUIDE in Pittsboro Nexus first.")
            return
        options = ["Pittsboro Nexus", "Poptropi-Con Hub", "Early-Dome Island", "Shark-Tartarus Island",
                   "Spy-Isle", "Super-Power Island", "Time-Tangled Island", "Golden Egg Summit"]
        self.ui.show_dialogue("Fast Travel: " + ", ".join(options[:4]) + "... (demo)")
        # In full version, this would be a selectable menu
            
    def draw(self):
        """Draw current state"""
        screen.fill(COLORS['black'])
        
        if self.state == "tutorial":
            self.tutorial.draw(screen)
            
        elif self.state == "overworld":
            self.world.draw(screen)
            self.player.draw(screen)
            self.ui.draw_hud(screen, self.player, self.player.active_seraphim)
            if self.ui.dialogue_active:
                self.ui.draw_dialogue(screen)
            
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
async def main():
    print("BOKEMON SWARM initializing...")
    game = GameState()
    game.tutorial.start()
    
    try:
        save_sprites_to_disk()
    except Exception as e:
        print(f"Sprite generation note: {e}")
    
    print("BOKEMON SWARM running. Press SPACE to advance tutorial, arrow keys to move.")
    print("Poptropi-Con: Press E to interact, M for map.")
    
    while game.running:
        game.handle_events()
        game.update()
        game.draw()
        game.clock.tick(60)
        await asyncio.sleep(0)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    asyncio.run(main())