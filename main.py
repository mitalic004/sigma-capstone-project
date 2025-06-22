import random

# Set Knight stats
knight = {
    "Name": "Knight",
    "HP": 100,
    "Max_HP": 100,
    "ATK": 10,
    "DEF": 20,
    "Buff_ATK": 0,
    "Actions": ["1. Attack the dragon.", "2. True Strike (Special Attack).", "3. Increase attack for 2 turns.", "4. Flee."]
}

# Set Warrior stats
warrior = {
    "Name": "Warrior",
    "HP": 100,
    "Max_HP": 100,
    "ATK": 5,
    "DEF": 25,
    "Buff_DEF": 0,
    "Actions": ["1. Attack the dragon.", "2. Berserk Charge. (Special Attack)", "3. Taunt the dragon and increase defence for 2 turns.", "4. Flee."]
}

# Set Mage stats
mage = {
    "Name": "Mage",
    "HP": 100,
    "Max_HP": 100,
    "ATK": 8,
    "DEF": 15,
    "LUCK": 0,
    "Buff_LUCK": 0,
    "Actions": ["1. Attack the dragon.", "2. Heal the party.", "3. Increase the party's luck for 2 turns. (Skip next turn.)", "4. Flee."]
}

# Set Dragon stats
dragon = {
    "Name": "Dragon",
    "HP": 1000,
    "Max_HP": 1000,
    "ATK": 25,
    "DEF": 25,
}

# Set Party list
party = [knight, warrior, mage]


def display_status():
    """
    Display party and dragon status in a readable format.
    """

    # Party Status
    party_stats_chara = ""
    party_stats_hp = ""
    party_stats_atk = ""
    party_stats_def = ""

    # Adds all characters in party to display
    for ch in party:
        if ch is party[-1]:
            party_stats_chara += ch["Name"]
            party_stats_hp += f'HP: {ch["HP"]}'
            party_stats_atk += f'ATK: {ch["ATK"]}'
            party_stats_def += f'DEF: {ch["DEF"]}'
        else:
            party_stats_chara += f' {ch["Name"]}\t|'
            party_stats_hp += f' HP: {ch["HP"]}\t|'
            party_stats_atk += f' ATK: {ch["ATK"]}\t|'
            party_stats_def += f' DEF: {ch["DEF"]}\t|'

    # Calculate width and generate separating lines
    width = len(party_stats_hp)
    # separator = "\n=="
    # for i in width:
    #     separator += "="
    # separator += "\n"

    # Display Party Status
    # print(separator)
    print("==".center(width, "=") + "\n")
    print("~ Party Status ~".center(width, "~") + "\n")
    print(party_stats_hp)
    print(party_stats_atk)
    print(party_stats_def + "\n")
    print("-".center(width, "-") + "\n")

    # Display Dragon Status
    dragon_stats = f' HP: {dragon["HP"]} \n ATK: {dragon["ATK"]} \n DEF: {dragon["DEF"]} \n'
    print("~ Dragon Status ~".center(len(dragon_stats), "~") + "\n")
    print(dragon_stats + "\n")
    # print(separator)
    print("==".center(width, "=") + "\n")


# Character Action Functions


def party_luck(roll):
    """
    Check if party luck is buffed and add to character roll.
    """

    if mage["LUCK"] != 0:
        print(f'Luck boost is active!')
        roll += mage["LUCK"]

    return roll


def chara_heal(chara, roll):
    """
    Calculate and return the healing amount for characters.
    """

    # Roll dice for character
    roll = random.randint(1, 6)
    print(f'\n{chara["Name"]} rolled a {roll}.')
    heal = roll * 5
    heal_list = []

    # Checks which character is healing
    if chara == dragon:
        heal_list += dragon
        print(f'\n{chara["Name"]} healed itself.')
    else:
        # Mage heals all characters in the party
        heal_list += party
        print(f'\n{chara["Name"]} healed the party.')

    # Calculates healing for characters
    for ch in heal_list:
        if ch["HP"] == ch["Max_HP"]:
            # Display outcome if character is already at max hp
            print(
                f'\n{ch["Name"]} is already at max HP! No HP was restored.')
        else:
            # Calculate healing, cannot go over max HP
            ch["HP"] += heal
            if ch["HP"] > ch["Max_HP"]:
                heal -= ch["HP"] - ch["Max_HP"]
                ch["HP"] = ch["Max_HP"]

            # Display outcome
            print(
                f'\n {ch["Name"]} restored {heal} HP! {ch["Name"]} now has {ch["HP"]} HP.')


