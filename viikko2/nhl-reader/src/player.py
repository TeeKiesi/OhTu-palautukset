class Player:
    def __init__(self, dict):

#        self.pelaaja = for i in dict: string +=
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.id = dict['id']
        self.pisteet = self.assists + self.goals
    
    def __str__(self):
        pelaaja = f"{self.name:20} {self.team:15} {self.assists:3} + {self.goals:3} = {self.pisteet}"
        return pelaaja
