from dataclasses import dataclass

from sts2_filter.enums.characters import Character
from sts2_filter.enums.relics import Relic


@dataclass
class Player:
    character: Character | None = None
    relics: list | None = None
    deck: list | None = None
    badges: list | None = None
    potions: list | None = None
    potion_slots: int = 0

    
    @classmethod
    def from_json(cls, data: dict):
        return cls(
            character = Character(data.get("character")),
            potion_slots = data.get("max_potion_slot_count"),
            potions = data.get("potions"),
            badges = data.get("badges"),
            deck = data.get("deck"),
            relics = data.get("relics")
        )
    
    def __repr__(self):
        return(
            f"\nCharacter: {self.character}\n"
            f"Potion Slots: {self.potion_slots}\n"
            f"Potions: {self.potions}\n"
            f"Badges: {self.badges}\n"
            f"Relic Count: {len(self.relics)}\n"
            f"Relics: {self.relics}\n"
            f"Deck Size: {len(self.deck)}\n"
            f"Deck: {self.deck}\n\n"
        )