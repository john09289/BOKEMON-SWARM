"""
Seraphim (Pokémon-like creatures) for BOKEMON SWARM
All data defined programmatically - no external assets
"""

from dataclasses import dataclass
from typing import List, Optional
from constants import CARRIER, PHI

@dataclass
class Move:
    name: str
    power: int
    hj_cost: float
    element: str
    description: str

@dataclass
class Seraphim:
    name: str
    element1: str
    element2: str
    level: int
    max_hp: int
    attack: int
    defense: int
    moves: List[Move]
    evolution: Optional[str] = None
    mercy_shards_required: int = 0

# Move definitions
def create_moves() -> dict:
    return {
        'carrier_lock': Move('Carrier Lock', 80, 20, 'Electric', 
            'Lock onto target with 11.71875 Hz carrier'),
        'mercy_pulse': Move('Mercy Pulse', 60, 15, 'Light',
            'Healing light that damages darkness'),
        'transmute': Move('Transmute', 70, 18, 'Light',
            'Convert enemy energy to ally HP'),
        'poison_sting': Move('Poison Sting', 40, 10, 'Bug',
            'Toxic barb that lingers'),
        'black_static': Move('Black Static', 50, 12, 'Dark',
            'Distortion field (11.72 corrected to 11.71875)'),
        'hive_mind': Move('Hive Mind', 90, 25, 'Dark',
            'Summon two Beedrills that attack separately'),
        'brute_force': Move('Brute Force', 95, 22, 'Psychic',
            'Overwhelming logic attack'),
        'logic_bomb': Move('Logic Bomb', 85, 20, 'Electric',
            'Disable enemy move for 2 turns'),
        'decode': Move('Decode', 0, 0, 'Psychic',
            'Reveal enemy weakness'),
        'aether_surge': Move('Aether Surge', 100, 25, 'Aether',
            'Unlimited energy blast'),
        'ac_dc': Move('AC/DC', 75, 18, 'Electric',
            'Alternating current shock'),
        'morgans_bane': Move('Morgan\'s Bane', 80, 20, 'Electric',
            'Corporate greed disruptor'),
        'radiant_heal': Move('Radiant Heal', 0, 15, 'Fairy',
            'Restore full HP to ally'),
        'daughters_kiss': Move('Daughter\'s Kiss', 70, 18, 'Fairy',
            'Blessed light from Makindran'),
        'christlight': Move('Christlight', 90, 22, 'Light',
            'Divine illumination'),
        'patent_steal': Move('Patent Steal', 65, 15, 'Dark',
            'Steal enemy technique'),
        'dc_smog': Move('DC Smog', 55, 12, 'Electric',
            'Choking darkness'),
        'debt_chain': Move('Debt Chain', 60, 15, 'Ghost',
            'Binds enemy with golden chains'),
        'gilded_cage': Move('Gilded Cage', 75, 20, 'Ghost',
            'Traps enemy in corporate prison'),
        'war_forge': Move('War Forge', 85, 20, 'Fire',
            'Weapons of conflict'),
        'vanity_mirror': Move('Vanity\'s Mirror', 70, 15, 'Dark',
            'Reflects enemy pride'),
        'scapegoat': Move('Scapegoat', 0, 0, 'Dark',
            'Takes enemy status effects'),
    }

# Seraphim roster
def create_seraphim_roster() -> dict:
    moves = create_moves()
    
    return {
        'KILO': Seraphim(
            name='KILO',
            element1='Electric',
            element2='Light',
            level=5,
            max_hp=80,
            attack=60,
            defense=50,
            moves=[moves['carrier_lock'], moves['mercy_pulse'], moves['transmute']],
            evolution='KILO ELITE',
            mercy_shards_required=5
        ),
        'B-GOLDEN': Seraphim(
            name='B-GOLDEN',
            element1='Bug',
            element2='Dark',
            level=15,
            max_hp=100,
            attack=80,
            defense=65,
            moves=[moves['poison_sting'], moves['black_static'], moves['hive_mind']],
            evolution=None
        ),
        'CARSON CHRIST': Seraphim(
            name='CARSON CHRIST',
            element1='Psychic',
            element2='Electric',
            level=20,
            max_hp=90,
            attack=85,
            defense=70,
            moves=[moves['brute_force'], moves['logic_bomb'], moves['decode']]
        ),
        'NIKOLA TESLA': Seraphim(
            name='NIKOLA TESLA',
            element1='Electric',
            element2='Aether',
            level=25,
            max_hp=110,
            attack=95,
            defense=75,
            moves=[moves['aether_surge'], moves['ac_dc'], moves['morgans_bane']]
        ),
        'MAKINDRAN': Seraphim(
            name='MAKINDRAN',
            element1='Light',
            element2='Fairy',
            level=30,
            max_hp=120,
            attack=70,
            defense=80,
            moves=[moves['radiant_heal'], moves['daughters_kiss'], moves['christlight']]
        ),
        'EDISON SHADE': Seraphim(
            name='EDISON SHADE',
            element1='Dark',
            element2='Electric',
            level=12,
            max_hp=70,
            attack=65,
            defense=55,
            moves=[moves['patent_steal'], moves['dc_smog']]
        ),
        'J.P. MORGAN WRAITH': Seraphim(
            name='J.P. MORGAN WRAITH',
            element1='Dark',
            element2='Ghost',
            level=14,
            max_hp=75,
            attack=60,
            defense=60,
            moves=[moves['debt_chain'], moves['gilded_cage']]
        ),
        'WATCHER AZAZEL': Seraphim(
            name='WATCHER AZAZEL',
            element1='Fire',
            element2='Dark',
            level=35,
            max_hp=150,
            attack=120,
            defense=90,
            moves=[moves['war_forge'], moves['vanity_mirror'], moves['scapegoat']]
        ),
    }

# Get all Seraphim
SERAPHIM_ROSTER = create_seraphim_roster()

def get_seraphim(name: str) -> Seraphim:
    return SERAPHIM_ROSTER.get(name)

def get_all_seraphim_names() -> List[str]:
    return list(SERAPHIM_ROSTER.keys())

# Evolution paths
EVOLUTION_PATHS = {
    'KILO': {
        'to': 'KILO ELITE',
        'level': 16,
        'shards': 5
    },
    'KILO ELITE': {
        'to': 'KILO WITNESS',
        'level': 36,
        'shards': 15
    }
}