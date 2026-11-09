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
