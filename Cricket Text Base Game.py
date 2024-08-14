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

        else: #This is for if you lose toss:(
            print("You lost the toss.")
            self.player_batting = False if self.opponent_strength == 'batting' else True # Makes it so if the opponent is batting you are bowling and vice versa
            print(f"Opponent chose to {'bat' if not self.player_batting else 'bowl'} first.") 

        if self.player_batting:#If you are batting first, starts the batting innings then the bowling innings
            self.batting_innings() 
            self.bowling_innings() 
        else: #If you are bowling first, starts the bowling innings then the batting innings
            self.bowling_innings()
            self.batting_innings()

    def batting_innings(self): 
        print("\nYour team is batting now!")
        self.overs_played = 0 #Keeps count of the overs played. will increase once over is completed
        self.innings_phase = "Powerplay"
        while self.overs_played < self.max_overs and self.player_wickets < 10: #Checks to see if the overs played is less than the max overs and if the player wickets are less than 10, if done it finishes the innings
            self.play_over(batting=True)
            if self.player_team_score > self.opponent_team_score and self.player_bowling: 
                break
            if self.overs_played == self.powerplay_overs: #Checks to see if powerplay is over
                self.innings_phase = "Middle Overs"
        print(f"\nEnd of innings! Your team scored {self.player_team_score} runs with {self.player_wickets} wickets down.") #once Overs_Played is equal to max_overs, the innings is over
        self.player_innings_finished = True #Sets the innings to finished

    def bowling_innings(self): #Similar code as explained above
        print("\nYour team is bowling now!") 
        self.choose_bowler()
        self.overs_played = 0
        self.innings_phase = "Powerplay"
        while self.overs_played < self.max_overs and self.opponent_wickets < 10: #
            self.play_over(batting=False)
            if self.opponent_team_score > self.player_team_score and not self.player_bowling:
                break
            if self.overs_played == self.powerplay_overs:
                self.innings_phase = "Middle Overs"
        print(f"\nEnd of innings! Opponent scored {self.opponent_team_score} runs with {self.opponent_wickets} wickets down.")
        self.opponent_innings_finished = True

    def choose_bowler(self): 
        while True:
            print("\nChoose your bowler:")
            print("1. Fast Bowler")
            print("2. Spinner")
            choice = input("Enter 1 or 2: ").strip() #ask for usre input and stores it in 'choice' which is used in the if statemnt below
            if choice in ['1', '2']:
                self.current_bowler = 'Fast Bowler' if choice == '1' else 'Spinner' #Chooses the bowler based on the input. Only comes to this if they choose 1 or 2
                break
            print("Invalid input, please choose 1 or 2.") 
        print(f"{self.current_bowler} is ready to bowl.")

    def play_over(self, batting): #inherits the batting variable from the function that calls it
        if batting:#Checks if you are batting or not
            self.simulate_batting_over()  
        else:
            self.simulate_bowling_over()
        self.overs_played += 1 #adds 1 to overs played once the function is finished
        print(f"\nEnd of over {self.overs_played}/{self.max_overs}.")
        print(f"Score: {'Your Team' if batting else 'Opponent'} {self.player_team_score if batting else self.opponent_team_score}/{self.player_wickets if batting else self.opponent_wickets}")

        def simulate_batting_over(self): #Simulates the batting over
            for _ in range(6):
                ball_type = random.choice(['fast', 'spin', 'bouncer', 'yorker']) #Randomly chooses the ball type
                print(f"\nBall is a {ball_type}.") 
                while True:
                    shot = input("Choose your shot (defend, drive, pull, loft): ").lower().strip()
                    if shot in ['defend', 'drive', 'pull', 'loft']:
                        break
                print("Invalid input, please choose 'defend', 'drive', 'pull', or 'loft'.")
            outcome = self.get_batting_outcome(ball_type, shot) #Gets the outcome of the ball
            self.process_batting_outcome(outcome, shot) 

    def get_dynamic_weights(self, shot, batting=True):
        if batting:
            if self.innings_phase == "Powerplay":
                return [50, 10, 10, 20, 10] if shot == 'drive' else \
                    [45, 15, 10, 15, 15] if shot == 'pull' else \
                    [40, 5, 20, 25, 10] if shot == 'loft' else \
                    [30, 5, 45, 15, 5]
            else:
                return [40, 10, 10, 25, 15] if shot == 'drive' else \
                    [35, 15, 15, 20, 15] if shot == 'pull' else \
                    [30, 5, 25, 30, 10] if shot == 'loft' else \
                    [25, 5, 50, 15, 5]

    def get_batting_outcome(self, ball_type, shot):
        is_edge_case = random.random() < 0.05  # These are rare events that can happen

        if is_edge_case:
            return random.choice(['wicket', 'no-ball', 'wide'])

        if (ball_type == 'yorker' and shot == 'pull') or \
        (ball_type == 'bouncer' and shot == 'drive') or \
        (ball_type == 'spin' and shot == 'pull') or \
        (ball_type == 'fast' and shot == 'loft'):
            return 'wicket'
        #Basically makes sure that you play the right shot for the right ball. If you play a pull shot for a yorker of course you are going to get out

        weights = self.get_dynamic_weights(shot, batting=True) 
        return random.choices(['runs', 'wicket', 'dot', 'boundary', 'six'], weights=weights)[0] #Chooses the outcome of the ball based on the weights. Factors that influence this is the powerplay and the shot played


            
    def simulate_bowling_over(self):
        for _ in range(6): #Loops through the over
            while True:
                field = input("\nChoose your field placement (aggressive, balanced, defensive): ").lower().strip()
                if field in ['aggressive', 'balanced', 'defensive']:
                    break
                print("Invalid input, please choose 'aggressive', 'balanced', or 'defensive'.")
            bowler_type = input("\nChange bowler? (same/fast/spinner): ").lower().strip()
            if bowler_type in ['fast', 'spinner']:
                self.current_bowler = 'Fast Bowler' if bowler_type == 'fast' else 'Spinner'
            outcome = self.get_bowling_outcome(field)
            self.process_bowling_outcome(outcome, field) 


    #def play(self):
        #self.start_game()
        #self.display_result()

#game = CricketGame()
#game.play()