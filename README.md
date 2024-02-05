# Text-based-Adventure-Game-Anouk-Leyris-CDOF2

A text-based adventure game where the player's decisions define the outcome of the story.

## Getting Started

To get started, clone the repository to your local machine: git clone https://github.com/anoukleyris/Text-based-Adventure-Game-Anouk-Leyris-CDOF2.git

# Prerequisites (for those who want to help me)

Before making any changes, create a fork and a branch with the issue you resolve, where you will modify the code without touching my main branch.

## Running the Tests
Before running the tests, ensure you have the required libraries installed. You can install them using:
pip install colorama playsound
# Add other libraries if needed
Open the code project.py with Visual Studio Code for example
Launch the code using the "Run" command or in entering "run project.py" in a terminal and start playing!


### Break Down into End-to-End Tests

The game will end when the story is complete.

## main steps: 

Function Definitions:

introduction(): Prints a welcome message and sets the stage for the text adventure.
create_question(question, choices): Prints a question and a list of choices, takes user input, and validates the choice.
encounter_creature(): Describes encountering a mysterious creature in the forest.
use_torch(): Describes using a torch to illuminate the path.
eaten(), run(), run2(), left(), right(), turn_back(), surprise(), win(): Different scenarios and outcomes of the story.
exit_game(): Prints a thank-you message and exits the game.
forest_adventure() Function:

Asks the player to make a choice between exploring the forest further or lighting a torch.
If the player chooses to explore, more choices and scenarios unfold, leading to different outcomes based on subsequent choices.
main() Function:

Calls introduction() to set up the story.
Calls forest_adventure() to start the main part of the text adventure.
if __name__ == "__main__": Block:

Checks if the script is being run directly and not imported as a module.
Calls the main() function to start the execution of the text adventure.
The story involves making choices that affect the outcome, with different branches leading to various possible endings. The code uses time.sleep() to introduce delays in the text for a better storytelling experience.


**Contributors:**
- Anouk Leyris - Head of the project
- Joshua Bornet - Part of the game realisation
- Jean-Baptiste Martin - Part of the README redaction 


## Authors

- **Anouk Leyris** - Head of the project
- **Jean-Baptiste Martin**
- **Joshua Bornet**

## License

This project is licensed under the MIT License
