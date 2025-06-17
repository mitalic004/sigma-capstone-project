import random

# Set Player stats
player = {
    "HP": 100,
    "ATK": 10,
    "DEF": 20,
    "Buff_ATK": 0,
    "Buff_DEF": 0
}

# Set Dragon stats
dragon = {
    "HP": 100,
    "ATK": 25,
    "DEF": 20,
}


def display_status():
    """
    Display player and dragon status in a readable format.
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


def chara_heal(chara, roll):
    """
    Calculates and returns the healing amount for a character.
    """

    heal = roll * 5
    chara["HP"] += heal
    if chara["HP"] > 100:
        heal -= chara["HP"] - 100
        chara["HP"] = 100

    return heal


# Loop for the main game
def main_game():
    """
    The main game which involves the player and dragon taking turns to act.
    """

    # Set outcome variable to be returned
    end = 0

    # Loop for fight
    while True:
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
        # Player attacks the dragon
        elif action == 1:
            # Roll dice for player
            roll = random.randint(1, 6)
            print(f'\nYou rolled a {roll}.')
            # Calculate damage
            dmg = player["ATK"] * roll
            dmg -= dragon["DEF"]
            # Display outcome, no damage dealt if less than dragon defence
            print("\nYou attacked the dragon.")
            if dmg <= 0:
                print(
                    f'The dragon defended itself! You dealt no damage.')
            else:
                dragon["HP"] -= dmg
                # Set dragon HP to 0 if negative
                if dragon["HP"] < 0:
                    dragon["HP"] = 0
                print(
                    f'You dealt {dmg} damage! The dragon\'s HP is {dragon["HP"]}.')
        # Player heals themselves
        elif action == 2:
            if player["HP"] == 100:
                # Display outcome
                print("\nYou healed yourself.")
                print(
                    f'\nYou are already at max HP! No HP was restored.')
            else:
                # Roll dice for player
                roll = random.randint(1, 6)
                print(f'\nYou rolled a {roll}.')
                # Calculate healing, cannot go over max 100 HP
                heal = chara_heal(player, roll)
                # Display outcome
                print("\nYou healed yourself.")
                print(
                    f'\n{heal} HP was restored! You now have {player["HP"]} HP.')
        # Player buffs their attack
        elif action == 3:
            player["Buff_ATK"] = 3
            player["ATK"] = 15
            print(
                "\nYou increased your attack by 5 points! \nThis effect lasts for 2 turns.")
        # Player buffs their defence
        elif action == 4:
            player["Buff_DEF"] = 3
            player["DEF"] = 40
            print(
                "\nYou increased your defence by 10 points! \nThis effect lasts for 2 turns.")

        # Breaks loop if dragon is defeated, player wins
        if dragon["HP"] == 0:
            end = 1
            break

        # Dragon Turn
        print("\nIt is the dragon's turn.")

        # Randomise dragon attack, more likely to do less damaging attacks
        action = random.randint(1, 7)
        print(f'Dragon action: {action}')
        if action < 7:
            roll = random.randint(1, 10)
            print(f'Dragon roll: {roll}')
            # Calculate damage if dragon attacks
            if action < 4:
                print("\nThe dragon attacked you with a tail swipe.")
                dmg = dragon["ATK"] + roll
            elif action < 6:
                print("\nThe dragon attacked you with a claw scratch.")
                dmg = dragon["ATK"] + roll * 2
            elif action == 6:
                print("\nThe dragon attacked you with fire breath.")
                dmg = dragon["ATK"] + roll * 3

            # Display outcome, no damage dealt if less than player defence
            dmg -= player["DEF"]
            if dmg <= 0:
                print(
                    f'You defended yourself! The dragon dealt no damage.')
            else:
                player["HP"] -= dmg
                # Set dragon HP to 0 if negative
                if player["HP"] < 0:
                    player["HP"] = 0
                print(
                    f'The dragon dealt {dmg} damage! Your HP is {player["HP"]}.')
        else:
            print("\nThe dragon healed itself.")
            if dragon["HP"] == 100:
                # Display outcome
                print(
                    f'\nThe dragon was already at max HP! No HP was restored.')
            else:
                # Calculate healing, cannot go over max 100 HP
                roll = random.randint(1, 6)
                heal = chara_heal(dragon, roll)
                # Display outcome
                print(
                    f'\nThe dragon restored {heal} HP! The dragon now has {dragon["HP"]} HP.')

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
