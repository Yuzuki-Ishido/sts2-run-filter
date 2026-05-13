# a Run class to store individual runs into individual instances
from dataclasses import dataclass
from sts2_filter.enums.characters import Character
from sts2_filter.enums.acts import Act

@dataclass
class Run:
    character: Character | None = None
    ascension: int = 0
    victory: bool = False
    floor_reached: int = 0
    seed: str = ""
    build_id: str = ""
    raw_data: dict | None = None
    acts: list | None = None


    def set_seed(self, data: dict):
        self.seed = data.get("seed")

    # @classmethod
    # def set_seed(cls, data: dict):
    #     return cls(
    #         seed = data.get("seed")
    #     )

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            character = data.get("character"),
            seed = data.get("seed"),
            acts = [Act.from_json(val) for val in data.get("acts")]
        )
