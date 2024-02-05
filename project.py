import time
from colorama import Fore, Style
from playsound import playsound
import sys

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        
def introduction():
    print("\n******************************************")
    print("           The Forest Adventure           ")
    print("******************************************\n")

    slow_print("Darkness surrounds you as you step into the mysterious forest.")
    time.sleep(1)
    slow_print("The moonlight barely pierces through the dense canopy above.")
    time.sleep(1)
    slow_print("Strange sounds echo through the trees, creating an eerie atmosphere.")
    time.sleep(1)
    slow_print("You are about to embark on a journey filled with choices and mysteries.")
    time.sleep(1)
    slow_print("In this interactive tale, your decisions will shape your destiny.")
    time.sleep(1)
    slow_print("Be mindful, for the forest is not as it seems.")
    time.sleep(1)
    slow_print("Your adventure begins now. May your choices be your guide.")
    time.sleep(1)
    slow_print("Let The Forest Adventure unfold...\n")
    time.sleep(1)        


def create_question(question, choices):
    slow_print(question)
    time.sleep(1)
    slow_print("Available choices:")
    for i, choice in enumerate(choices, start=1):
        slow_print("\n"+f"{i}. {choice}")

    while True:
        try:
            choice_num = int(input("\nChoose a number: "))
            if 1 <= choice_num <= len(choices):
                return choice_num
            else:
                slow_print("Please choose a valid number.")
        except ValueError:
            slow_print("Please enter a number.")

def encounter_creature():
    slow_print("You encounter a mysterious creature in the forest.")
    time.sleep(1)
    slow_print("...")
    time.sleep(2)

def use_torch():
    slow_print("The torch illuminates your path.")
    time.sleep(1)
    slow_print("...")
    time.sleep(2)

def eaten():
    slow_print(Fore.RED + "The creature is actually a werewolf. Tonight being a full moon, it attacks and eats you." + Style.RESET_ALL)
    time.sleep(1)
    slow_print("...")
    time.sleep(2)
    slow_print("End of the adventure.")
    playsound("werewolf_howl.mp3")
    exit_game()

def run():
    slow_print(Fore.RED + "You flee, but the absence of light makes you miss the root on the ground. You stumble. Slowly, the creature approaches you and eventually devours you." + Style.RESET_ALL)
    time.sleep(1)
    slow_print("...")
    time.sleep(2)
    slow_print("End of the adventure.")
    playsound("werewolf_howl.mp3")
    exit_game()

def run2():
    print("You run away, but in haste, you miss the root on the ground. You stumble. Slowly, the creature approaches you and eventually devours you.")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("End of the adventure.")
    exit_game()

def left():
    print("You arrive on a road. You come across a well-maintained house, but it seems uninhabited.")
    time.sleep(1)
    print("...")
    time.sleep(2)

def right():
    print("You venture deeper into the forest following the noises. Suddenly, the monster appears in front of you. You wield your torch to scare it, you're ready.")
    time.sleep(1)
    print("...")
    time.sleep(2)

def turn_back():
    print("You turn back and return to the forest. What the story hides from us is that by making these kinds of decisions, you will never get out of here.")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("End of the adventure.")
    exit_game()

def surprise():
    print("You enter the house. Suddenly the lights come on, and you see about ten people shouting 'Happy Birthday!!!'. Was all of this just a setup? And what about the noises from the right path? You will find out, one day...")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("End of the adventure.")
    exit_game()

def win():
    print("You throw the torch at the werewolf. It catches fire and flees into the forest. You've won!")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("Victory, for now...")
    exit_game()

def exit_game():
    print("Thanks for playing!")
    exit()

def forest_adventure():
    question_text = "You find yourself in a dark forest. You hear strange noises around you."
    choices = ["Explore the forest further.", "Light a torch."]
    
    choice = create_question(question_text, choices)

    if choice == 1:
        encounter_creature()
        question_text = "You can barely make out the creature, but it seems to be your size. What do you do?"
        choices = ["Approach.", "Light a torch.", "Run away."]
        choice = create_question(question_text, choices)
        if choice == 1:
            eaten()
        if choice == 2:
            use_torch()
            question_text = "You realize the creature is actually a werewolf. What do you do?"
            choices = ["Attack it", "Run away"]
            choice = create_question(question_text, choices)
            if choice == 1:
                win()
            if choice == 2:
                run2()
        if choice == 3:
            run()
    elif choice == 2:
        use_torch()
        question_text = "The edge of the forest is far now. You are on a path, and it eventually splits. Noises seem to come from the right one, but it's impossible to know if they are friendly or hostile. What do you do?"
        choices = ["Go left.", "Go right.", "Turn back."]
        choice = create_question(question_text, choices)
        if choice == 1:
            left()
            question_text = "Your fate (your life?) is in your hands. What do you do?"
            choices = ["Enter the house.", "Turn back."]
            choice = create_question(question_text, choices)
            if choice == 1:
                surprise()
            if choice == 2:
                turn_back()
        if choice == 2:
            right()
            question_text = "It's time to make the most important choice of your life!"
            choices = ["Confront the beast.", "Turn back."]
            choice = create_question(question_text, choices)
            if choice == 1:
                win()
            if choice == 2:
                run2()
        if choice == 3:
            turn_back()
    else:
        print("Something went wrong.")

def main():
    introduction()
    forest_adventure()

if __name__ == "__main__":
    main()
