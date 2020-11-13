from time import sleep
from os import system


# Allows random numbers to be generated
import random

# MAD LIB 1 OBTAINED FROM: https://irp-cdn.multiscreensite.com/ec2b0ab8/files/uploaded/Mad%20Libs.pdf
# Function for the first Mad Lib
def mad_lib1():
    print("\033[0;32m" + "Mad Lib Version 1\n" + "\033[0m") #Displays Mad Lib version in green


    # Ask User for appropriate terms to generate Mad Lib
    noun1 = input("Please enter a noun: ")
    adjective1 = input("Please enter an adjective: ")
    number = input("Please enter a number: ")
    adjective2 = input("Please enter a second adjective: ")
    noun2 = input("Please enter a second noun: ")
    name1 = input("Please enter a name: ")
    name2 = input("Please enter a second name: ")
    plural_Noun = input("Please enter a plural noun: ")
    ing_Verb = input("Please enter a verb ending with 'ing': ")
    plural_Noun2 = input("Please enter a second plural noun: ")
    adjective3 = input("Please enter a third adjective: ")
    adverb = input("Please enter an adverb: ")

    #Clears screen and displays Mad Lib
    system('clear')
    print("Mad Lib generated:\n")

    #Mad Lib is defined here
    mad_lib11 = ("One very nice morning near the end of summer, my mother woke me up at 4:00 A.M. and"
                 "\nsaid, \"Wake up and smell the grass, sleepy head! Today is your first day of school"
                 "\nand you can't be late.\" I groaned in my bed for twenty seconds, but eventually I got dressed."
                 "\nI wore a blue and white striped, long sleeve (NOUN) with a collar on it, a red tie,"
                 "\ndark gray pants, white socks, black shoes, and a(n) (ADJECTIVE) hat. In ten minutes I"
                 "\nmade lunch and ate my breakfast. (NUMBER) minutes later, the bus came. A few minutes later,"
                 "\nI was at school. In school, I met two really (ADJECTIVE2) kids. All of us became friends"
                 "\nvery fast. That day we had Science, and luckily my friends and I were at the same (NOUN2)."
                 "\nMy friends' names are (NAME1) and (NAME2). In Math we weren't together, and that really bugged me. "
                 "\nWe learned what (PLURAL NOUN) were, and when to use them. At snack and recess, we played a game "
                 "together. "
                 "\nIt was extremely fun. At P. E., we were (-ING VERB) off of the ropes onto (PLURAL NOUN2). I thought it was"
                 "\na very (ADJECTIVE3) idea. In swimming class, we needed to swim extremely (ADVERB),"
                 "\nor else we would have to swim longer. Before I knew it, school was over. I grabbed all my belongings"
                 "\nand put them into my backpack. In two minutes, the bus came. As I stepped into the bus I shouted,"
                 "\n\"Goodbye, adios amigos, and shalom,\" to my friends. Then I went into the bus. In a flash, I was"
                 "\nback home. This day was an extremely exciting day!")

    # Replacing the characters with the user input and displaying with underline
    mad_lib_final = mad_lib11.replace("(NOUN)", "\033[4m" + noun1.lower() + "\033[0m").replace("(ADJECTIVE)",
                                                                                                  "\033[4m" + adjective1.lower() + "\033[0m").replace(
        "(NUMBER)", "\033[4m" + number + "\033[0m").replace("(ADJECTIVE2)",
                                                               "\033[4m" + adjective2.lower() + "\033[0m").replace(
        "(NOUN2)", "\033[4m" + noun2 + "\033[0m").replace("(NAME1)",
                                                             "\033[4m" + name1.capitalize() + "\033[0m").replace(
        "(NAME2)", "\033[4m" + name2.capitalize() + "\033[0m").replace("(PLURAL NOUN)",
                                                                          "\033[4m" + plural_Noun.lower() + "\033[0m").replace(
        "(-ING VERB)", "\033[4m" + ing_Verb.lower() + "\033[0m").replace("(PLURAL NOUN2)",
                                                                            "\033[4m" + plural_Noun2.lower() + "\033[0m").replace(
        "(ADJECTIVE3)", "\033[4m" + adjective3.lower() + "\033[0m").replace("(ADVERB)",
                                                                               "\033[4m" + adverb.lower() + "\033[0m")

    #Prints generated Mad Lib
    print(mad_lib_final)

    #Returns to ask if User would want to continue playing
    play_Again()

# Function for restarting the game
def play_Again():
    user = input("\nWould you like to play again? (y/n)\n")

    #If user enters an invalid input
    while user.lower() not in ['y', 'yes', 'n', 'no']:
        print("\033[0;31m" + "\nInvalid input. Please try again.\n" + "\033[0m")
        user = input("Would you like to play again? (y/n)\n")
        # Terminates program if user says no

    if user.lower() in ['n', 'no']:
        print("\nSee you later, goodbye!")

    else:
        lets_Play()


