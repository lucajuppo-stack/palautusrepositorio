class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.games = dict['games']
        self.nationality = dict['nationality']
        self.points = dict['goals'] + dict['assists']

    def __str__(self):
        return f"{self.name:<22}{self.team:<16}{self.goals} + {self.assists} = {self.points}"
