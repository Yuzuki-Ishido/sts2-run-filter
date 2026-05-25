# enum file containing all cards in sts2, separated by color
# modeling the game's categorization

from enum import StrEnum

class CardID(StrEnum):
    """Base type for all Card IDs."""
    pass


class RedCard(CardID):
    STRIKE = "STRIKE_IRONCLAD"
    DEFEND = "DEFEND_IRONCLAD"
    BASH = "BASH"

class GreenCard(CardID):
    STRIKE = "STRIKE_SILENT"
    DEFEND = "DEFEND_SILENT"
    NEUTRALIZE = "NEUTRALIZE"
    SURVIVOR = "SURVIVOR"

class OrangeCard(CardID):
    STRIKE = "STRIKE_REGENT"
    DEFEND = "DEFEND_REGENT"
    FALLING_STAR = "FALLING_STAR"
    VENERATE = "VENERATE"

class PinkCard(CardID):
    STRIKE = "STRIKE_NECROBINDER"
    DEFEND = "DEFEND_NECROBINDER"
    UNLEASH = "UNLEASH"
    BODYGUARD = "BODYGUARD"

class BlueCard(CardID):
    STRIKE = "STRIKE_DEFECT"
    DEFEND = "DEFEND_DEFECT"
    ZAP = "ZAP"
    DUALCAST = "DUALCAST"
