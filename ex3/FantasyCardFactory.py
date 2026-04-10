from .CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random
from ex0.Card import Rarity


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power=None) -> CreatureCard:
        return CreatureCard("Dragon", 5, Rarity.COMMON, 7, 5)

    def create_spell(self, name_or_power=None) -> SpellCard:
        return SpellCard("Fireball", 3, Rarity.LEGENDARY, "damage")

    def create_artifact(self, name_or_power=None) -> ArtifactCard:
        return ArtifactCard("Mana Ring", 2, Rarity.RARE, 5, "+1 mana")

    def create_themed_deck(self, size) -> dict:
        deck = []
        for _ in range(size):
            deck.append(
                random.choice(
                    [
                        self.create_creature(),
                        self.create_spell(),
                        self.create_artifact(),
                    ]
                )
            )
        return {"deck": deck}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }
