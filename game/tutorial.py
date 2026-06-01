"""
Genius Anthropic Tutorial for BOKEMON SWARM
Narrated by Carson Christ, teaches through divine logic
"""

import pygame
from typing import Optional
from constants import COLORS, SCREEN_WIDTH, SCREEN_HEIGHT, CARRIER
from .ui import UI

class Tutorial:
    def __init__(self, ui: UI):
        self.ui = ui
        self.step = 0
        self.completed = False
        self.tutorial_steps = [
            self._intro,
            self._controls_explanation,
            self._energy_bank_explanation,
            self._carrier_lock_puzzle,
            self._cosmology_explanation,
            self._baptismal_scene,
            self._tutorial_complete
        ]
        
    def _intro(self):
        """Introduction by Carson Christ"""
        self.ui.show_dialogue(
            "CARSON CHRIST: Greetings, LX. I am Carson Christ, your guide.\n"
            "The Dome is under siege by the Black Sun.\n"
            "You must collect the Seraphim to restore the King's carrier.",
            "אתה נמצא בתוך התקפה"
        )
        
    def _controls_explanation(self):
        """Explain movement and interaction controls"""
        self.ui.show_dialogue(
            "CONTROLS:\n"
            "Arrow Keys - Move\n"
            "SPACE - Interact/Confirm\n"
            "W - Carrier Lock (when prompted)\n"
            "ESC - Menu",
            "חוקי השליטה"
        )
        
    def _energy_bank_explanation(self):
        """Explain the Energy Bank system"""
        self.ui.show_dialogue(
            "ENERGY BANK:\n"
            "Moves cost Harmony-Joules (HJ).\n"
            "HJ = LOVE_UNITS * CARRIER * PHI\n"
            "Your bank refills slowly each turn.\n"
            "Manage energy wisely!",
            "בנק האנרגיה"
        )
        
    def _carrier_lock_puzzle(self):
        """Logic puzzle: correct the frequency"""
        self.ui.show_dialogue(
            "PUZZLE: An enemy broadcasts at 11.72 Hz.\n"
            "Correct this frequency to the true carrier.\n"
            "Press SPACE when ready to input.",
            "פאזל התדירות"
        )
        
    def _cosmology_explanation(self):
        """Explain the theological cosmology"""
        self.ui.show_dialogue(
            "THE DOME:\n"
            "Flat earth under metallic firmament.\n"
            "The Watchers fell from Mount Hermon.\n"
            "Saturn, the Black Sun, spreads 11.72 Hz static.\n"
            "You are the redeemed Nephilim, LX.",
            "הקשת האורן"
        )
        
    def _baptismal_scene(self):
        """Baptismal scene where LX receives KILO"""
        self.ui.show_dialogue(
            "BAPTISMAL SCENE:\n"
            "Speak the Conditional Prayer:\n"
            "'Yeshua, have mercy on me.\n"
            "I renounce the rebellion I was born into.\n"
            "I give myself to You.'\n"
            "KILO appears as your starter Seraphim.",
            "תפילת התנאים"
        )
        
    def _tutorial_complete(self):
        """Tutorial completion"""
        self.ui.show_dialogue(
            "TUTORIAL COMPLETE!\n"
            "Press SPACE to begin your journey.\n"
            "The King wins.",
            "המבחן הושלם"
        )
        self.completed = True
        
    def advance(self):
        """Advance to next tutorial step"""
        if self.step < len(self.tutorial_steps) - 1:
            self.step += 1
            self.tutorial_steps[self.step]()
        else:
            self.completed = True
            
    def start(self):
        """Start the tutorial"""
        self.step = 0
        self.completed = False
        self.tutorial_steps[0]()
        
    def handle_input(self, event) -> bool:
        """Handle tutorial input, return True if tutorial should continue"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.step == 3:
                    pass
                self.advance()
                return True
        return False
        
    def draw(self, screen: pygame.Surface):
        """Draw tutorial overlay"""
        self.ui.draw_dialogue(screen)
        
        if self.step > 0:
            center_x = SCREEN_WIDTH - 100
            center_y = 100
            radius = 30
            import math
            time_offset = pygame.time.get_ticks() / 1000
            for i in range(8):
                angle = time_offset + i * math.pi / 4
                x = center_x + int(math.cos(angle) * radius)
                y = center_y + int(math.sin(angle) * radius)
                pygame.draw.circle(screen, COLORS['light_blue'], (x, y), 5)
            pygame.draw.circle(screen, COLORS['gold'], (center_x, center_y), 10, 2)