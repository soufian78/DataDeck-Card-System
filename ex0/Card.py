from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = "common"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: Rarity) -> None:
        if not isinstance(rarity, Rarity):
            raise ValueError("rarity must be a Rarity enum")
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {"name": self.name, "cost": self.cost,
                "rarity": self.rarity.value}

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
