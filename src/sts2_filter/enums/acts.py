from enum import StrEnum

class Act(StrEnum):
    OVERGROWTH = "ACT.OVERGROWTH"
    UNDERDOCKS = "ACT.UNDERDOCKS"
    HIVE = "ACT.HIVE"
    GLORY = "ACT.GLORY"

    @classmethod
    def from_json(cls, value: str) -> "Act | str":
        try:
            return cls(value)
        except ValueError:
            return value
        
    def __str__(self) -> str:
        return self.name