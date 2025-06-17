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
    "DEF": 20,
}


# Display player and dragon status
def display_status():
    """
    Displays player and dragon status in a readable format.
    """

    # Player Status
    print("========================================")
    print("\n~~~~~ Your Status: ~~~~~~\n")
    print(
        f'HP: {player["HP"]} \nATK: {player["ATK"]} \nDEF: {player["DEF"]} \n')
    print("----------------------------------------")

    # Dragon Status
    print("\n~~~~~ Dragon's Status: ~~~~~\n")
    print(
        f'HP: {dragon["HP"]} \nATK: {dragon["ATK"]} \nDEF: {dragon["DEF"]} \n')
    print("========================================")


# Loop for the main game
def main_game():
    """
    The main game which involves the player and dragon taking turns to act.
    """

    # Set outcome variable to be returned
    end = 0

    # Set condition for continuing fight
    if player["HP"] != 0 or dragon["HP"] != 0:
        fight = True

    # Loop for fight
    while fight:
        # Player Turn
        print("\nIt is your turn.\n")

        display_status()

        # Check buff effect duration
        if player["Buff_ATK"] != 0:
            player["Buff_ATK"] -= 1
            if player["Buff_ATK"] == 0:
                print("\nYour attack buff has expired.")
                player["ATK"] = 10

        if player["Buff_DEF"] != 0:
            player["Buff_DEF"] -= 1
            if player["Buff_DEF"] == 0:
                print("\nYour defence buff has expired.")
                player["DEF"] = 30

        print("\nChoose your action: ")
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

        # Breaks loop if player chooses to Flee
        if action == 5:
            end = 3
            break
        # If player chooses action which needs a dice roll
        elif action == 1:
            pass
        elif action == 2:
            pass
        # If player chooses action which does not need a dice roll
        elif action == 3:
            player["Buff_ATK"] = 3
            player["ATK"] = 15
            print(
                "\nYou have increased your attack by 5 points! This effect lasts for 2 turns.")
        elif action == 4:
            player["Buff_DEF"] = 3
            player["DEF"] = 40
            print(
                "\nYou have increased your defence by 10 points! This effect lasts for 2 turns.")

        # Breaks loop if dragon is defeated, player wins
        if dragon["HP"] == 0:
            end = 1
            break

        # Dragon Turn
        print("\nIt is the dragon's turn.")

        # Breaks loop if player is defeated, dragon wins
        if player["HP"] == 0:
            end = 2
            break

    return end


# Main Game
print("\n~~~~~~~~~~ Defeat the Dragon ~~~~~~~~~~\n")
print("You are on a quest to defeat a mighty dragon.")
print("After a long and difficult journey, it is time for the final battle.")

end = main_game()

# Display end of fight
if end == 1:
    print("\nYou won! You have defeated the dragon.")
elif end == 2:
    print("\nYou lost. The dragon has defeated you.")
elif end == 3:
    print("\nYou... fled? The dragon was confused. No one was defeated.")
