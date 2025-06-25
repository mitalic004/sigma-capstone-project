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
    for chara in party:
        if chara is party[-1]:
            party_stats_chara += f"  {chara["Name"]:<7}"
            party_stats_hp += f"  HP: {chara["HP"]:<7}"
            party_stats_atk += f"  ATK: {chara["ATK"]:<7}"
            party_stats_def += f"  DEF: {chara["DEF"]:<7}"
        else:
            party_stats_chara += f"  {chara["Name"]:<7}\t|"
            party_stats_hp += f"  HP: {chara["HP"]:<7}\t|"
            party_stats_atk += f"  ATK: {chara["ATK"]:<7}\t|"
            party_stats_def += f"  DEF: {chara["DEF"]:<7}\t|"

    # Calculate width and generate separating lines
    width = len(party_stats_hp)

    # Display Party Status
    print("==".center(width, "=") + "\n")
    print("~ Party Status ~".center(width, "~") + "\n")
    print(party_stats_chara)
    print("_".center((width), "_") + "\n")
    print(party_stats_hp)
    print(party_stats_atk)
    print(party_stats_def + "\n")
    print("-".center(width, "-") + "\n")

    # Display Dragon Status
    dragon_stats = f"  HP: {dragon["HP"]} \n  ATK: {dragon["ATK"]} \n  DEF: {dragon["DEF"]} \n"
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
        print(f"Luck boost is active!")
        roll += mage["LUCK"]

    return roll


def chara_heal(chara, roll):
    """
    Calculate and return the healing amount for characters.
    """

    # Roll dice for character
    roll = random.randint(1, 6)
    print(f"\n{chara["Name"]} rolled a {roll}.")
    heal = roll * 5
    heal_list = []

    # Checks which character is healing
    if chara == dragon:
        heal_list += dragon
        print(f"\n{chara["Name"]} healed itself.")
    else:
        # Mage heals all characters in the party
        heal_list += party
        print(f"\n{chara["Name"]} healed the party.")

    # Calculates healing for characters
    for chara in heal_list:
        if chara["HP"] == chara["Max_HP"]:
            # Display outcome if character is already at max hp
            print(
                f"\n{chara["Name"]} is already at max HP! No HP was restored.")
        else:
            # Calculate healing, cannot go over max HP
            chara["HP"] += heal
            if chara["HP"] > chara["Max_HP"]:
                heal -= chara["HP"] - chara["Max_HP"]
                chara["HP"] = chara["Max_HP"]

            # Display outcome
            print(
                f"\n {chara["Name"]} restored {heal} HP! {chara["Name"]} now has {chara["HP"]} HP.")


def party_atk(chara):
    """
    Calculate and return damage for a basic attack done by one of the party members.
    """

    # Roll dice for character
    roll = random.randint(1, 6)
    print(f"\n{chara["Name"]} rolled a {roll}.")
    roll = party_luck(roll)

    # Calculate damage
    dmg = chara["ATK"] * roll
    dmg -= dragon["DEF"]

    print(f"\n{chara["Name"]} attacked the dragon.")

    return dmg


def party_damage(chara, dmg):
    """
    Display damage dealt to Dragon by one of the party members.
    """

    # Display outcome, no damage dealt if less than dragon defence
    if dmg <= 0:
        print(
            f"The dragon defended itself! {chara["Name"]} dealt no damage.")
    else:
        dragon["HP"] -= dmg
        # Set dragon HP to 0 if negative
        if dragon["HP"] < 0:
            dragon["HP"] = 0
        print(
            f"{chara["Name"]} dealt {dmg} damage! The dragon's HP is {dragon["HP"]}.")


def knight_atk(roll):
    """
    Calculate and return damage for a special attack done by Knight.
    """

    # Roll dice for character
    print(f"\n{knight["Name"]} rolled a {roll}.")
    roll = party_luck(roll)

    # Calculate damage
    dmg = (knight["ATK"] + 5) * roll
    dmg -= dragon["DEF"]

    print(f"\n{knight["Name"]} used True Strike to attack the dragon.")

    return dmg


def warrior_atk(roll):
    """
    Calculate and return damage for a special attack done by Warrior.
    """

    # Roll dice for character
    print(f"\n{warrior["Name"]} rolled a {roll}.")
    roll = party_luck(roll)

    # Calculate damage
    dmg = warrior["DEF"] + (roll * 10)
    dmg -= dragon["DEF"]

    print(f"\n{warrior["Name"]} used Berserk Charge to attack the dragon.")

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
    global party
    # Calculate damage if dragon attacks
    if action < 4:
        party_hit.extend(party)
        print("\nThe dragon attacked the party with a tail swipe.")
        dmg = dragon["ATK"] + roll
    elif action < 6:
        party_hit.append(dragon_target())
        print(
            f"\nThe dragon attacked {party_hit[0]["Name"]} with a claw scratch.")
        dmg = dragon["ATK"] + roll * 2
    elif action == 6:
        party_hit.extend(party)
        print("\nThe dragon attacked the party with fire breath.")
        dmg = dragon["ATK"] + roll * 3

    # Display outcome, no damage dealt if less than character defence
    for chara in party_hit:
        dmg -= chara["DEF"]
        if dmg <= 0:
            print(
                f"{chara["Name"]} defended against the attack! The dragon dealt no damage.")
        else:
            chara["HP"] -= dmg
            # Set character HP to 0 if negative
            if chara["HP"] < 0:
                chara["HP"] = 0
                print(
                    f"The dragon dealt {dmg} damage to {chara["Name"]}! {chara["Name"]} has fallen!")
                party -= chara
            else:
                print(
                    f"The dragon dealt {dmg} damage to {chara["Name"]}! Their HP is {chara["HP"]}.")


