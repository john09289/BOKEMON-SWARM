"""
Hazed Hollow - Westmoreland Haze area for BOKEMON SWARM
"""

import pygame
from typing import Dict, Optional
from constants import COLORS, SCREEN_WIDTH, SCREEN_HEIGHT
from .ui import UI

class HazedHollow:
    def __init__(self, ui: UI):
        self.ui = ui
        self.quests_completed = {
            'andrew': False,
            'zach': False,
            'gaaret': False,
            'riley': False,
            'eli': False,
        }
        self.hazeion_summoned = False
        
    def draw(self, screen: pygame.Surface):
        """Draw Hazed Hollow area"""
        screen.fill((100, 100, 120))  # Foggy grey
        
        # Draw fog overlay
        fog_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        fog_surface.fill((150, 150, 180, 100))
        screen.blit(fog_surface, (0, 0))
        
    def get_npc_dialogue(self, npc_name: str) -> str:
        """Get dialogue for NPCs in Hazed Hollow"""
        dialogues = {
            'andrew': "ANDREW: You dare challenge me? I will silence you with the Haze of Compliance!",
            'zach': "ZACH: My songs will lure you into eternal static... listen to the Discordant Chord!",
            'gaaret': "GAARET: My cube algorithms predict your every move. Can you solve the Cube Trap?",
            'riley': "RILEY: I weave webs of desire, but you will find only Reagan's Rejection.",
            'eli': "ELI: My mech of cubes will crush you! Prepare for the Cube Missile!",
            'reagan': "REAGAN: I cannot be captured, but I can give you the Correction Letter for Riley.",
        }
        return dialogues.get(npc_name, "A foggy figure stands before you.")
        
    def complete_quest(self, npc_name: str) -> bool:
        """Mark a quest as complete and return True if all are done"""
        if npc_name in self.quests_completed:
            self.quests_completed[npc_name] = True
            return all(self.quests_completed.values())
        return False
        
    def can_summon_hazeion(self) -> bool:
        """Check if Hazeion can be summoned"""
        return all(self.quests_completed.values()) and not self.hazeion_summoned