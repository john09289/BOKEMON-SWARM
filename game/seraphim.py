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
        'haze_compliance': Move('Haze of Compliance', 70, 15, 'Dark',
            'Oppressive fog that drains will'),
        'suffer_to_sleep': Move('Suffer-to-Sleep', 0, 0, 'Dark',
            'Puts target to sleep with ongoing damage'),
        'shut_down': Move('Shut-Down', 80, 20, 'Dark',
            'Complete mental shutdown'),
        'discordant_chord': Move('Discordant Chord', 65, 15, 'Psychic',
            'False praise that spreads static'),
        'false_praise': Move('False Praise', 50, 10, 'Normal',
            'Lures with deceptive melody'),
        'echo_of_enoch': Move('Echo of Enoch', 75, 18, 'Psychic',
            'Ancient knowledge blast'),
        'cube_trap': Move('Cube Trap', 60, 12, 'Psychic',
            'Confuses target with patterns'),
        'algorithm': Move('Algorithm', 85, 20, 'Steel',
            'Predicts and counters moves'),
        'speed_solve': Move('Speed Solve', 0, 0, 'Psychic',
            'Solves cube to boost stats'),
        'loveless_web': Move('Loveless Web', 55, 12, 'Bug',
            'Ensnares with empty desire'),
        'desire_drain': Move('Desire Drain', 70, 15, 'Dark',
            'Drains Energy Bank'),
        'widows_kiss': Move('Widow\'s Kiss', 65, 14, 'Dark',
            'Bitter embrace'),
        'reagans_rejection': Move('Reagan\'s Rejection', 0, 0, 'Dark',
            'Self-harming move of denial'),
        'cube_missile': Move('Cube Missile', 80, 18, 'Electric',
            'Launching rotating blocks'),
        'scramble_shield': Move('Scramble Shield', 0, 0, 'Steel',
            'Defends with shifting cubes'),
        'haze_summon': Move('Haze Summon', 90, 25, 'Dark',
            'Calls Hazeion to battle'),
        # Asylum of Temptation moves
        'manic_wave': Move('Manic Wave', 70, 15, 'Fire',
            'Uncontrolled fire attack'),
        'depressive_fog': Move('Depressive Fog', 0, 0, 'Dark',
            'Lowers speed and attack'),
        'stabilize': Move('Stabilize', 0, 0, 'Light',
            'Cures confusion and rage'),
        'mirror_coat': Move('Mirror Coat', 0, 0, 'Dark',
            'Reflects psychic attacks'),
        'vanity_drain': Move('Vanity Drain', 60, 12, 'Dark',
            'Steals beauty for power'),
        'selfie_curse': Move('Selfie Curse', 50, 10, 'Dark',
            'Confuses target with vanity'),
        'discordant_wail': Move('Discordant Wail', 80, 18, 'Dark',
            'Multi-hit baby attack'),
        'crawling_horror': Move('Crawling Horror', 40, 8, 'Dark',
            'Low-level fear damage'),
        'bite': Move('Bite', 30, 5, 'Dark',
            'Basic attack'),
        'wow_wisdom': Move('Wow Wisdom', 60, 10, 'Normal',
            'Random stat boost'),
        'lightning_mcqueen': Move('Lightning McQueen', 75, 15, 'Electric',
            'Speedy electric dash'),
        'nose_crunch': Move('Nose Crunch', 50, 8, 'Normal',
            'Headbutt attack'),
        'swarm': Move('Swarm', 65, 12, 'Bug',
            'Multiple small attacks'),
        'tunnel': Move('Tunnel', 0, 0, 'Ground',
            'Dodges next attack'),
        'royal_jelly': Move('Royal Jelly', 0, 0, 'Bug',
            'Heals party'),
        'undead_bite': Move('Undead Bite', 55, 10, 'Ghost',
            'Drains HP'),
        'plague_cloud': Move('Plague Cloud', 70, 15, 'Poison',
            'Poison all enemies'),
        'reanimate': Move('Reanimate', 0, 0, 'Ghost',
            'Revives fallen ally'),
        'krav_strike': Move('Krav Strike', 85, 18, 'Fighting',
            'Priority counter attack'),
        'pride_beam': Move('Pride Beam', 70, 12, 'Fairy',
            'Rainbow laser attack'),
        'daddy_issues': Move('Daddy Issues', 0, 0, 'Fairy',
            'Stat fluctuation'),
        'fabulous_uppercut': Move('Fabulous Uppercut', 65, 10, 'Fighting',
            'Powerful punch'),
        'glitter_grenade': Move('Glitter Grenade', 75, 15, 'Fairy',
            'Area fairy damage'),
        'frosty_glamour': Move('Frosty Glamour', 60, 12, 'Ice',
            'Freezing attack'),
        'thawing_kiss': Move('Thawing Kiss', 0, 0, 'Light',
            'Healing move'),
        'hot_shot': Move('Hot Shot', 70, 12, 'Fire',
            'Fire attack'),
        'scorched_earth': Move('Scorched Earth', 80, 18, 'Fire',
            'Area fire damage'),
        'warm_embrace': Move('Warm Embrace', 0, 0, 'Light',
            'Healing move'),
        'tidal_wave': Move('Tidal Wave', 75, 15, 'Water',
            'Water attack'),
        'drowning_lust': Move('Drowning Lust', 65, 12, 'Dark',
            'Drains energy'),
        'pure_spring': Move('Pure Spring', 0, 0, 'Light',
            'Cures status'),
        'pimp_slap': Move('Pimp Slap', 55, 10, 'Dark',
            'Dark attack'),
        'contract_trap': Move('Contract Trap', 0, 0, 'Dark',
            'Traps enemy'),
        'exploitation': Move('Exploitation', 80, 18, 'Dark',
            'Drains all stats'),
        # Hyperculture moves
        'flight_23': Move('Flight 23', 85, 20, 'Flying',
            'Meteor dunk from the rafters'),
        'airness': Move('Airness', 0, 0, 'Flying',
            'Float above all attacks'),
        'flu_game': Move('Flu Game', 70, 15, 'Fire',
            'Play through pain'),
        'deadstock': Move('Deadstock', 60, 12, 'Steel',
            'Perfect condition attack'),
        'bid_war': Move('Bid War', 0, 0, 'Psychic',
            'Forces enemy to switch moves'),
        'legit_check': Move('Legit Check', 50, 10, 'Normal',
            'Reveals enemy weakness'),
        'denim_sutra': Move('Denim Sutra', 75, 15, 'Light',
            'Enlightened denim strike'),
        'karma_stitch': Move('Karma Stitch', 0, 0, 'Fairy',
            'Heals based on damage dealt'),
        'bargain_enlightenment': Move('Bargain Enlightenment', 65, 12, 'Light',
            'Discounted healing'),
        'gothic_flash': Move('Gothic Flash', 80, 18, 'Dark',
            'Blinding chrome light'),
        'rockstar_bleed': Move('Rockstar Bleed', 70, 15, 'Dark',
            'Life drain with style'),
        'reapers_hoodie': Move('Reaper\'s Hoodie', 0, 0, 'Dark',
            'Stealth and protection'),
        'anchor_drop': Move('Anchor Drop', 75, 15, 'Water',
            'Heavy water attack'),
        'windbreaker_shield': Move('Windbreaker Shield', 0, 0, 'Flying',
            'Deflects wind attacks'),
        'retro_wave': Move('Retro Wave', 60, 12, 'Water',
            'Nostalgic water blast'),
        'tail_wag': Move('Tail Wag', 0, 0, 'Normal',
            'Heals party morale'),
        'retail_bite': Move('Retail Bite', 55, 10, 'Dark',
            'Bargain attack'),
        'dad_energy': Move('Dad Energy', 65, 12, 'Normal',
            'Unexpected power boost'),
        'airdrop_strike': Move('AirDrop Strike', 80, 18, 'Electric',
            'Deliver justice from above'),
        'patent_war': Move('Patent War', 70, 15, 'Steel',
            'Defend innovation'),
        'ecosystem_lock': Move('Ecosystem Lock', 0, 0, 'Electric',
            'Secure the Dome'),
        # Poptropi-Con moves
        'beta_blast': Move('Beta Blast', 75, 18, 'Psychic',
            'Glitchy reality warp from Early-Dome era'),
        'glitch_shift': Move('Glitch Shift', 0, 0, 'Psychic',
            'Warps position and confuses target'),
        'nostalgia_drain': Move('Nostalgia Drain', 65, 14, 'Dark',
            'Drains HP by recalling lost memories'),
        'slide_tackle': Move('Slide Tackle', 70, 15, 'Ice',
            'Low icy slide attack'),
        'ice_gadget': Move('Ice Gadget', 60, 12, 'Ice',
            'Freezing gadget deployment'),
        'martini_shaker': Move('Martini Shaker', 55, 10, 'Dark',
            'Classy but damaging shake'),
        'frequency_punch': Move('Frequency Punch', 80, 18, 'Light',
            '11.71875 Hz harmonic strike'),
        'static_shield': Move('Static Shield', 0, 0, 'Electric',
            'Blocks next attack with static'),
        'hero_landing': Move('Hero Landing', 85, 20, 'Fighting',
            'Dramatic descent attack'),
        'temporal_loop': Move('Temporal Loop', 70, 16, 'Psychic',
            'Forces target to repeat last move'),
        'erasure': Move('Erasure', 90, 22, 'Dark',
            'Deletes target from timeline temporarily'),
        'history_theft': Move('History Theft', 65, 14, 'Psychic',
            'Steals stat boosts from target'),
        'carrier_purge': Move('Carrier Purge', 85, 20, 'Dark',
            'Cleanses corrupted carrier frequency'),
        'balloon_burst': Move('Balloon Burst', 90, 22, 'Fire',
            'Explosive fire/flying combo'),
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
        # Westmoreland Haze characters
        'ANDREW ESTMORLAND': Seraphim(
            name='ANDREW ESTMORLAND',
            element1='Dark',
            element2='Poison',
            level=18,
            max_hp=110,
            attack=75,
            defense=70,
            moves=[moves['haze_compliance'], moves['suffer_to_sleep'], moves['shut_down']]
        ),
        'ZACH WILLIAMS': Seraphim(
            name='ZACH WILLIAMS',
            element1='Psychic',
            element2='Normal',
            level=16,
            max_hp=85,
            attack=60,
            defense=65,
            moves=[moves['discordant_chord'], moves['false_praise'], moves['echo_of_enoch']]
        ),
        'GAARET LEISTER': Seraphim(
            name='GAARET LEISTER',
            element1='Psychic',
            element2='Steel',
            level=22,
            max_hp=95,
            attack=70,
            defense=80,
            moves=[moves['cube_trap'], moves['algorithm'], moves['speed_solve']]
        ),
        'RILEY BLACKBURN': Seraphim(
            name='RILEY BLACKBURN',
            element1='Bug',
            element2='Dark',
            level=20,
            max_hp=90,
            attack=75,
            defense=65,
            moves=[moves['loveless_web'], moves['desire_drain'], moves['widows_kiss'], moves['reagans_rejection']]
        ),
        'ELI': Seraphim(
            name='ELI',
            element1='Electric',
            element2='Steel',
            level=24,
            max_hp=100,
            attack=85,
            defense=80,
            moves=[moves['cube_missile'], moves['scramble_shield'], moves['speed_solve']]
        ),
        'HAZEION': Seraphim(
            name='HAZEION',
            element1='Dark',
            element2='Abyssal',
            level=40,
            max_hp=180,
            attack=100,
            defense=100,
            moves=[moves['haze_summon'], moves['haze_compliance'], moves['shut_down']]
        ),
        # Asylum of Temptation characters
        'LUNARA': Seraphim(
            name='LUNARA',
            element1='Psychic',
            element2='Fire',
            level=20,
            max_hp=95,
            attack=70,
            defense=65,
            moves=[moves['manic_wave'], moves['depressive_fog'], moves['stabilize']]
        ),
        'MIRRORAZ': Seraphim(
            name='MIRRORAZ',
            element1='Dark',
            element2='Fairy',
            level=18,
            max_hp=85,
            attack=60,
            defense=75,
            moves=[moves['mirror_coat'], moves['vanity_drain'], moves['selfie_curse']]
        ),
        'OWEN WOZ': Seraphim(
            name='OWEN WOZ',
            element1='Normal',
            element2='Light',
            level=15,
            max_hp=75,
            attack=55,
            defense=50,
            moves=[moves['wow_wisdom'], moves['lightning_mcqueen'], moves['nose_crunch']]
        ),
        'ANT QUEEN': Seraphim(
            name='ANT QUEEN',
            element1='Bug',
            element2='Ground',
            level=22,
            max_hp=100,
            attack=75,
            defense=70,
            moves=[moves['swarm'], moves['tunnel'], moves['royal_jelly']]
        ),
        'ZOMBIE LORD': Seraphim(
            name='ZOMBIE LORD',
            element1='Ghost',
            element2='Poison',
            level=24,
            max_hp=110,
            attack=80,
            defense=65,
            moves=[moves['undead_bite'], moves['plague_cloud'], moves['reanimate']]
        ),
        'SGT KRAV': Seraphim(
            name='SGT KRAV',
            element1='Fighting',
            element2='Steel',
            level=25,
            max_hp=105,
            attack=90,
            defense=75,
            moves=[moves['krav_strike'], moves['fabulous_uppercut'], moves['glitter_grenade']]
        ),
        'BRECKIE DILL': Seraphim(
            name='BRECKIE DILL',
            element1='Ice',
            element2='Dark',
            level=19,
            max_hp=88,
            attack=65,
            defense=60,
            moves=[moves['frosty_glamour'], moves['thawing_kiss'], moves['scorched_earth']]
        ),
        'MEG NUTTE': Seraphim(
            name='MEG NUTTE',
            element1='Fire',
            element2='Dark',
            level=21,
            max_hp=92,
            attack=78,
            defense=62,
            moves=[moves['hot_shot'], moves['scorched_earth'], moves['warm_embrace']]
        ),
        'RILEY READE': Seraphim(
            name='RILEY READE',
            element1='Water',
            element2='Dark',
            level=20,
            max_hp=85,
            attack=70,
            defense=65,
            moves=[moves['tidal_wave'], moves['drowning_lust'], moves['pure_spring']]
        ),
        'SILKY J': Seraphim(
            name='SILKY J',
            element1='Dark',
            element2='Steel',
            level=23,
            max_hp=95,
            attack=75,
            defense=70,
            moves=[moves['pimp_slap'], moves['contract_trap'], moves['exploitation']]
        ),
        # Hyperculture characters
        'AIR JORDAN': Seraphim(
            name='AIR JORDAN',
            element1='Flying',
            element2='Fire',
            level=25,
            max_hp=100,
            attack=85,
            defense=75,
            moves=[moves['flight_23'], moves['airness'], moves['flu_game']]
        ),
        'STOCK-X GOLEM': Seraphim(
            name='STOCK-X GOLEM',
            element1='Steel',
            element2='Psychic',
            level=22,
            max_hp=95,
            attack=70,
            defense=80,
            moves=[moves['deadstock'], moves['bid_war'], moves['legit_check']]
        ),
        'TRUE RELIGION BUDDHA': Seraphim(
            name='TRUE RELIGION BUDDHA',
            element1='Light',
            element2='Fairy',
            level=20,
            max_hp=90,
            attack=65,
            defense=70,
            moves=[moves['denim_sutra'], moves['karma_stitch'], moves['bargain_enlightenment']]
        ),
        'CHROME HEARTS CROSS': Seraphim(
            name='CHROME HEARTS CROSS',
            element1='Steel',
            element2='Dark',
            level=24,
            max_hp=95,
            attack=75,
            defense=75,
            moves=[moves['gothic_flash'], moves['rockstar_bleed'], moves['reapers_hoodie']]
        ),
        'NAUTICA SAILOR': Seraphim(
            name='NAUTICA SAILOR',
            element1='Water',
            element2='Normal',
            level=18,
            max_hp=80,
            attack=60,
            defense=65,
            moves=[moves['anchor_drop'], moves['windbreaker_shield'], moves['retro_wave']]
        ),
        'BIGDOG PUP': Seraphim(
            name='BIGDOG PUP',
            element1='Normal',
            element2='Fighting',
            level=16,
            max_hp=75,
            attack=55,
            defense=60,
            moves=[moves['tail_wag'], moves['retail_bite'], moves['dad_energy']]
        ),
        'LX APPLE': Seraphim(
            name='LX APPLE',
            element1='Grass',
            element2='Electric',
            level=28,
            max_hp=110,
            attack=80,
            defense=85,
            moves=[moves['airdrop_strike'], moves['patent_war'], moves['ecosystem_lock']]
        ),
        # Poptropi-Con Seraphim
        'THE PURPLE WATCHER': Seraphim(
            name='THE PURPLE WATCHER',
            element1='Psychic',
            element2='Dark',
            level=12,
            max_hp=85,
            attack=65,
            defense=55,
            moves=[moves['beta_blast'], moves['glitch_shift'], moves['nostalgia_drain']]
        ),
        'MEGALODON WATCHER': Seraphim(
            name='MEGALODON WATCHER',
            element1='Water',
            element2='Dark',
            level=18,
            max_hp=110,
            attack=75,
            defense=60,
            moves=[moves['tidal_wave'], moves['drowning_lust'], moves['nostalgia_drain']]
        ),
        'DIRECTOR ZED': Seraphim(
            name='DIRECTOR ZED',
            element1='Steel',
            element2='Psychic',
            level=22,
            max_hp=95,
            attack=70,
            defense=80,
            moves=[moves['algorithm'], moves['logic_bomb'], moves['glitch_shift']]
        ),
        'AGENT PENGUIN': Seraphim(
            name='AGENT PENGUIN',
            element1='Ice',
            element2='Fighting',
            level=16,
            max_hp=80,
            attack=60,
            defense=65,
            moves=[moves['slide_tackle'], moves['ice_gadget'], moves['martini_shaker']]
        ),
        'THE MEGALOMANIAC': Seraphim(
            name='THE MEGALOMANIAC',
            element1='Electric',
            element2='Dark',
            level=25,
            max_hp=100,
            attack=85,
            defense=70,
            moves=[moves['black_static'], moves['ac_dc'], moves['glitch_shift']]
        ),
        'CAPTAIN CORRECTION': Seraphim(
            name='CAPTAIN CORRECTION',
            element1='Light',
            element2='Steel',
            level=20,
            max_hp=90,
            attack=75,
            defense=75,
            moves=[moves['frequency_punch'], moves['static_shield'], moves['hero_landing']]
        ),
        'CHRONOS WATCHER': Seraphim(
            name='CHRONOS WATCHER',
            element1='Psychic',
            element2='Dragon',
            level=30,
            max_hp=130,
            attack=95,
            defense=85,
            moves=[moves['temporal_loop'], moves['erasure'], moves['history_theft']]
        ),
        'BLOON-PHOENIX': Seraphim(
            name='BLOON-PHOENIX',
            element1='Fire',
            element2='Flying',
            level=35,
            max_hp=140,
            attack=110,
            defense=80,
            moves=[moves['balloon_burst'], moves['carrier_purge'], moves['hero_landing']]
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