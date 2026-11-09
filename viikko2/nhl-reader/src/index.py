from urllib import response

import requests
from player import Player

class PlayerReader:

    def __init__(self, url):
        self.response = requests.get(url).json()
        

    def get_players(self):
        players = []
        
        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)

        return players

class PlayerStats:

    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality):
        pisteytetty = []
        for player in self.players:
            if player.nationality == nationality:
                pisteytetty.append((player.pisteet, player))
                #print(player)
    
        pisteytetty.sort(key=lambda item: item[0])
        print(pisteytetty)
        return pisteytetty

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"

    #print("JSON-muotoinen vastaus:")
#    print(response)
    reader = PlayerReader(url)
    
    pelaajat = reader.get_players()
    stats = PlayerStats(pelaajat)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player[1])
    

    

    

if __name__ == "__main__":
    main()
