# enum file containing all cards in sts2, separated by color
# modeling the game's categorization

from enum import StrEnum

class RedCard(StrEnum):
    STRIKE = "STRIKE_IRONCLAD"
    DEFEND = "DEFEND_IRONCLAD"
    BASH = "BASH"

class GreenCard(StrEnum):
    STRIKE = "STRIKE_SILENT"
    DEFEND = "DEFEND_SILENT"
    NEUTRALIZE = "NEUTRALIZE"
    SURVIVOR = "SURVIVOR"

class OrangeCard(StrEnum):
    STRIKE = "STRIKE_REGENT"
    DEFEND = "DEFEND_REGENT"
    FALLING_STAR = "FALLING_STAR"
    VENERATE = "VENERATE"

class PinkCard(StrEnum):
    STRIKE = "STRIKE_NECROBINDER"
    DEFEND = "DEFEND_NECROBINDER"
    UNLEASH = "UNLEASH"
    BODYGUARD = "BODYGUARD"

class BlueCard(StrEnum):
    STRIKE = "STRIKE_DEFECT"
    DEFEND = "DEFEND_DEFECT"
    ZAP = "ZAP"
    DUALCAST = "DUALCAST"
