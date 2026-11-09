class Player:  # pylint: disable=too-few-public-methods
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.team = player_dict['team']
        self.goals = player_dict['goals']
        self.assists = player_dict['assists']
        self.games = player_dict['games']
        self.nationality = player_dict['nationality']
        self.points = player_dict['goals'] + player_dict['assists']

    def __str__(self):
        return f"{self.name:<22}{self.team:<16}{self.goals} + {self.assists} = {self.points}"
