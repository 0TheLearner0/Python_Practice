import random
def get_choices():
    player_choice=input("Enter your choice(Rock, Paper, Scissor): ")
    options=["Rock","Paper","Scissor"]
    computer_choice=random.choices(options)


   # Dictionaries
    choices ={"Player": player_choice, "Computer": computer_choice}
    return choices
choices= get_choices()
print(choices)

#List
#   food=["Pizza","Bread Butter","Stake"]