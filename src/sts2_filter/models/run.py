# a Run class to store individual runs into individual instances
from dataclasses import dataclass
from sts2_filter.enums.characters import Character
from sts2_filter.enums.acts import Act
from sts2_filter.models.player import Player

@dataclass
class Run:
    acts: list | None = None
    ascension: int = 0
    build_id: str = ""
    players: list | None = None
    victory: bool = False
    floor_reached: int = 0
    seed: str = ""
    win: bool = False
    raw_data: dict | None = None
    

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            players = [Player.from_json(data.get("players")[i]) for i in range(len(data.get("players")))],
            # players = Player.from_json(data.get("players")[0]),
            seed = data.get("seed"),
            acts = [Act.from_json(val) for val in data.get("acts")],
            win = data.get("win")
        )
    
    def __repr__(self):
        return(
            f"Acts: {self.acts}\n"
            f"{'WIN' if self.win else 'LOSS'}\n"
            f"players:\n{self.players}"
        )
