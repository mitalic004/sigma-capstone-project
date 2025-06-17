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
        print("\nIt is your turn.\n")
        print("Choose your action: ")
        action = 0
        while action not in [1, 2, 3, 4, 5]:
            try:
                action = int(input(
                    "1. Attack the dragon. \n2. Heal yourself. \n3. Increase your attack for 2 turns. \n4. Increase your defence for 2 turns. \n5. Flee. \n"))
            except ValueError:
                action = 0

            if action == 0 or action not in [1, 2, 3, 4, 5]:
                print("\nThat is not an option. Please enter a valid option.")

    return "TEMP"


# Main Game
print("\n~~~~~~~~~~ Defeat the Dragon ~~~~~~~~~~\n")
print("You are on a quest to defeat a mighty dragon.")
print("After a long and difficult journey, it is time for the final battle.")
print(main_game(player, dragon))
