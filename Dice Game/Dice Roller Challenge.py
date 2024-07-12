import random # allow us to generate random numbers

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

while True:
    players = input("Enter the number of players (2 - 4): ")
    
    if players.isdigit(): #tell us if this is a digit or not (valid number)
        players = int(players) # convert the entered string into an integer
        if (2 <= players <= 4):
            break
        else:
            print ("Must be between 2 - 4 players.")
    else:
            print ("Invalid number of players, try again")

max_score = 50

player_scores = [0 for _ in range(players)] #this block of code essentially puts zero inside of the list for every single player that we have 

game_running = True #check if the gaming is been played 

while max(player_scores) < max_score and game_running: #this block checks if any player has reached the maximum score
    
    for player_idx in range(players): #finding the index of the range of players
        print("\nPlayer", player_idx + 1, "turn has just started")#the next players turn 
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0
    
        while True:
            should_roll = input("Would you like to roll (y) or to exit (e)? ")
            if should_roll.lower() == "e":
                game_running = False
                break
            if should_roll.lower() != "y": #even if the player enters capital Y still we convert it to lower case and let the player play
                break
        
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value 
                print("You rolled a :",value)
            
            print("Your score is:", current_score)
        
        player_scores[player_idx] += current_score
        print("Your total score is:",player_scores[player_idx])
        
        if not game_running:
            break


max_score = max(player_scores)
winning_idx = player_scores.index(max_score)

if game_running:  
    print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)  
else:  
    print("\nGame exited by user. Final scores:") 
    for i in range(players):  
        print(f"Player {i + 1}'s score: {player_scores[i]}") 