def party_atk(chara):
    """
    Calculate and return damage for a basic attack done by one of the party members.
    """

    # Roll dice for character
    roll = random.randint(1, 6)
    print(f'\n{chara["Name"]} rolled a {roll}.')
    roll = party_luck(roll)

    # Calculate damage
    dmg = chara["ATK"] * roll
    dmg -= dragon["DEF"]

    print(f'\n{chara["Name"]} attacked the dragon.')

    return dmg


def party_damage(chara, dmg):
    """
    Display damage dealt to Dragon by one of the party members.
    """

    # Display outcome, no damage dealt if less than dragon defence
    if dmg <= 0:
        print(
            f'The dragon defended itself! {chara["Name"]} dealt no damage.')
    else:
        dragon["HP"] -= dmg
        # Set dragon HP to 0 if negative
        if dragon["HP"] < 0:
            dragon["HP"] = 0
        print(
            f'{chara["Name"]} dealt {dmg} damage! The dragon\'s HP is {dragon["HP"]}.')


def knight_atk():
    """
    Calculate and return damage for a special attack done by Knight.
    """

    # Roll dice for character
    roll = random.randint(1, 6)
    print(f'\n{knight["Name"]} rolled a {roll}.')
    roll = party_luck(roll)

    # Calculate damage
    dmg = (knight["ATK"] + 5) * roll
    dmg -= dragon["DEF"]

    print(f'\n{knight["Name"]} used True Strike to attack the dragon.')

    return dmg


def warrior_atk():
    """
    Calculate and return damage for a special attack done by Warrior.
    """

    # Roll dice for character
    roll = random.randint(1, 6)
    print(f'\n{warrior["Name"]} rolled a {roll}.')
    roll = party_luck(roll)

    # Calculate damage
    dmg = warrior["DEF"] + (roll * 10)
    dmg -= dragon["DEF"]

    print(f'\n{warrior["Name"]} used Berserk Charge to attack the dragon.')

    return dmg


def dragon_target():
    """
    Calculates which party member to target during a dragon attack.
    """

    if warrior["Buff_DEF"] != 0:
        target = random.randint(1, 5)
    else:
        target = random.randint(1, 3)

    if target == 1:
        target_chara = knight
    elif target == 2:
        target_chara = mage
    else:
        target_chara = warrior

    return target_chara


def dragon_atk():
    """
    Calculate and return damage for all attacks from Dragon.
    """

    # Randomise dragon attack, more likely to do less damaging attacks
    action = random.randint(1, 6)
    roll = random.randint(1, 10)
    party_hit = []
    # Calculate damage if dragon attacks
    if action < 4:
        party_hit += party
        print("\nThe dragon attacked the party with a tail swipe.")
        dmg = dragon["ATK"] + roll
    elif action < 6:
        party_hit += dragon_target()
        print(
            f'\nThe dragon attacked {party_hit[0]["Name"]} with a claw scratch.')
        dmg = dragon["ATK"] + roll * 2
    elif action == 6:
        party_hit += party
        print("\nThe dragon attacked the party with fire breath.")
        dmg = dragon["ATK"] + roll * 3

    # Display outcome, no damage dealt if less than character defence
    for chara in party_hit:
        dmg -= chara["DEF"]
        if dmg <= 0:
            print(
                f'{chara["Name"]} defended against the attack! The dragon dealt no damage.')
        else:
            chara["HP"] -= dmg
            # Set character HP to 0 if negative
            if chara["HP"] < 0:
                chara["HP"] = 0
            print(
                f'The dragon dealt {dmg} damage to {chara["Name"]}! Their HP is {chara["HP"]}.')


