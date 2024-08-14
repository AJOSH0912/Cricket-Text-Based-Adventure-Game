import random

# Stup for the game. This is the main class that will be used to play the game.
class CricketGame:
    def __init__(self):
        # Intialises the game with the following attributes
        self.player_team_score = 0
        self.opponent_team_score = 0
        self.player_wickets = 0
        self.opponent_wickets = 0
        self.overs_played = 0
        self.max_overs = 5 #How many over game it is
        self.powerplay_overs = 2
        self.player_batting = False
        self.player_bowling = False
        self.current_bowler = None
        self.opponent_strength = random.choice(['batting', 'bowling']) # Randomly selects the opponent strength
        self.innings_phase = "Powerplay" 
        self.player_batting_order = []
        self.opponent_batting_order = [f"Opponent Player {i}" for i in range(1, 12)] # 
        self.player_innings_finished = False
        self.opponent_innings_finished = False
        self.player_scores = {}
        self.opponent_scores = {}
        self.commentary = [] # Where all the messages will be stored

    # Start of functions for the game
    def start_game(self):
        print("Welcome to the Ultimate Cricket Match!")
        self.choose_team_strength()
        self.set_batting_order()
        self.toss()