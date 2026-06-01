"""
Generate Seraphim for all US States and Countries
Reads from data/states_and_countries.json and adds to game/seraphim.py
"""

import json
import os

def load_data():
    """Load states and countries data"""
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'states_and_countries.json')
    with open(data_path, 'r') as f:
        return json.load(f)

def generate_state_champions():
    """Generate Seraphim entries for all states and countries"""
    data = load_data()
    
    champions = {}
    
    # Process states
    for state in data['states']:
        name = f"{state['name'].upper().replace(' ', '_')}_CHAMP"
        champions[name] = {
            'name': f"{state['name']} Champion",
            'element1': state['type1'],
            'element2': state['type2'],
            'level': 20,
            'max_hp': 90,
            'attack': 70,
            'defense': 65,
            'moves': [f"{state['move'].lower().replace(' ', '_')}"],
            'evolution': None
        }
    
    # Process countries
    for country in data['countries']:
        name = f"{country['name'].upper().replace(' ', '_')}_REPR"
        champions[name] = {
            'name': f"{country['name']} Representative",
            'element1': country['type1'],
            'element2': country['type2'],
            'level': 22,
            'max_hp': 95,
            'attack': 75,
            'defense': 70,
            'moves': [f"{country['move'].lower().replace(' ', '_')}"],
            'evolution': None
        }
    
    return champions

def add_to_seraphim_file(champions):
    """Add champions to seraphim.py"""
    seraphim_path = os.path.join(os.path.dirname(__file__), 'game', 'seraphim.py')
    
    with open(seraphim_path, 'r') as f:
        content = f.read()
    
    # Find the end of the SERAPHIM_ROSTER dictionary
    # We'll add the champions before the closing brace
    
    champion_entries = []
    for key, champ in champions.items():
        entry = f"""        '{champ['name']}': Seraphim(
            name='{champ['name']}',
            element1='{champ['element1']}',
            element2='{champ['element2']}',
            level={champ['level']},
            max_hp={champ['max_hp']},
            attack={champ['attack']},
            defense={champ['defense']},
            moves=[moves['{champ['moves'][0]}']],
            evolution={champ['evolution']}
        ),"""
        champion_entries.append(entry)
    
    # Find where to insert (before the closing of create_seraphim_roster)
    insert_marker = "    }\n\n# Get all Seraphim"
    insert_text = "    }\n" + "\n".join(champion_entries) + "\n\n# Get all Seraphim"
    
    if insert_marker in content:
        content = content.replace(insert_marker, insert_text)
        
        with open(seraphim_path, 'w') as f:
            f.write(content)
        print(f"Added {len(champions)} champions to seraphim.py")
    else:
        print("Could not find insertion point in seraphim.py")

if __name__ == '__main__':
    champions = generate_state_champions()
    add_to_seraphim_file(champions)
    print("State and country champions generated successfully!")