class PlayerStats:
    def __init__(self, player_reader):
        self._player_reader = player_reader

    def top_scorers_by_nationality(self, nationality):
        players = self._player_reader.get_players()

        players_from_nationality = [
            player for player in players if player.nationality == nationality
        ]

        players_from_nationality.sort(key=lambda player: player.points, reverse=True)

        return players_from_nationality

    def top_scorers_by_team(self, team):
        players = self._player_reader.get_players()

        players_from_team = [player for player in players if player.team == team]

        players_from_team.sort(key=lambda player: player.points, reverse=True)

        return players_from_team

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa maalimäärän mukaan laskevassa järjestyksessä"""
        players = self._player_reader.get_players()

        players.sort(key=lambda player: player.goals, reverse=True)

        return players[:how_many]
