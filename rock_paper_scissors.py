# We will write a rock paper scissors game in class - Complete it in this file
import random
player_choice = "rock"
computer_choice = "paper"

# Create a function that gets the choices
def get_choices():
    options = ["rock", "paper", "scizzors"]
    player_choice = "rock"
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

choices = get_choices()
print(choices)