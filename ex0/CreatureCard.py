from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be positive int")
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health must be positive int")
        super().__init__(name, cost, rarity)
        self.type = "Creature"
        self.attack = attack
        self.health = health

    def get_card_info(self):
        info = super().get_card_info()
        info["type"] = self.type
        info["Attack"] = self.attack
        info["Health"] = self.health
        return info

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target: "CreatureCard") -> dict:
        target.health -= self.attack
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": target.health <= 0,
        }