def chara_buff(chara):
    """
    Check and updates buff duration for a character.
    """

    # Check Knight buff effect duration
    if chara == knight:
        if knight["Buff_ATK"] != 0:
            knight["Buff_ATK"] -= 1
            if knight["Buff_ATK"] == 0:
                print(f"\n{knight["Name"]}'s attack buff has expired.")
                knight["ATK"] = 10

    # Check Warrior buff effect duration
    if chara == warrior:
        if warrior["Buff_DEF"] != 0:
            warrior["Buff_DEF"] -= 1
            if warrior["Buff_DEF"] == 0:
                print(f"\n{warrior["Name"]}'s defence buff has expired.")
                warrior["DEF"] = 25

    # Check Mage buff effect duration
    if chara == mage:
        if mage["Buff_LUCK"] != 0:
            mage["Buff_LUCK"] -= 1
            if mage["Buff_LUCK"] == 0:
                print(f"\n{mage["Name"]}'s luck buff has expired.")
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
            f"\n{knight["Name"]} used Blessed Sword! \n{knight["Name"]} increased their attack by 5 points! \nThis effect lasts for 2 turns.")

    # Warrior buffs their defence
    if chara == warrior:
        warrior["Buff_DEF"] = 3
        warrior["DEF"] = 30
        print(
            f"\n{warrior["Name"]} used Stalwart Guardian! \n{warrior["Name"]} taunted the dragon and increased their defence by 5 points! \nThis effect lasts for 2 turns.")

    # Mage buffs party luck
    if chara == mage:
        mage["Buff_LUCK"] = 3
        mage["LUCK"] = 3
        print(
            f"\n{mage["Name"]} used Fortune's Favour! \n{mage["Name"]} increased the party's luck by 3 points! \nThis effect lasts for 2 turns. \n{mage["Name"]} will skip their next turn.")


def flee(chara):
    print(f"\n{chara["Name"]} has fled the battle!")
    global party
    party.remove(chara)


# Character Turns


def party_turn():
    """
    Party's Turn
    """

    print("\nIt is the party's turn.\n")

    # Gives turn to all characters in party
    for chara in party:
        # Checks the buff effect duration
        chara_buff(chara)

        # Display current status of all characters
        display_status()
        action = 0

        print(f"\nIt is {chara["Name"]}'s turn.")

        # Loop for validating player input
        while action not in [1, 2, 3, 4]:
            try:
                # Displays list of all possible character actions
                print(f"\nActions:")
                for act in chara["Actions"]:
                    print(f" {act}")

                action = int(input(f"\nChoose {chara["Name"]}'s action: "))
            except ValueError:
                action = 0

            if action == 0 or action not in [1, 2, 3, 4]:
                print("\nThat is not an option. Please enter a valid option.")

        # Removes character from party if they choose to Flee
        if action == 4:
            flee(chara)
        # Character attacks Dragon
        elif action == 1:
            dmg = party_atk(chara)
            party_damage(chara, dmg)
        # Character uses special skill
        elif action == 2:
            # Roll dice for character
            roll = random.randint(1, 6)

            if chara == knight:
                dmg = knight_atk(roll)
                party_damage(chara, dmg)

            if chara == warrior:
                warrior_atk(roll)
                party_damage(chara, dmg)

            if chara == mage:
                chara_heal(mage, roll)
        # Character applies a buff
        elif action == 3:
            add_buff(chara)


def dragon_turn():
    """
    Dragon's Turn
    """

    print("\nIt is the dragon's turn.")

    # Randomise dragon attack, more likely to do less damaging attacks
    act = random.randint(1, 3)
    if act < 3:
        dragon_atk()
    else:
        roll = random.randint(1, 6)
        chara_heal(dragon, roll)


# Loop for the main game
def main_game():
    """
    The main game which involves the party and dragon taking turns to act.
    """

    # Set outcome variable to be returned
    end = 0

    # Loop for fight
    while end == 0:
        # Party Turn
        party_turn()

        # Breaks loop if party has fled
        if not party:
            end = 3
            break

        # Breaks loop if dragon is defeated, player wins
        if dragon["HP"] == 0:
            end = 1
            break

        # Dragon Turn
        dragon_turn()

        # Breaks loop if party is defeated, dragon wins
        if not party:
            end = 2
            break

    return end


# Main Game
print("\n~~~~~~~~~~~~~~~ Defeat the Dragon ~~~~~~~~~~~~~~~\n")
print("A party of brave adventurers are on a quest to defeat a mighty dragon.")
print("After a long and difficult journey, it is time for the final battle.")

end = main_game()

# Display end of fight
if end == 1:
    print("\nThe party won! The party has defeated the dragon.\n")
elif end == 2:
    print("\nThe party lost. The dragon has defeated the party.\n")
elif end == 3:
    print("\nThe party... fled? The dragon was confused.\n")
