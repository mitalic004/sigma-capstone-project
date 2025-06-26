# Sigma Labs Pre-Work Capstone Project

<a id="overview"></a>
## Overview

This project was created as the Capstone Project for the Sigma Labs pre-work assignment. It is a simple turn-based text battle where the player will act as three characters in a party to defeat a dragon. The project was created using Python and can be run using any Python compiler.

## Contents
- [Overview](#overview)
- [How to Run](#run-proj)
- [Planning](#planning)
- [Development](#dev)
- [Testing](#testing)
  - [Manual Testing](#manual-test)
  - [Known Bugs](#bugs)
- [Future Improvements](#future-imp)
- [Credits](#credits)


<a id="run-proj"></a>
## How to Run

1. Download and save the `main.py` file from this GitHub repository.
2. Open a Python IDE/Interpreter.
3. Navigate to the folder where the `main.py` file is stored. (If using an online Python Interpreter, copy and paste the contents of the `main.py` file into it.)
4. Run the `main.py` file using `python3 main.py`.
5. You can now play the game.

<a id="planning"></a>
## Planning

Initially the project only included a single character fighting a dragon. After this initial base was developed, more characters were added to make the game more complex and engaging.

During the planning stage, the stats for the player and the basic outline of program flow were decided before any coding began. These can be seen below:

### Player & Dragon Stats

```
Player
=======
HP: 100
ATK: 10
DEF: 30

Skills:
  - Attack (ATK * Rand(1,6))
  - Heal HP (5 * Rand(1,6))
  - Buff ATK (+5, 2 turns)
  - Buff DEF (+10, 2 turns)
```

```
Dragon
=======
HP: 100
ATK: 25
DEF: 20

Skills:
  - Heal HP (5 * Rand(1,6))
  - Tail Swipe (ATK + Rand(1,10))
  - Claw Scratch ((ATK + Rand(1,10)) * 2)
  - Fire Breath ((ATK + Rand(1,10)) * 3)
```

### Program Flow

```
Overview
========
- player turn
  - display status
  - choose action
    - validation
  - dice roll & calculate outcome
  - display outcome
  - check dragon HP

- dragon turn
  - random action
  - calculate outcome
  - display outcome
  - check player HP

- if player/dragon HP = 0, end fight
  - display end message
```


<a id="dev"></a>
## Development

The project was developed entirely in Python. All characters and their stats were stored in dictionaries and any actions which caused changes in the stored values were reflected in the structures and displayed to users. The party for playable characters was stored as a global list and updated whenever any character left the party.

The initial game with only the player and dragon was created with most actions being programmed and excecuted within a main loop. After adding more characters, these actions were abstacted and refactored so that most of the inital code from the main loop was broken down into several reusable functions which could be accessed by multiple characters and used throughout the program to cut down on repeated code. All functions included appropriate Docstrings with descriptions and comments were included throughout the code to make it easier to understand.

### Character Stats

```python
# Set Knight stats
knight = {
    "Name": "Knight",
    "HP": 100,
    "Max_HP": 100,
    "ATK": 10,
    "DEF": 20,
    "Buff_ATK": 0,
    "Cooldown": 0,
    "Actions": ["1. Attack the dragon.", "2. True Strike (Special Attack, 2 turn cooldown).", "3. Increase attack for 2 turns.", "4. Flee."]
}
```

```python
# Set Warrior stats
warrior = {
    "Name": "Warrior",
    "HP": 100,
    "Max_HP": 100,
    "ATK": 5,
    "DEF": 25,
    "Buff_DEF": 0,
    "Cooldown": 0,
    "Actions": ["1. Attack the dragon.", "2. Berserk Charge. (Special Attack, 2 turn cooldown)", "3. Taunt the dragon and increase defence for 2 turns.", "4. Flee."]
}
```

```python
# Set Mage stats
mage = {
    "Name": "Mage",
    "HP": 100,
    "Max_HP": 100,
    "ATK": 8,
    "DEF": 20,
    "LUCK": 0,
    "Buff_LUCK": 0,
    "Actions": ["1. Attack the dragon.", "2. Heal the party.", "3. Increase the party's luck for 2 turns. (Skip next turn.)", "4. Flee."]
}
```

```python
# Set Dragon stats
dragon = {
    "Name": "Dragon",
    "HP": 1000,
    "Max_HP": 1000,
    "ATK": 25,
    "DEF": 25,
}
```


<a id="testing"></a>
## Testing

<a id="manual-test"></a>
### Manual Testing

Manual testing was carried out throughout the development of the project.

<details>

| Function | Expected Outcome | Pass/Fail |
| ----------- | ----------- | ----------- |
| Program Runs | No errors are displayed when the program is run. | Pass |
| Character Turns | The game cycles through all characters in the party and allows the user to take action with them. | Pass |
| Status Screen | A status screen detailing the current stats of all characters is displayed at the start of character turns. | Pass |
| Action Display | All available action for a character's turn are displayed to the user. | Pass |
| Input Validation | User inputs to decide the actions of characters are validated to ensure only listed actions are taken. | Pass |
| Invalid Inputs | Invalid inputs prompt the user to enter a valid input. | Pass |
| Dragon Turn | The dragon takes a turn and text is displayed to reflect the action taken. | Pass |
| Dragon Attacks | The descriptions and outcomes of the dragon's attacks are displayed to the user and reflected in the next status screen. | Pass |
| Character Attacks | The descriptions and outcomes of character attacks are displayed to the user and reflected in the next status screen. | Pass |
| Character Healing | The description and outcome of healing characters are displayed to the user and reflected in the next status screen. | Pass |
| Knight Special Attack | The knight will perform their special attack, this attack will then be unavailable for next 2 turns. | Pass |
| Knight Buff | The knight will buff their own attack for 2 turns, this change is reflected in the next status screen. | Pass |
| Warrior Buff | The warrior will buff their own defence for 2 turns, this change is reflected in the next status screen. | Pass |
| Warrior Special Attack | The warrior will perform their special attack, this attack will then be unavailable for next 2 turns. | Pass |
| Mage Buff | The mage will buff the party's luck for 3 turns, the mage's next turn is skipped. | Pass |
| Special Attack Cooldowns | If a special attack is on cooldown, the user will be unable to select the option to perform this action. | Pass |
| Special Attack Cooldowns Ending | After the cooldowns for special attacks have expired, the user is notified and the action is made available again. | Pass |
| Buff Durations | After buffs have expired, the user is notified and the stats of characters are changed back to their original values. | Pass |
| Character Defeated | If a character's HP is reduced to 0, they are removed from the party and all following displays. | Pass |
| Party Defeated | If the final character in the party has their HP reduced to 0, the game will end. | Pass |
| Dragon Defeated | If the dragon's HP is reduced to 0, the game will end. | Pass |
| Character Flees | If a character chooses to flee, they are removed from the party and all following displays. | Pass |
| Party Flees | If the final character in the party chooses to flee, the game will end. | Pass |
| Ending Display | The appropriate ending text is displayed if the conditions are met. | Pass |

</details>

<a id="bugs"></a>
### Known Bugs

- There are no known bugs in this project.


<a id="future-imp"></a>
## Future Improvements

- Making the program more visually engaging, perhaps by adding ASCII art for the dice rolls or endings.
- Increase the complexity of the Dragon's moveset.
- Adding a second phase for the Dragon.
- Include more flavour text or descriptions for more engagement.

<a id="credits"></a>
## Credits

Supplementary learning resources which were referenced throughout the project are listed below:

- [W3Schools](https://www.w3schools.com/python/default.asp)
- [Build a Quiz Application With Python](https://realpython.com/python-quiz-application/)
- [Build a Dice-Roll Application With Python](https://realpython.com/python-dice-roll/)
