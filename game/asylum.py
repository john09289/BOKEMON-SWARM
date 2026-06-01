"""
Asylum of Temptation & War - New area for BOKEMON SWARM
Contains NPCs, quests, and the Ants vs Zombies mini-game
"""

import pygame
from typing import List, Optional
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import CARRIER, PHI, MERCY_DRONE, VICTORY_CHIME
from game.seraphim import get_seraphim

# Asylum map layout (simple grid)
ASYLUM_MAP = [
    "####################",
    "#..................#",
    "#..L##M##O##S##Z..#",
    "#..#.............#..#",
    "#..#..#######..#..#",
    "#..#..#.....#..#..#",
    "#..#..#..@..#..#..#",
    "#..#..#######..#..#",
    "#..#.............#..#",
    "#..##K##B##R##D..#..#",
    "#..................#",
    "####################",
]

# Area definitions
AREAS = {
    'asylum_entrance': {'x': 10, 'y': 1, 'name': 'Asylum Entrance'},
    'lunara_chamber': {'x': 2, 'y': 2, 'name': 'Lunara\'s Chamber'},
    'mirroraz_room': {'x': 6, 'y': 2, 'name': 'Mirroraz Room'},
    'owen_woz_cave': {'x': 10, 'y': 2, 'name': 'Owen Woz Cave'},
    'sgt_krav_dojo': {'x': 14, 'y': 2, 'name': 'Sgt Krav Dojo'},
    'ant_queen_nest': {'x': 2, 'y': 9, 'name': 'Ant Queen Nest'},
    'zombie_lord_tomb': {'x': 6, 'y': 9, 'name': 'Zombie Lord Tomb'},
    'breckie_pool': {'x': 10, 'y': 9, 'name': 'Breckie\'s Pool'},
    'meg_campfire': {'x': 14, 'y': 9, 'name': 'Meg\'s Campfire'},
    'riley_fountain': {'x': 18, 'y': 9, 'name': 'Riley\'s Fountain'},
    'silky_j_lounge': {'x': 22, 'y': 9, 'name': 'Silky J Lounge'},
}

# NPC dialogue
NPC_DIALOGUE = {
    'LUNARA': [
        "Welcome to my chamber of manic fire...",
        "I swing between manic waves and depressive fog.",
        "Only those who can stabilize my chaos may pass.",
        "Use the move 'Stabilize' to calm my rage!"
    ],
    'MIRRORAZ': [
        "Mirror, mirror on the wall...",
        "Who is the fairest of them all?",
        "My vanity drains the beauty from others.",
        "Beware my selfie curse - it traps the soul!"
    ],
    'OWEN WOZ': [
        "Wow! Just wow! Did you know that wow wisdom comes from the King?",
        "I harness lightning like my cousin McQueen.",
        "My nose is legendary - nose crunch!"
    ],
    'SGT KRAV': [
        "In the Army of the Lord, we fight with honor.",
        "My krav strike has priority - it counters first!",
        "The fabulous uppercut will knock you into next week.",
        "Glitter grenades for the glory of the King!"
    ],
    'ANT QUEEN': [
        "The ants march in formation, loyal to the hive.",
        "We tunnel underground, avoiding detection.",
        "Royal jelly heals all who serve the Queen.",
        "Join the swarm or be consumed by it!"
    ],
    'ZOMBIE LORD': [
        "The dead shall rise and serve the King.",
        "My undead bite drains the life force.",
        "Plague clouds spread the infection of truth.",
        "Even in death, we reanimate for the Kingdom."
    ],
    'BRECKIE DILL': [
        "Cool as ice, sharp as winter.",
        "My frosty glamour freezes the heart.",
        "A thawing kiss can melt the coldest soul.",
        "Scorched earth burns away the lies."
    ],
    'MEG NUTTE': [
        "Hot shots and scorching truth.",
        "The earth burns with righteous fire.",
        "A warm embrace for the redeemed.",
        "Join me by the campfire of salvation."
    ],
    'RILEY READE': [
        "Tidal waves of divine judgment.",
        "Drowning lust in the waters of life.",
        "Pure springs flow from the throne of grace.",
        "Drink and be refreshed, child of the King."
    ],
    'SILKY J': [
        "Smooth talker, sharp contracts.",
        "Exploitation ends when the King returns.",
        "Pimp slaps for those who exploit the weak.",
        "The contract trap binds until redemption."
    ],
}

