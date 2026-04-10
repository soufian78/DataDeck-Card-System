from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        played = []
        mana_used = 0

        for card in sorted(hand, key=lambda c: c.cost):
            if card.cost <= 5:
                played.append(card.name)
                mana_used += card.cost

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": len(played) * 2,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(available_targets)
