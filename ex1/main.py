from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex0.Card import Rarity


def main():
    print("\n=== DataDeck Deck Builder ===\n")
    spell = SpellCard("Lightning Bolt", 3, Rarity.LEGENDARY, "damage")
    Artifact = ArtifactCard("Mana Crystal", 2, Rarity.EPIC, 10, 5)
    creature = CreatureCard("Fire Dragon", 5, Rarity.COMMON, 7, 5)
    D = Deck()
    D.add_card(spell)
    D.add_card(Artifact)
    D.add_card(creature)
    print(f"Deck stats: {D.get_deck_stats()}\n")
    print("Drawing and playing cards:")
    while D.cards:
        dct = {}
        DC = D.draw_card()
        if isinstance(DC, SpellCard):
            card = "Spell"
        elif isinstance(DC, ArtifactCard):
            card = "Artifact"
        elif isinstance(DC, CreatureCard):
            card = "Creature"
        print(f"Drew: {DC.name} ({card})")
        print(f"Play result: {DC.play(dct)}\n")
    print("Polymorphism in action: Same interface, different card behaviors!")


main()
