import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),   # 4+12 = 16
            Player("Lemieux", "PIT", 45, 54),  # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53),  # 37+53 = 90
            Player("Yzerman", "DET", 42, 56),  # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)   # 35+89 = 124
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_correct_player_when_found(self):
        player = self.stats.search("Lemieux")

        self.assertEqual(str(player), "Lemieux PIT 45 + 54 = 99")

    def test_search_returns_none_when_player_not_found(self):
        player = self.stats.search("Jagr")

        self.assertEqual(player, None)

    def test_team_returns_players_of_given_team(self):
        players = self.stats.team("EDM")

        names = [player.name for player in players]
        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_returns_empty_list_when_no_players_in_team(self):
        players = self.stats.team("NYR")

        self.assertEqual(players, [])

    def test_top_returns_players_sorted_by_points_by_default(self):
        top = self.stats.top(3)

        names = [player.name for player in top]
        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman", "Kurri"])

    def test_top_returns_players_sorted_by_goals(self):
        top = self.stats.top(3, SortBy.GOALS)

        names = [player.name for player in top]
        self.assertEqual(names, ["Lemieux", "Yzerman", "Kurri", "Gretzky"])

    def test_top_returns_players_sorted_by_assists(self):
        top = self.stats.top(3, SortBy.ASSISTS)

        names = [player.name for player in top]
        self.assertEqual(names, ["Gretzky", "Yzerman", "Lemieux", "Kurri"])


if __name__ == "__main__":
    unittest.main()