# Quest definitions
QUESTS = {
    'stabilize_lunara': {
        'name': 'Stabilize Lunara',
        'description': 'Use Stabilize on Lunara to calm her manic rage',
        'required_move': 'stabilize',
        'reward': 'ANT QUEEN',
        'completed': False
    },
    'mirroraz_vanity': {
        'name': 'Mirroraz Vanity',
        'description': 'Defeat Mirroraz without being confused',
        'required_item': None,
        'reward': 'SGT KRAV',
        'completed': False
    },
    'owen_wisdom': {
        'name': 'Owen Woz Wisdom',
        'description': 'Learn the Wow Wisdom from Owen',
        'required_item': None,
        'reward': 'ZOMBIE LORD',
        'completed': False
    },
}

class AsylumArea:
    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x = x
        self.y = y
        self.npc_present = None
        self.quest_available = None
        self.visited = False
        
    def set_npc(self, npc_name: str):
        self.npc_present = npc_name
        
    def set_quest(self, quest_key: str):
        self.quest_available = quest_key

def create_asylum_areas() -> dict:
    areas = {}
    for key, data in AREAS.items():
        area = AsylumArea(data['name'], data['x'], data['y'])
        areas[key] = area
        
        # Assign NPCs to their chambers
        if 'LUNARA' in key.upper() or 'LUNARA' in data['name'].upper():
            area.set_npc('LUNARA')
        elif 'MIRRORAZ' in key.upper():
            area.set_npc('MIRRORAZ')
        elif 'OWEN' in key.upper() or 'WOZ' in key.upper():
            area.set_npc('OWEN WOZ')
        elif 'KRAV' in key.upper():
            area.set_npc('SGT KRAV')
        elif 'ANT' in key.upper():
            area.set_npc('ANT QUEEN')
        elif 'ZOMBIE' in key.upper():
            area.set_npc('ZOMBIE LORD')
        elif 'BRECKIE' in key.upper():
            area.set_npc('BRECKIE DILL')
        elif 'MEG' in key.upper():
            area.set_npc('MEG NUTTE')
        elif 'RILEY' in key.upper() and 'READE' in key.upper():
            area.set_npc('RILEY READE')
        elif 'SILKY' in key.upper():
            area.set_npc('SILKY J')
            
    return areas

# Ants vs Zombies mini-game
class AntZombieBattle:
    def __init__(self):
        self.ants_hp = 100
        self.zombies_hp = 100
        self.turn = 0
        self.game_over = False
        self.winner = None
        
    def ant_attack(self, attack_type: str) -> str:
        if attack_type == 'swarm':
            damage = 15
            self.zombies_hp -= damage
            return f"Ants swarm! Zombie HP: {self.zombies_hp}"
        elif attack_type == 'tunnel':
            return "Ants tunnel underground, evading next attack!"
        elif attack_type == 'royal_jelly':
            self.ants_hp = min(100, self.ants_hp + 20)
            return f"Royal jelly heals ants! Ant HP: {self.ants_hp}"
        return "Ants hesitate..."
            
    def zombie_attack(self, attack_type: str) -> str:
        if attack_type == 'undead_bite':
            damage = 12
            self.ants_hp -= damage
            return f"Zombie bites! Ant HP: {self.ants_hp}"
        elif attack_type == 'plague_cloud':
            damage = 10
            self.ants_hp -= damage
            return f"Plague cloud! Ant HP: {self.ants_hp}"
        elif attack_type == 'reanimate':
            self.zombies_hp = min(100, self.zombies_hp + 15)
            return f"Zombie reanimates! Zombie HP: {self.zombies_hp}"
        return "Zombies shamble..."
            
    def check_winner(self) -> Optional[str]:
        if self.ants_hp <= 0:
            self.game_over = True
            self.winner = 'ZOMBIES'
            return 'ZOMBIES'
        elif self.zombies_hp <= 0:
            self.game_over = True
            self.winner = 'ANTS'
            return 'ANTS'
        return None

# Audio for Asylum
def play_asylum_theme():
    """Play the asylum area theme - discordant but resolving to carrier"""
    # This would be called by the main audio engine
    pass

def play_ants_vs_zombies_music():
    """Play the RTS mini-game music"""
    # Fast-paced battle using VICTORY_CHIME frequency
    pass