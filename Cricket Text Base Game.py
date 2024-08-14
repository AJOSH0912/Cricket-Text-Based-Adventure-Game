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

    def choose_team_strength(self): #To choose your team strength
        while True:
            print("\nChoose your team's strength:") 
            print("1. Batting")
            print("2. Bowling")
            choice = input("Enter 1 or 2: ").strip() # Takes the input from the user
            if choice in ['1', '2']:
                self.player_strength = 'batting' if choice == '1' else 'bowling'
                break # Breaks the loop if the input is valid
            print("Invalid input, please choose 1 or 2.")
        print(f"Your team is known for its {self.player_strength}.")

    def set_batting_order(self): #TO choose you batsmen only for top 3 though because i
        print("\nSet your team's batting order. Choose your top 3 batsmen:")
        for i in range(1, 4): # Loop to take the input from the user
            player = input(f"Enter name of Batsman {i}: ").strip()
            self.player_batting_order.append(player) # adds the player to the batting order which is a list above
        self.player_batting_order += [f"Player {i}" for i in range(4, 12)]
        print(f"Your batting order is set as: {', '.join(self.player_batting_order[:3])}, and others.")
        self.player_scores = {player: 0 for player in self.player_batting_order} # Sets the score of each player to 0
        self.opponent_scores = {player: 0 for player in self.opponent_batting_order} # Sets the score of each player to 0 in the oother batting team

    def toss(self): #For the coin toss to decide who is going to bat or bowl fuirst
        print("\nTossing the coin...")
        toss_outcome = random.choice(['win', 'lose'])
        if toss_outcome == 'win':
            while True:
                choice = input("You won the toss! Do you want to bat or bowl first? (bat/bowl): ").lower().strip()
                if choice in ['bat', 'bowl']:
                    self.player_batting = True if choice == 'bat' else False
                    break
                print("Invalid input, please choose 'bat' or 'bowl'.")