def chara_buff(chara):
    """
    Check and updates buff duration for a character.
    """

    # Check Knight buff effect duration
    if chara == knight:
        if knight["Buff_ATK"] != 0:
            knight["Buff_ATK"] -= 1
            if knight["Buff_ATK"] == 0:
                print(f'\n{knight["Name"]}\'s attack buff has expired.')
                knight["ATK"] = 10

    # Check Warrior buff effect duration
    if chara == warrior:
        if warrior["Buff_DEF"] != 0:
            warrior["Buff_DEF"] -= 1
            if warrior["Buff_DEF"] == 0:
                print(f'\n{warrior["Name"]}\'s defence buff has expired.')
                warrior["DEF"] = 25

    # Check Mage buff effect duration
    if chara == mage:
        if mage["Buff_LUCK"] != 0:
            mage["Buff_LUCK"] -= 1
            if mage["Buff_LUCK"] == 0:
                print(f'\n{mage["Name"]}\'s luck buff has expired.')
                mage["LUCK"] = 0


def add_buff(chara):
    """
    Applies a buff depending on the character.
    """

    # Knight buffs their attack
    if chara == knight:
        knight["Buff_ATK"] = 3
        knight["ATK"] = 15
        print(
            f'\n{knight["Name"]} used Blessed Sword! \n{knight["Name"]} increased their attack by 5 points! \nThis effect lasts for 2 turns.')

    # Warrior buffs their defence
    if chara == warrior:
        warrior["Buff_DEF"] = 3
        warrior["DEF"] = 30
        print(
            f'\n{warrior["Name"]} used Stalwart Guardian! \n{warrior["Name"]} taunted the dragon and increased their defence by 5 points! \nThis effect lasts for 2 turns.')

    # Mage buffs party luck
    if chara == mage:
        mage["Buff_LUCK"] = 3
        mage["LUCK"] = 3
        print(
            f'\n{mage["Name"]} used Fortune\'s Favour! \n{mage["Name"]} increased the party\'s luck by 3 points! \nThis effect lasts for 2 turns. \n{mage["Name"]} will skip their next turn.')


# Loop for the main game
def main_game():
    """
    The main game which involves the party and dragon taking turns to act.
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
        while action not in [1, 2, 3, 4]:
            try:
                action = int(input(
                    "1. Attack the dragon. \n2. Heal yourself. \n3. Increase your attack for 3 turns. \n4. Increase your defence for 3 turns. \n5. Flee. \n"))
            except ValueError:
                action = 0

            if action == 0 or action not in [1, 2, 3, 4, 5]:
                print("\nThat is not an option. Please enter a valid option.")

        # Breaks loop if player chooses to Flee
        if action == 5:
            end = 3
            break
        # Player attacks Dragon
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
                "\nYou increased your attack by 5 points! \nThis effect lasts for 3 turns.")
        # Player buffs their defence
        elif action == 4:
            player["Buff_DEF"] = 3
            player["DEF"] = 30
            print(
                "\nYou increased your defence by 10 points! \nThis effect lasts for 3 turns.")
        # Breaks loop if dragon is defeated, player wins
        if dragon["HP"] == 0:
            end = 1
            break

        # Dragon Turn
        print("\nIt is the dragon's turn.")

        # Randomise dragon attack, more likely to do less damaging attacks
        action = random.randint(1, 7)
        if action < 7:
            roll = random.randint(1, 10)
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
print("\n~~~~~~~~~~~~~~~ Defeat the Dragon ~~~~~~~~~~~~~~~\n")
print("You are on a quest to defeat a mighty dragon.")
print("After a long and difficult journey, it is time for the final battle.")

end = main_game()

# Display end of fight
if end == 1:
    print("\nYou won! You have defeated the dragon.\n")
elif end == 2:
    print("\nYou lost. The dragon has defeated you.\n")
elif end == 3:
    print("\nYou... fled? The dragon was confused. No one was defeated.\n")
