'''
Written by Jahanzeb Qureshi
Started November 12, 2020

Program Name: Mad Libs
Program Description: The program will generate a sequence of Mad Libs randomly from pre-defined Mad Lib paragraphs.
                       The user will then be asked appropriate words which will replace the sequences
                       to generate a corresponding Mad Lib.

DISCLAIMER: ALL THE MAD LIBS THAT ARE USED ARE OBTAINED FROM THE FOLLOWING LINK:
https://irp-cdn.multiscreensite.com/ec2b0ab8/files/uploaded/Mad%20Libs.pdf
THE CREDITS ARE TO THEIR RESPECTIVE OWNERS
'''


# Import appropriate methods
from letsPlay import lets_Play


#Starts the game
def start_game():
    """

    :rtype: object
    """
    print("Welcome to Mad Libs.")
    userInput = input("Are you ready to start playing Mad Libs? (y/n)\n")

    # Ensures User enters 'y' or 'yes'
    while userInput.lower() not in ['y', 'yes', 'n', 'no']:
        print("\033[0;31m" + "\nInvalid input. Please try again.\n" + "\033[0m") #Displays Error in red color
        userInput = input("Are you ready to start playing Mad Libs? (y/n)\n")

    # Terminates program if user says no
    if userInput.lower() in ['n', 'no']:
        print("\nSee you later, goodbye!")

    else:
        lets_Play()


start_game() #Calls the method above
