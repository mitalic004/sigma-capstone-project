import random

# Set Player stats
player = {
    "HP": 100,
    "ATK": 10,
    "DEF": 30,
    "Buff_ATK": 0,
    "Buff_DEF": 0
}

# Set Dragon stats
dragon = {
    "HP": 100,
    "ATK": 15,
    "DEF": 30,
}


# Loop for the main game
def main_game(user, enemy):
    if user["HP"] != 0 or enemy["HP"] != 0:
        fight = True

    while fight:
        pass


# Main Game
print("\n~~~~~~~~~~ Defeat the Dragon ~~~~~~~~~~\n")
print("You are on a quest to defeat a mighty dragon.")
print("After a long and difficult journey, it is time for the final battle.\n")
