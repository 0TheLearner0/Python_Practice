import random
def get_choices():
    player_choice=input("Enter your choice(Rock, Paper, Scissor): ")
    options=['Rock','Paper','Scissor'] #List 
    computer_choice=random.choice(options)


   # Dictionaries
    choices ={"player": player_choice, "computer": computer_choice}
    return choices
    


def check_Win(player, computer):
    if player==computer:
        return "It's a Tie"
    elif player=="Rock":
        if computer=="Paper":
            return "Paper covers the rock: You lose"
        else:
            return "Rock Smashes the Scissor. You Win!"
    elif player=="Paper":
        if computer=="Scissor":
            return "Scissor cuts paper. You Lose"
        else:
            return "Paper covers the Rock. U win."
    elif player=="Scissor":
        if computer=="Rock":
            return "Rock smashes the Scissor. You Lose"
        else:
            return "Scissor cuts the paper. U win."


choices= get_choices()
print(choices)
result=check_Win(choices["player"], choices["computer"])
print(result)

    
    
    
    
        

#List
#   food=["Pizza","Bread Butter","Stake"]