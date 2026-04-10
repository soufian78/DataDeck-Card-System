from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main():
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")
    print(f"Available types: {factory.get_supported_types()}\n")

    print("Simulating aggressive turn...")
    print("Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]\n")
    turn = engine.simulate_turn()
    print(" Turn execution:")
    print(f"Strategy: {turn.pop('strategy')}")
    print(f"Actions: {turn}\n")
    print("Game Report:")
    print(engine.get_engine_status())
    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


main()
