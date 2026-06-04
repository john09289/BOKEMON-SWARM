"""
Poptropica-Complete: Procedural Island Generator
Carrier: 11.71875 Hz
Generates maps, quests, encounters, and boss battles from a manifest.
"""

import json
import os
import random
import numpy as np
from constants import COLORS

MANIFEST_PATH = "data/poptropica_islands.json"
OUTPUT_DIR = "data/islands"

def load_manifest():
    """Load the island manifest"""
    with open(MANIFEST_PATH, 'r') as f:
        return json.load(f)['islands']

def hex_to_rgb(hex_str):
    """Convert hex color to RGB tuple"""
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def generate_tile_map(island, size=30):
    """Generate a 2D tile map for an island based on its theme and colors"""
    colors = [hex_to_rgb(c) for c in island['color_scheme']]
    tile_map = np.zeros((size, size, 3), dtype=int)
    
    # Fill with base color
    base_color = colors[0] if colors else (100, 100, 100)
    tile_map[:] = base_color
    
    # Add paths (lighter color)
    path_color = colors[1] if len(colors) > 1 else (150, 150, 150)
    for i in range(5, size-5):
        tile_map[i][size//2] = path_color
        tile_map[size//2][i] = path_color
    
    # Add rooms (darker color)
    room_color = colors[2] if len(colors) > 2 else (80, 80, 80)
    for x in range(8, size-8, 6):
        for y in range(8, size-8, 6):
            if random.random() > 0.3:
                tile_map[y:y+4, x:x+4] = room_color
    
    # Add special tiles
    # Boss tile (red marker)
    tile_map[5][size//2] = (255, 0, 0)
    # Seraphim encounter tile (gold marker)
    tile_map[size-6][size//2] = (255, 215, 0)
    # Key item tile (blue marker)
    tile_map[size//2][5] = (0, 0, 255)
    
    return tile_map.tolist()

def generate_npc_dialogues(island):
    """Generate generic NPC dialogues for the island"""
    dialogues = []
    themes = island['theme']
    boss = island['boss_name']
    
    dialogues.append({
        "npc": "Guide",
        "text": f"Welcome to {island['parody_name']}! Beware of {boss}..."
    })
    dialogues.append({
        "npc": "Local",
        "text": f"I heard {boss} guards the {island['key_item']}."
    })
    dialogues.append({
        "npc": "Mysterious Stranger",
        "text": "The Carrier frequency is 11.71875 Hz. Trust in the King."
    })
    return dialogues

def generate_puzzle(island):
    """Generate a simple puzzle function for the key item"""
    key_item = island['key_item']
    theme = island['theme'][0] if island['theme'] else "mystery"
    
    def puzzle():
        """Simple riddle puzzle based on island theme"""
        riddles = {
            "underwater": "What has many teeth but cannot bite? (A comb/shark - answer: shark)",
            "space": "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I? (A map)",
            "pirate": "What has a head and a tail but no body? (A coin)",
            "carnival": "What gets broken without being held? (A promise)",
            "default": "What is 11.71875 Hz? (The King's carrier frequency)"
        }
        riddle = riddles.get(theme, riddles["default"])
        print(f"PUZZLE: {riddle}")
        answer = input("Your answer: ").strip().lower()
        return True  # Simplified: always pass for now
    
    return puzzle

def generate_boss_moveset(boss_type):
    """Generate a moveset based on boss type"""
    type_moves = {
        "Water": ["Tidal Wave", "Aqua Jet", "Waterfall"],
        "Fire": ["Inferno", "Fire Blast", "Dragon Rage"],
        "Dark": ["Dark Pulse", "Nightmare", "Shadow Ball"],
        "Psychic": ["Psychic", "Psyshock", "Future Sight"],
        "Steel": ["Iron Tail", "Flash Cannon", "Meteor Mash"],
        "Electric": ["Thunder", "Volt Tackle", "Discharge"],
        "Grass": ["Solar Beam", "Leaf Storm", "Energy Ball"],
        "Ghost": ["Shadow Ball", "Curse", "Phantom Force"],
        "Fighting": ["Close Combat", "Brick Break", "Aura Sphere"],
        "Dragon": ["Dragon Claw", "Outrage", "Dragon Pulse"],
        "Flying": ["Hurricane", "Brave Bird", "Air Slash"],
        "Fairy": ["Moonblast", "Dazzling Gleam", "Play Rough"],
        "Ground": ["Earthquake", "Stone Edge", "Bulldoze"],
        "Ice": ["Blizzard", "Ice Beam", "Avalanche"],
        "Poison": ["Sludge Bomb", "Toxic", "Acid Spray"],
        "Normal": ["Hyper Voice", "Double-Edge", "Body Slam"],
        "Light": ["Judgment", "Flash", "Luster Purge"]
    }
    
    moves = []
    for t in boss_type:
        moves.extend(type_moves.get(t, ["Struggle"])[:2])
    return moves[:4]  # Max 4 moves

def generate_island_data(island):
    """Generate complete data package for an island"""
    tile_map = generate_tile_map(island)
    dialogues = generate_npc_dialogues(island)
    puzzle = generate_puzzle(island)
    boss_moves = generate_boss_moveset(island['boss_type'])
    
    return {
        "id": island['id'],
        "name": island['parody_name'],
        "tile_map": tile_map,
        "size": len(tile_map),
        "npcs": dialogues,
        "puzzle_type": island['theme'][0] if island['theme'] else "mystery",
        "puzzle_hint": f"Riddle about {island['theme'][0] if island['theme'] else 'mystery'}",
        "boss": {
            "name": island['boss_name'],
            "type": island['boss_type'],
            "moves": boss_moves,
            "key_item": island['key_item']
        },
        "seraphim": {
            "name": island['seraphim_name'],
            "type": island['seraphim_type']
        },
        "music_style": island['music_style'],
        "unlocks": island.get('unlocks', [])
    }

def generate_all_islands():
    """Generate data for all islands in the manifest"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    manifest = load_manifest()
    
    generated = []
    for island in manifest:
        data = generate_island_data(island)
        output_path = os.path.join(OUTPUT_DIR, f"{island['id']}.json")
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
        generated.append(island['id'])
        print(f"Generated: {island['parody_name']}")
    
    return generated

if __name__ == "__main__":
    islands = generate_all_islands()
    print(f"\nTotal islands generated: {len(islands)}")
    print("Islands:", islands)
