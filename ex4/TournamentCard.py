from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from ex0.Card import Rarity


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int,
                 rarity: Rarity, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_state: dict) -> dict:
        return {"played": self.name}

    def attack(self, target: Card) -> dict:
        return {"attacker": self.name, "target": target.name}

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage
        return {"remaining_health": self.health}

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_power, "health": self.health}

    def calculate_rating(self) -> int:
        self.rating = 1200 + self.wins * 16 - self.losses * 16
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {"wins": self.wins, "losses": self.losses,
                "rating": self.rating}

    def get_tournament_stats(self) -> dict:
        return self.get_rank_info()
