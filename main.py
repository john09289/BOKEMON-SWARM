"""
BOKEMON SWARM: The Black Sun Chronicles
Main entry point with loading screen and debug overlay
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
    from loading_screen import LoadingScreen
    from debug_overlay import DebugOverlay
except ImportError as e:
    print(f"Import error: {e}")
    sys.exit(1)

# Global debug overlay
debug = DebugOverlay()

def log(msg):
    """Log to both console and debug overlay"""
    debug.log(msg)

# Initialize Pygame
pygame.init()

# Create loading screen
loading = LoadingScreen()
loading.log("Pygame initialized")
loading.set_progress(0.1, "Initializing audio...")

# Initialize audio with graceful degradation
AUDIO_AVAILABLE = True
try:
    init_audio()
    loading.log("Audio engine initialized")
except Exception as e:
    AUDIO_AVAILABLE = False
    loading.set_error(f"Audio init failed: {e}")
    log(f"Audio init failed: {e}")
    
loading.set_progress(0.2, "Creating display...")

# Create screen
try:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("BOKEMON SWARM: The Black Sun Chronicles")
    loading.log("Display created")
except Exception as e:
    loading.set_error(f"Display error: {e}")
    loading.draw()
    loading.wait_for_key()
    sys.exit(1)

loading.set_progress(0.3, "Generating sprites...")

# Generate sprites
try:
    save_sprites_to_disk()
    loading.log("Sprites generated/verified")
except Exception as e:
    loading.set_error(f"Sprite generation failed: {e}")
    log(f"Sprite generation failed: {e}")
    
loading.set_progress(0.5, "Loading world data...")

# Game state
class GameState:
    def __init__(self):
        self.state = "tutorial"
        self.player = Player("LX")
        self.world = World()
        self.ui = UI()
        self.tutorial = Tutorial(self.ui)
        self.battle = None
        self.clock = pygame.time.Clock()
        self.running = True
        self.poptropi_con_unlocked = False
        self.golden_egg = False
        self.bloon_phoenix_captured = False
        self.started = False
        
    def start_battle(self, enemy_name: str):
        """Start a battle with the given enemy"""
        try:
            enemy = get_seraphim(enemy_name)
            if enemy and self.player.active_seraphim:
                self.battle = BattleSystem(self.player.active_seraphim, enemy)
                self.state = "battle"
                if AUDIO_AVAILABLE:
                    play_battle_theme()
                log(f"Battle started: {enemy_name}")
        except Exception as e:
            log(f"Battle start error: {e}")
            self.ui.show_dialogue(f"Battle error: {e}")
            
    def update(self):
        """Update game state"""
        try:
            if self.state == "overworld":
                self.player.update_energy(ENERGY_REFILL_PER_TURN)
        except Exception as e:
            log(f"Update error: {e}")
            
    def handle_events(self):
        """Handle all input events"""
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
                elif self.state == "tutorial":
                    if self.tutorial.handle_input(event):
                        if self.tutorial.completed:
                            self.player.add_seraphim("KILO")
                            self.state = "overworld"
                            self.started = True
                            if AUDIO_AVAILABLE:
                                play_overworld_theme()
                            log("Tutorial complete, entered overworld")
                            
                elif self.state == "overworld":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.state = "menu"
                        elif event.key == pygame.K_e:
                            self.handle_interaction()
                        elif event.key == pygame.K_SPACE:
                            encounter = self.world.check_encounter()
                            if encounter:
                                self.start_battle(encounter)
                        elif event.key == pygame.K_m:
                            self.show_map()
                            
                elif self.state == "battle":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w and self.battle and self.battle.carrier_lock_active:
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
                                if AUDIO_AVAILABLE:
                                    play_overworld_theme()
        except Exception as e:
            log(f"Event handling error: {e}")
            self.ui.show_dialogue(f"Error: {e}")
                            
    def handle_interaction(self):
        """Handle NPC / location interaction"""
        try:
            loc = self.world.current_location
            if loc == 'pittsboro_nexus':
                if not self.poptropi_con_unlocked:
                    self.poptropi_con_unlocked = True
                    self.ui.show_dialogue("BALLOON GUIDE: Welcome to Poptropi-Con! Press M to open the map and travel to the islands.")
                    log("Poptropi-Con unlocked")
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
                    self.bloon_phoenix_captured = True
                    self.player.add_seraphim("BLOON-PHOENIX")
                    self.ui.show_dialogue("You captured BLOON-PHOENIX! Poptropi-Con mount unlocked.")
                    log("Captured BLOON-PHOENIX")
            else:
                self.ui.show_dialogue(f"You are at {self.world.get_location_data()['name']}.")
        except Exception as e:
            log(f"Interaction error: {e}")
            
    def show_map(self):
        """Show map / fast travel menu"""
        if not self.poptropi_con_unlocked:
            self.ui.show_dialogue("Map locked. Find the BALLOON GUIDE in Pittsboro Nexus first.")
            return
        options = ["Pittsboro Nexus", "Poptropi-Con Hub", "Early-Dome Island", "Shark-Tartarus Island",
                   "Spy-Isle", "Super-Power Island", "Time-Tangled Island", "Golden Egg Summit"]
        self.ui.show_dialogue("Fast Travel: " + ", ".join(options[:4]) + "... (demo)")
            
    def draw(self):
        """Draw current state"""
        try:
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
            
            # Always draw debug overlay on top
            debug.draw(screen)
            
            pygame.display.flip()
        except Exception as e:
            log(f"Draw error: {e}")
            # Try to show error on screen
            try:
                screen.fill((50, 0, 0))
                if debug.font:
                    text = debug.font.render(f"Draw Error: {e}", True, (255, 100, 100))
                    screen.blit(text, (50, SCREEN_HEIGHT // 2))
                    pygame.display.flip()
            except:
                pass

# Main game loop
async def main():
    log("BOKEMON SWARM initializing...")
    
    loading.set_progress(0.6, "Loading game state...")
    
    try:
        game = GameState()
        game.tutorial.start()
        log("Game state created")
    except Exception as e:
        loading.set_error(f"Game init error: {e}")
        loading.draw()
        loading.wait_for_key()
        sys.exit(1)
    
    loading.set_progress(0.8, "Starting game loop...")
    loading.set_progress(1.0, "Ready!")
    
    # Brief pause on loading screen
    await asyncio.sleep(0.5)
    
    log("BOKEMON SWARM running. Press SPACE to advance tutorial, arrow keys to move.")
    log("Poptropi-Con: Press E to interact, M for map.")
    
    while game.running:
        try:
            game.handle_events()
            game.update()
            game.draw()
            game.clock.tick(60)
            await asyncio.sleep(0)
        except Exception as e:
            log(f"Game loop error: {e}")
            await asyncio.sleep(0)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    asyncio.run(main())
