from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def main():
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
    print("CreatureCard Info:")
    print(dragon.get_card_info())
    print()
    dct = dict()
    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable:{dragon.is_playable(6)}")
    print(f"Play result: {dragon.play(dct)}\n")
    goblin = CreatureCard("Goblin Warrior", 5, Rarity.COMMON, 5, 6)
    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {dragon.attack_target(goblin)}\n")
    print("Testing insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}\n")
    print("Abstract pattern successfully demonstrated!")


try:
    main()
except Exception as e:
    print(e)
