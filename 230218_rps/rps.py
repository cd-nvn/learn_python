import random

#define a function for getting the choices of the player and the computer
def get_choices():
    player_choice=input("Enter a choice among Rock, Paper, Scissors: \n") #Get input of player choice
    options=["Rock", "Paper", "Scissors"]
    computer_choice=random.choice(options) #Select a random option as computer choice
    choices={"player": player_choice, "computer": computer_choice}
    return choices

#define a function to get the results of the game
def get_results(player,computer):
    print(f"You chose {player}, computer chose {computer}")
    if player==computer:
        return "It's a tie!"
    elif player=="Rock":
        if computer=="Scissors":
            return "Rock smashes Scissors. You win!"
        else:
            return "Paper covers Rock. You lose."
    elif player=="Paper":
        if computer=="Rock":
            return "Paper covers Rock. You win!"
        else:
            return "Scissorrs cut Paper. You lose."
    elif player=="Scissors": 
        if computer=="Paper":
            return "Scissors cut Paper. You win!"
        else:
            return "Rock smashes Scissors. You lose."

choices=get_choices()
result=get_results(choices["player"], choices["computer"])
print(result)