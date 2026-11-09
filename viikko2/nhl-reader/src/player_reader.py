import requests
from player import Player


class PlayerReader:  # pylint: disable=too-few-public-methods
    def __init__(self, url):
        self._url = url

    def get_players(self):
        response = requests.get(self._url, timeout=10)
        data = response.json()

        if not response.ok or not isinstance(data, list):
            raise ValueError(f"Tilastoja ei löytynyt osoitteesta {self._url}")

        players = []

        for player_dict in data:
            player = Player(player_dict)
            players.append(player)

        return players
