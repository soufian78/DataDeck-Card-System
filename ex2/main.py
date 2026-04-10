from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard
from ex0.Card import Rarity


def main():
    print("\n=== DataDeck Ability System ===\n")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")
    print("Playing Arcane Warrior (Elite Card):\n")
    print("Combat phase:")
    trgt = CreatureCard("Enemy", 5, Rarity.COMMON, 7, 5)
    Elit = EliteCard("Arcane Warrior", 5, Rarity.LEGENDARY, 6, 5, 4)
    print(f"Attack result: {Elit.attack(trgt)}")
    print(f"Defense result: {Elit.defend(5)}\n")
    print("Magic phase:")
    print(f"Spell cast: {Elit.cast_spell('Fireball', [['Enemy1', 'Enemy2']])}")
    print(f"Mana channel: {Elit.channel_mana(3)}\n")
    print("Multiple interface implementation successful!")


main()
