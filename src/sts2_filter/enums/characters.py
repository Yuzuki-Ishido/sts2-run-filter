# character enum and respective helper functions

from enum import StrEnum

class Character(StrEnum):
    IRONCLAD = "CHARACTER.IRONCLAD"
    SILENT = "CHARACTER.SILENT"
    REGENT = "CHARACTER.REGENT"
    NECROBINDER = "CHARACTER.NECROBINDER"
    DEFECT = "CHARACTER.DEFECT"

    @classmethod
    def from_json(cls, value: str) -> "Character | str":
        try:
            return cls(value)
        except ValueError:
            return value
    
    def __str__(self) -> str:
        return self.name

