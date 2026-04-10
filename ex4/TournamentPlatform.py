from ex4.TournamentCard import TournamentCard

import uuid


class TournamentPlatform:

    def __init__(self):
        self.cards = {}
        self.matches = 0

    def register_card(self, card: TournamentCard) -> str:
        cid = str(uuid.uuid4())
        self.cards[cid] = card
        return cid

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1: TournamentCard = self.cards[card1_id]
        c2: TournamentCard = self.cards[card2_id]

        winner = c1 if c1.attack_power > c2.attack_power else c2
        loser = c1 if winner == c2 else c2

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches += 1
        return {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> list:
        return sorted(
            [(c.name, c.calculate_rating()) for c in self.cards.values()],
            key=lambda x: x[1],
            reverse=True,
        )

    def generate_tournament_report(self) -> dict:
        return {"total_cards": len(self.cards), "matches_played": self.matches}
