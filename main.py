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
    """
    The main game which involves the user and enemy taking turns to act.
    """

    # Set outcome variable to be returned
    end = 0

    # Set condition for continuing fight
    if user["HP"] != 0 or enemy["HP"] != 0:
        fight = True

    # Loop for fight
    while fight:
        print("\nIt is your turn.\n")
        print("Choose your action: ")
        action = 0

        # Loop for validating player input
        while action not in [1, 2, 3, 4, 5]:
            try:
                action = int(input(
                    "1. Attack the dragon. \n2. Heal yourself. \n3. Increase your attack for 2 turns. \n4. Increase your defence for 2 turns. \n5. Flee. \n"))
            except ValueError:
                action = 0

            if action == 0 or action not in [1, 2, 3, 4, 5]:
                print("\nThat is not an option. Please enter a valid option.")

        # If player chooses to Flee
        if action == 5:
            end = 3
            fight = False

    return end


# Main Game
print("\n~~~~~~~~~~ Defeat the Dragon ~~~~~~~~~~\n")
print("You are on a quest to defeat a mighty dragon.")
print("After a long and difficult journey, it is time for the final battle.")

end = main_game(player, dragon)

# Display end of fight
if end == 1:
    print("\nYou won! You have defeated the dragon.")
elif end == 2:
    print("\nYou lost. The dragon has defeated you.")
elif end == 3:
    print("\nYou... fled? The dragon was confused. No one was defeated.")
