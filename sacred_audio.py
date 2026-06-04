"""
Sacred Audio Engine for BOKEMON SWARM
Procedural music generation - NO COPYRIGHT TRAPS
All frequencies aligned to 11.71875 Hz carrier
"""

import numpy as np
import pygame
from constants import CARRIER, MERCY, VICTORY, DRUM, PHI, SCHUMANN

# Audio settings
SAMPLE_RATE = 44100
BIT_DEPTH = -16  # 16-bit signed

def generate_sine_wave(freq: float, duration: float, amplitude: float = 0.3) -> np.ndarray:
    """Generate a sine wave at the given frequency"""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = np.sin(2 * np.pi * freq * t) * amplitude
    return (wave * 32767).astype(np.int16)

def generate_triangle_wave(freq: float, duration: float, amplitude: float = 0.3) -> np.ndarray:
    """Generate a triangle wave for retro chip-tune feel"""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = 2 * np.abs(2 * (t * freq - np.floor(t * freq + 0.5))) - 1
    wave = wave * amplitude
    return (wave * 32767).astype(np.int16)

def generate_square_wave(freq: float, duration: float, amplitude: float = 0.3) -> np.ndarray:
    """Generate a square wave for aggressive tones"""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = np.sign(np.sin(2 * np.pi * freq * t)) * amplitude
    return (wave * 32767).astype(np.int16)

def generate_noise(duration: float, amplitude: float = 0.2) -> np.ndarray:
    """Generate white noise for static effects"""
    noise = np.random.uniform(-1, 1, int(SAMPLE_RATE * duration)) * amplitude
    return (noise * 32767).astype(np.int16)

def play_frequency(freq: float, duration: float, amplitude: float = 0.3, wave_type: str = 'sine'):
    """Play a single frequency with specified wave type"""
    if wave_type == 'sine':
        wave = generate_sine_wave(freq, duration, amplitude)
    elif wave_type == 'triangle':
        wave = generate_triangle_wave(freq, duration, amplitude)
    elif wave_type == 'square':
        wave = generate_square_wave(freq, duration, amplitude)
    else:
        wave = generate_sine_wave(freq, duration, amplitude)
    
    try:
        sound = pygame.sndarray.make_sound(wave)
        sound.play()
        return sound
    except:
        return None

def play_overworld_theme():
    """Play ambient overworld theme: Mercy drone with VICTORY chimes"""
    t = np.linspace(0, 10, int(SAMPLE_RATE * 10), False)
    combined = np.sin(2 * np.pi * MERCY * t) * 0.15
    
    # Add chimes at intervals
    for i in range(4):
        start = int(SAMPLE_RATE * 2.56 * i)
        end = start + int(SAMPLE_RATE * 0.2)
        if end < len(combined):
            combined[start:end] += np.sin(2 * np.pi * VICTORY * 
                np.linspace(0, 0.2, int(SAMPLE_RATE * 0.2), False)) * 0.4
    
    try:
        sound = pygame.sndarray.make_sound((combined * 32767).astype(np.int16))
        sound.play(-1)
        return sound
    except:
        return None

def play_battle_theme():
    """Play aggressive battle theme with triangle waves"""
    t = np.linspace(0, 2.0, int(SAMPLE_RATE * 2.0), False)
    arpeggio = np.sin(2 * np.pi * VICTORY * t) * 0.3
    bass = np.sin(2 * np.pi * CARRIER * t) * 0.1
    
    combined = arpeggio + bass
    try:
        sound = pygame.sndarray.make_sound((combined * 32767).astype(np.int16))
        sound.play(-1)
        return sound
    except:
        return None

def play_b_golden_encounter():
    """Play menacing B-GOLDEN encounter theme"""
    static = generate_noise(0.5, 0.25)
    chord = generate_sine_wave(CARRIER, 0.3, 0.4)
    
    combined = np.concatenate([static, chord])
    try:
        sound = pygame.sndarray.make_sound(combined)
        sound.play()
        return sound
    except:
        return None