# MAD LIB 2 OBTAINED FROM: https://irp-cdn.multiscreensite.com/ec2b0ab8/files/uploaded/Mad%20Libs.pdf
# Function for the second Mad Lib
def mad_lib2():
    print("\033[0;32m" + "Mad Lib Version 2\n" + "\033[0m") #Displays Mad Lib version in green

    #Ask user for appropriate terms to generate Mad Lib
    adjective1 = input("Please enter an adjective: ")
    noun = input("Please enter a noun: ")
    past_tense_verb = input("Please enter a verb in past tense: ")
    adverb = input("Please enter an adverb: ")
    adjective2 = input("Please enter a second adjective: ")
    noun2 = input("Please enter a second noun: ")
    noun3 = input("Please enter a third noun: ")
    adjective3 = input("Please enter a third adjective: ")
    verb = input("Please enter a verb: ")
    adverb2 = input("Please enter a second adverb: ")
    past_tense_verb2 = input("Please enter a second verb in past tense: ")
    adjective4 = input("Please enter a fourth adjective: ")

    #Mad Lib is defined here
    mad_lib22 = ("\nToday I went to the zoo. I saw a(n) (ADJECTIVE) (NOUN) jumping up and down in its tree."
                 "\nHe (PAST TENSE VERB) (ADVERB) through the large tunnel that led to its (ADJECTIVE2) (NOUN2). "
                 "\nI got some peanuts and passed them through the cage to a gigantic gray (NOUN3) towering above my head. "
                 "\nFeeding that animal made me hungry. I went to get a (ADJECTIVE3) scoop of ice cream. It filled my stomach. "
                 "\nAfterwards I had to (VERB) (ADVERB2) to catch our bus. When I got home I (PAST TENSE VERB2) my mom for a (ADJECTIVE4) "
                 "day at the zoo. ")

    # Replacing the characters with the user input and displaying with underline
    mad_lib_final = mad_lib22.replace("(ADJECTIVE)", "\033[4m" + adjective1.lower() + "\033[0m").replace(
        "(NOUN)", "\033[4m" + noun.lower() + "\033[0m").replace("(PAST TENSE VERB)", "\033[4m" + past_tense_verb.lower() + "\033[0m").replace(
        "(ADVERB)", "\033[4m" + adverb.lower() + "\033[0m").replace("(ADJECTIVE2)", "\033[4m" + adjective2.lower() + "\033[0m").replace(
        "(NOUN2)", "\033[4m" + noun2.lower() + "\033[0m").replace("(NOUN3)","\033[4m" + noun3.lower() + "\033[0m").replace(
        "(ADJECTIVE3)", "\033[4m" + adjective3.lower() + "\033[0m").replace("(VERB)", "\033[4m" + verb.lower() + "\033[0m").replace(
        "(ADVERB2)", "\033[4m" + adverb2.lower() + "\033[0m").replace("(PAST TENSE VERB2)", "\033[4m" + past_tense_verb2.lower() + "\033[0m").replace(
        "(ADJECTIVE4)", "\033[4m" + adjective4.lower() + "\033[0m")

    #Clears screen and displays Mad Lib
    system('clear')
    print("Mad Lib generated:\n")

    #Prints generated Mad Lib
    print(mad_lib_final)

    #Asks if User wants to play again
    play_Again()

# MAD LIB 3 OBTAINED FROM: https://irp-cdn.multiscreensite.com/ec2b0ab8/files/uploaded/Mad%20Libs.pdf
# Function for the third Mad Lib
def mad_lib3():
    print("\033[0;32m" + "Mad Lib Version 3\n" + "\033[0m") #Displays Mad Lib version in green

    #Asks user for appropriate terms to generate Mad Lib
    verb = input("Please enter a verb: ")
    noun = input("Please enter a noun: ")
    adjective = input("Please enter an adjective: ")
    adverb = input("Please enter an adverb: ")

    #Mad Lib is defined here
    mad_lib33 = ("The day I saw the Monkey King (VERB) was one of the most interesting days of the year."
                "\nAfter he did that, the king played chess on his brother's (NOUN) and then combed his (ADJECTIVE) "
                 "\nhair with a comb made out of old fish bones. Later that same day, I saw the Monkey King dance "
                 "(ADVERB) "
                 "in front of an audience of kangaroos and wombats.")

    # Replacing the characters with User input and displaying with underline
    mad_lib_final = mad_lib33.replace("(VERB)", "\033[4m" + verb.lower() + "\033[0m").replace("(NOUN)", "\033[4m"
                    + noun.lower()+"\033[0m").replace("(ADJECTIVE)", "\033[4m"  + adjective.lower() + "\033[0m").replace(
                    "(ADVERB)", "\033[4m" + adverb.lower() + "\033[0m")

    #Clears screen and displays Mad Lib
    system('clear')
    print("\nMad Lib generated:\n")

    print(mad_lib_final)
    play_Again()

def lets_Play():
    # Creates loading screen
    print("Okay, let's play :)")
    sleep(2)  # puts above text on display for 2 seconds and then clears screen
    system('clear')
    print("Let's begin:")

    #The Mad Lib is generated based on a randon number generated from 1-3
    x = random.randint(1,3)

    #Appropriate Mad Lib function is called
    if x == 1:
        mad_lib1()
    elif x == 2:
        mad_lib2()
    else:
        mad_lib3()
