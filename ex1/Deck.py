from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for c in self.cards:
            if c.name == card_name:
                self.cards.remove(c)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        creatures = 0
        spells = 0
        artifacts = 0
        for c in self.cards:
            if isinstance(c, CreatureCard):
                creatures += 1
            elif isinstance(c, SpellCard):
                spells += 1
            elif isinstance(c, ArtifactCard):
                artifacts += 1
        avg_cost = (
            sum(crd.cost for crd in self.cards) / len(self.cards)
            if self.cards else 0
        )
        return {
            "total_cards": len(self.cards),
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(avg_cost, 1),
        }
