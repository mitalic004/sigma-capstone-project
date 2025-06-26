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


<a id="dev"></a>
## Development


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


<a id="credits"></a>
## Credits

### Code

Supplementary learning resources which were referenced throughout the project are listed below:

- Ex1 from [Source](src_link)

### Media

ASCII art images
