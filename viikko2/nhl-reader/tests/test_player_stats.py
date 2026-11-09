import unittest

from player import Player
from player_stats import PlayerStats


class StubReader:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


def player(name, team, goals, assists, nationality):
    return Player({
        "name": name,
        "team": team,
        "goals": goals,
        "assists": assists,
        "games": 1,
        "nationality": nationality,
    })


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.players = [
            player("Mikko Rantanen", "DAL", 9, 12, "FIN"),
            player("Jason Robertson", "DAL", 9, 10, "USA"),
            player("Sebastian Aho", "CAR", 10, 5, "FIN"),
            player("Teuvo Teravainen", "CAR", 2, 20, "FIN"),
        ]
        self.stats = PlayerStats(StubReader(self.players))

    def test_top_scorers_by_nationality_returns_only_players_of_given_nationality(self):
        scorers = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(len(scorers), 3)
        for scorer in scorers:
            self.assertEqual(scorer.nationality, "FIN")

    def test_top_scorers_by_nationality_orders_by_points_descending(self):
        scorers = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(
            [scorer.name for scorer in scorers],
            ["Teuvo Teravainen", "Mikko Rantanen", "Sebastian Aho"],
        )

    def test_top_scorers_by_team_returns_only_players_of_given_team(self):
        scorers = self.stats.top_scorers_by_team("CAR")

        self.assertEqual(len(scorers), 2)
        for scorer in scorers:
            self.assertEqual(scorer.team, "CAR")

    def test_top_scorers_by_team_orders_by_points_descending(self):
        scorers = self.stats.top_scorers_by_team("CAR")

        self.assertEqual(
            [scorer.name for scorer in scorers],
            ["Teuvo Teravainen", "Sebastian Aho"],
        )

    def test_top_goal_scorers_returns_requested_amount(self):
        scorers = self.stats.top_goal_scorers(2)

        self.assertEqual(len(scorers), 2)

    def test_top_goal_scorers_orders_by_goals_descending(self):
        scorers = self.stats.top_goal_scorers(2)

        self.assertEqual(
            [scorer.name for scorer in scorers],
            ["Sebastian Aho", "Mikko Rantanen"],
        )


if __name__ == "__main__":
    unittest.main()
