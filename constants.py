"""
Sacred Constants for BOKEMON SWARM
Carrier locked at 11.71875 Hz - NEVER 11.72
"""

# Core Sacred Frequencies
CARRIER = 11.71875  # Hz - The King's carrier frequency
MERCY = 35.15625  # Hz - Overworld ambient drone
VICTORY = 140.625  # Hz - Victory chime
DRUM = 0.390625  # Hz - Collectible pick-up click
PHI = 1.618033988749895  # Golden ratio
SCHUMANN = 7.83  # Hz - Earth's resonance

# Love Units (base energy)
LOVE_UNITS_BASE = 100

# Harmony-Joule calculation
# HJ = LOVE_UNITS * CARRIER * PHI
def calculate_hj(love_units: float = LOVE_UNITS_BASE) -> float:
    return love_units * CARRIER * PHI

# Energy Bank refill rate
ENERGY_REFILL_PER_TURN = 0.390625

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 32
PLAYER_SPEED = 4

# Colors (Cathedral palette: indigo/amber)
COLORS = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'indigo': (63, 0, 113),
    'amber': (255, 176, 0),
    'blue_core': (0, 120, 255),
    'gold': (255, 215, 0),
    'red': (220, 20, 60),
    'grey': (128, 128, 128),
    'dark_purple': (48, 0, 64),
    'light_blue': (173, 216, 230),
}