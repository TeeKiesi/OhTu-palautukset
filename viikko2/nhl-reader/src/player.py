class Player:
    def __init__(self, dicti):

        self.name = dicti['name']
        self.nationality = dicti['nationality']
        self.assists = dicti['assists']
        self.goals = dicti['goals']
        self.team = dicti['team']
        self.games = dicti['games']
        self.pisteet = self.assists + self.goals

    def __str__(self):
        pelaaja = f"{self.name:20} {self.team:15} {self.assists:3} + {self.goals:3} = {self.pisteet}"
        return pelaaja

    def dosomething(self):
        print("Doing something")
