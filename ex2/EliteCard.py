from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name, cost, rarity, attack, health, mana_pool):
        Card.__init__(self, name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.mana_pool = mana_pool
        self._wins = 0
        self._damage_blocked = 0

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Deal 3 damage to target",
        }

    def attack(self, target: Card) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        armor = self.attack_power // 2
        blocked = min(armor, incoming_damage)
        taken = incoming_damage - blocked
        self.health -= taken
        self._damage_blocked += blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "attack": self.attack_power,
            "health": self.health,
            "damage_blocked": self._damage_blocked,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = len(targets) * 4
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost,
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana_pool += amount
        return {"channeled": amount, "total_mana": self.mana_pool}

    def get_magic_stats(self) -> dict:
        return {"name": self.name, "mana_pool": self.mana_pool}
