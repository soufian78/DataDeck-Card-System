from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.turns = 0
        self.cards_created = 0
        self.total_damage = 0
        self.damge = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        hand = [self.factory.create_creature(), self.factory.create_spell()]
        battlefield = []

        result = self.strategy.execute_turn(hand, battlefield)

        self.turns += 1
        self.cards_created += len(hand)
        self.total_damage += 8

        return result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