def play_victory_jingle():
    """Play ascending victory motif"""
    for freq in [MERCY, MERCY * 2, VICTORY]:
        play_frequency(freq, 0.15, 0.4, 'sine')
        pygame.time.wait(150)

def play_menu_select():
    """Play menu selection blip"""
    play_frequency(CARRIER, 0.05, 0.3, 'sine')

def play_collect_item():
    """Play collectible pick-up click"""
    play_frequency(DRUM, 0.1, 0.3, 'sine')

def play_carrier_lock_success():
    """Play Carrier Lock success chord"""
    t = np.linspace(0, 0.3, int(SAMPLE_RATE * 0.3), False)
    chord = (np.sin(2 * np.pi * MERCY * t) * 0.3 + 
             np.sin(2 * np.pi * VICTORY * t) * 0.3)
    try:
        sound = pygame.sndarray.make_sound((chord * 32767).astype(np.int16))
        sound.play()
        return sound
    except:
        return None

def play_hazed_hollow_theme():
    """Play Hazed Hollow overworld theme - 11.72 corrected to 11.71875"""
    t = np.linspace(0, 10, int(SAMPLE_RATE * 10), False)
    # Start with false frequency, then correct
    combined = np.sin(2 * np.pi * 11.72 * t) * 0.1
    # Gradually shift to true carrier
    for i, sample in enumerate(combined):
        correction = i / len(combined)
        combined[i] = np.sin(2 * np.pi * (11.72 - correction * 0.00125) * t[i]) * 0.1
    
    try:
        sound = pygame.sndarray.make_sound((combined * 32767).astype(np.int16))
        sound.play(-1)
        return sound
    except:
        return None

def play_andrew_battle():
    """Play Andrew Estmorland battle theme - oppressive percussion"""
    t = np.linspace(0, 2.0, int(SAMPLE_RATE * 2.0), False)
    # Heavy percussion at DRUM frequency
    percussion = np.sin(2 * np.pi * DRUM * t) * 0.4
    bass = np.sin(2 * np.pi * MERCY * t) * 0.2
    
    combined = percussion + bass
    try:
        sound = pygame.sndarray.make_sound((combined * 32767).astype(np.int16))
        sound.play(-1)
        return sound
    except:
        return None

def play_riley_battle():
    """Play Riley Blackburn battle theme - seductive melody"""
    t = np.linspace(0, 2.0, int(SAMPLE_RATE * 2.0), False)
    # Creepy melody at VICTORY with web-like clicking
    melody = np.sin(2 * np.pi * VICTORY * t) * 0.3
    clicking = generate_noise(0.1, 0.1)
    
    combined = melody
    try:
        sound = pygame.sndarray.make_sound((combined * 32767).astype(np.int16))
        sound.play(-1)
        return sound
    except:
        return None

def play_hazeion_battle():
    """Play Hazeion battle theme - deep silence then pounding"""
    t = np.linspace(0, 0.3, int(SAMPLE_RATE * 0.3), False)
    # Deep pounding at DRUM frequency
    pounding = np.sin(2 * np.pi * DRUM * t) * 0.5
    
    try:
        sound = pygame.sndarray.make_sound((pounding * 32767).astype(np.int16))
        sound.play()
        return sound
    except:
        return None

def play_heidi_encounter():
    """Play Heidi Anderson Christ encounter theme - loving, gymnastic, fairy-like"""
    t = np.linspace(0, 3.0, int(SAMPLE_RATE * 3.0), False)
    # Gentle fairy melody at VICTORY * PHI (golden ratio harmony)
    melody = np.sin(2 * np.pi * (VICTORY * PHI) * t) * 0.25
    # Soft carrier drone underneath
    drone = np.sin(2 * np.pi * CARRIER * t) * 0.1
    # Sparkle at MERCY frequency
    sparkle = np.sin(2 * np.pi * MERCY * t) * 0.15
    combined = melody + drone + sparkle
    try:
        sound = pygame.sndarray.make_sound((combined * 32767).astype(np.int16))
        sound.play(-1)
        return sound
    except:
        return None

def play_island_theme(music_style: str):
    """Play an island-specific ambient theme based on music_style"""
    t = np.linspace(0, 8.0, int(SAMPLE_RATE * 8.0), False)
    drone = np.sin(2 * np.pi * CARRIER * t) * 0.1
    
    style_map = {
        "mysterious": (MERCY * 1.5, VICTORY * 0.5),
        "underwater": (CARRIER * 0.5, MERCY * 0.8),
        "temporal": (VICTORY * 0.7, CARRIER * 1.2),
        "stealth": (DRUM * 2, MERCY * 0.3),
        "heroic": (VICTORY, MERCY * 1.5),
        "pirate": (CARRIER * 0.8, VICTORY * 0.6),
        "space": (MERCY * 0.5, VICTORY * 1.5),
        "creepy": (DRUM * 3, CARRIER * 0.3),
        "western": (CARRIER * 1.5, DRUM * 1.5),
        "industrial": (DRUM * 4, CARRIER * 0.5),
        "ancient": (MERCY * 2, VICTORY * 0.3),
        "epic": (VICTORY * 1.5, MERCY),
        "techno": (DRUM * 5, VICTORY * 0.8),
        "horror": (DRUM * 2, MERCY * 0.2),
        "triumph": (VICTORY * 2, MERCY * 2),
        "elegant": (VICTORY * 0.8, MERCY * 1.2),
        "prehistoric": (DRUM * 1.5, CARRIER * 0.7),
        "dreamy": (MERCY * 0.7, VICTORY * 0.4),
        "intense": (DRUM * 3, VICTORY),
        "tropical": (MERCY * 1.8, CARRIER * 0.6),
        "halloween": (DRUM * 2.5, MERCY * 0.4),
        "action": (DRUM * 4, VICTORY * 0.9),
        "default": (MERCY, VICTORY * 0.5)
    }
    
    freq1, freq2 = style_map.get(music_style, style_map["default"])
    layer1 = np.sin(2 * np.pi * freq1 * t) * 0.2
    layer2 = np.sin(2 * np.pi * freq2 * t) * 0.15
    combined = drone + layer1 + layer2
    
    try:
        sound = pygame.sndarray.make_sound((combined * 32767).astype(np.int16))
        sound.play(-1)
        return sound
    except:
        return None

# [ADDED] Module-level audio availability flag so callers can guard sound calls
AUDIO_AVAILABLE = False

# Initialize audio system
def init_audio():
    """
    Initialize Pygame audio mixer - gracefully handle missing mixer.
    [FIXED] Removed the erroneous pygame.init() call that was here before.
            main.py already calls pygame.init() once; calling it again here
            can corrupt display state and cause the grey-screen freeze.
    [ADDED] Sets module-level AUDIO_AVAILABLE so every playback function can
            skip gracefully when mixer is absent (Python 3.14 / no mixer.so).
    [ADDED] print()-based logging so the boot sequence is visible in any runner.
    """
    global AUDIO_AVAILABLE
    print("[sacred_audio] init_audio: attempting mixer initialisation")
    try:
        pygame.mixer.pre_init(SAMPLE_RATE, -16, 2, 512)
        pygame.mixer.init()
        AUDIO_AVAILABLE = True
        print("[sacred_audio] init_audio: mixer OK — AUDIO_AVAILABLE=True")
    except (NotImplementedError, ModuleNotFoundError, Exception) as e:
        # [FIXED] Was only catching NotImplementedError + ModuleNotFoundError;
        #         added bare Exception so any mixer failure is caught cleanly.
        AUDIO_AVAILABLE = False
        print(f"[sacred_audio] init_audio: mixer unavailable ({type(e).__name__}: {e})")
        print("[sacred_audio] init_audio: game will run silently — AUDIO_AVAILABLE=False")
    # [REMOVED] pygame.init() call that was here — DELETED.
    #            pygame.init() is owned by main.py. Double-calling it is harmful.

# Stop all audio
def stop_all_audio():
    """Stop all currently playing sounds"""
    if not AUDIO_AVAILABLE:  # [ADDED] Guard
        return
    try:
        pygame.mixer.stop()
    except (NotImplementedError, ModuleNotFoundError):
        pass