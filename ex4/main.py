from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from ex0.Card import Rarity


def print_card_info(name: str, cid: str, card: TournamentCard) -> None:
    print(f"{name} (ID: {cid})")
    info = card.get_rank_info()
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {info['rating']}")
    print(f"- Record: {info['wins']}-{info['losses']}\n")


def main():
    print("\n=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")
    trnmnt = TournamentPlatform()
    card1 = TournamentCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 6)
    card2 = TournamentCard("Ice Wizard", 6, Rarity.LEGENDARY, 5, 4)

    id1 = trnmnt.register_card(card1)
    id2 = trnmnt.register_card(card2)
    print_card_info(card1.name, id1, card1)
    print_card_info(card2.name, id2, card2)

    print("Creating tournament match...")
    result = trnmnt.create_match(id1, id2)
    print(f"Match result: {result}\n")

    print("Tournament Leaderboard:")
    leaderboard = trnmnt.get_leaderboard()

    rank = 1
    for name, rating in leaderboard:
        card = next(c for c in trnmnt.cards.values() if c.name == name)
        stats = card.get_rank_info()
        print(
            f"{rank}. {name} - Rating: {rating} ({stats['wins']}"
            f"-{stats['losses']})"
        )
        rank += 1

    report = trnmnt.generate_tournament_report()
    avg = sum(c.calculate_rating()
              for c in trnmnt.cards.values()) // len(trnmnt.cards)
    report["avg_rating"] = avg
    report["platform_status"] = "active"

    print()
    print("Platform Report:")
    print(report)
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


main()
