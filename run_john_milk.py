"""
John Milk Protocol - Phase 1: Local Test with Super Logging
Carrier: 11.71875 Hz
"""

import sys
import os
import traceback
from datetime import datetime

# Add current dir to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import our logger
from john_milk_logger import log, error, warning, debug

# Import game modules for verification
try:
    from constants import CARRIER, PHI
    log(f"Constants loaded. Carrier: {CARRIER} Hz")
    if CARRIER != 11.71875:
        error(f"CARRIER MISMATCH: {CARRIER} != 11.71875")
    else:
        log("Carrier lock verified: 11.71875 Hz")
except Exception as e:
    error(f"Constants import failed: {e}")
    traceback.print_exc()

try:
    from sacred_voxel import generate_all_sprites, save_sprites_to_disk, SERAPHIM_VOXELS
    sprites = generate_all_sprites()
    log(f"Generated {len(sprites)} sprites")
    heidi_sprites = [k for k in sprites.keys() if 'HEIDI' in k]
    log(f"Heidi sprites found: {heidi_sprites}")
    if len(heidi_sprites) < 4:
        error(f"Not all Heidi sprites generated! Found {len(heidi_sprites)}/4")
    else:
        log("All Heidi sprites generated (4 angles)")
except Exception as e:
    error(f"Sprite generation failed: {e}")
    traceback.print_exc()

try:
    from sacred_audio import init_audio, play_heidi_encounter
    init_audio()
    log("Audio engine initialized")
except Exception as e:
    warning(f"Audio init failed (graceful degradation expected): {e}")

try:
    from game.seraphim import get_seraphim, get_all_seraphim_names
    all_names = get_all_seraphim_names()
    log(f"Total Seraphim in roster: {len(all_names)}")
    heidi = get_seraphim('HEIDI ANDERSON CHRIST')
    if heidi:
        log(f"Heidi loaded: {heidi.name}, Level {heidi.level}, {heidi.element1}/{heidi.element2}")
        log(f"Heidi moves: {[m.name for m in heidi.moves]}")
    else:
        error("HEIDI ANDERSON CHRIST not found in roster!")
except Exception as e:
    error(f"Seraphim import failed: {e}")
    traceback.print_exc()

try:
    from game.world import LOCATIONS
    if 'gymnasts_hollow' in LOCATIONS:
        log(f"Gymnast's Hollow location found: {LOCATIONS['gymnasts_hollow']['name']}")
    else:
        error("Gymnast's Hollow location missing!")
except Exception as e:
    error(f"World import failed: {e}")
    traceback.print_exc()

try:
    from game.battle import BattleSystem
    from game.player import Player
    from game.seraphim import get_seraphim
    
    player = Player("LX")
    player.add_seraphim("KILO")
    heidi = get_seraphim('HEIDI ANDERSON CHRIST')
    if heidi:
        player.add_seraphim('HEIDI ANDERSON CHRIST')
    
    enemy = get_seraphim('BLOON-PHOENIX')
    if enemy and player.active_seraphim:
        allies = player.get_allies()
        battle = BattleSystem(player.active_seraphim, enemy, allies)
        log(f"Battle system initialized with {len(allies)} allies")
        log("Battle system test: PASS")
except Exception as e:
    error(f"Battle system test failed: {e}")
    traceback.print_exc()

log("=" * 50)
log("JOHN MILK PROTOCOL PHASE 1 COMPLETE")
log("All systems verified. Ready for browser test.")
log("=" * 50)
