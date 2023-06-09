class Team:
    # points = 0
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player):
        return player in self.players
    
   # extensions
    def play_game(self, win):
        if win:
            self.points += 3
        else:
            self.points = 0


