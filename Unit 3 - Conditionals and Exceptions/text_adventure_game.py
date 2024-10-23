import time
import random

def one_v_one():
       
    print("Matchmaking... (Ranked Duel - Diamond 1 Division 4)\n")
    time.sleep(2.5)
    print("Match Found\n")
    time.sleep(1)
    print("Entering match in 3...")
    time.sleep(1)
    print("Entering match in 2...")
    time.sleep(1)
    print("Entering match in 1...")
    time.sleep(1)
    print("Match Entered.\n")
    time.sleep(.5)
    print("You are playing against Megagamer768, first player to 3 goals wins!\n")
    time.sleep(3)
    print("Kickoff in 3...\n")
    time.sleep(1)
    print("Kickoff in 2...\n")
    time.sleep(1)
    print("Kickoff in 1...\n")


    first_kickoff_selection_1 = input("What kickoff are you gonna use?\nA) Speed Flip Kickoff\nB)Delayed Kickoff\nC)Fake Kickoff\n").lower()
    if first_kickoff_selection_1 == "a":
        first_one_v_one_speed_kickoff()
    if first_kickoff_selection_1 == "b":
        first_one_v_one_delayed_kickoff()
    if first_kickoff_selection_1 == "c":
        first_one_v_one_fake_kickoff()


def first_one_v_one_speed_kickoff():
    win_chance = random.random()
    if win_chance <= .4:
        print("You won the kickoff And scored, the score is now 1-0!\n")
        time.sleep(3)
        print("Kickoff in 3...\n")
        time.sleep(1)
        print("Kickoff in 2...\n")
        time.sleep(1)
        print("Kickoff in 1...\n")
        win_first_speed_kickoff_1()
    elif win_chance > .4:
        print("You lost the kickoff and your opponent scored, the score is now 0-1!\n")
        time.sleep(3)
        print("Kickoff in 3...\n")
        time.sleep(1)
        print("Kickoff in 2...\n")
        time.sleep(1)
        print("Kickoff in 1...\n")
        lost_first_speed_kickoff_1()

def lost_first_speed_kickoff_1():
    print("")

def win_first_speed_kickoff_1():
    second_kickoff_selection_2 = input("What kickoff are you gonna use?\nA) Speed Flip Kickoff\nB)Delayed Kickoff\nC)Fake Kickoff").lower()
    if second_kickoff_selection_2 == "a":
        time.sleep(1)
        win_chance = random.random()
        if win_chance <= .7:
            print("You won the kickoff!")
            time.sleep(1)
            offensive_kickoff()
    if second_kickoff_selection_2 == "b":
        print
    if second_kickoff_selection_2 == "c":
        print
    else:
        print("Invalid input, try again.")
        win_first_speed_kickoff_1()

def defend():
    button_press = input("Press X to defend.\n").lower()
    if button_press == "x":
        win_chance = random.random()
        if win_chance <= .50:
            print("You saved the ball and scored on Megagamer768's goal! The score is now 2-0.")
        else:
            print("You failed to defend. Megagamer768 scored on you and the score is now 1-1.")

def offensive_kickoff():
    selection = input("Would you like to \nA) Rush the ball without boost. \nB) Go to boost instead of the ball. \nC) Try to demolish Megagamer768.")
    if selection == "a":
        win_chance = random.random()
        if win_chance <= .8:
            print("You got to the ball first!")
            win_chance = random.random()
            if win_chance <= .85:
                print(username + "scored! The score is now 2-0.")
                third_kickoff()
                
            
        else:
            print("Megagamer768 got to the ball before you, the ball is now on your side. Defend.")
            defend()




def first_one_v_one_delayed_kickoff():
    win_first_kickoff_chance_1 = random.random()
    if win_first_kickoff_chance_1 <= .35:
        print("You won the kickoff And scored, the score is now 1-0.\n")
        win_first_speed_kickoff_1()
    else:
        print("You lost the kickoff and your opponent scored, the score is now 0-1.\n")
        lost_first_speed_kickoff_1()


def first_one_v_one_fake_kickoff():
    win_speed_kickoff_chance = random.random()
    if win_speed_kickoff_chance <= .8:
        print("You won the kickoff And scored, the score is now 1-0.\n")
        win_first_speed_kickoff_1()
    else:
        print("You lost the kickoff and your opponent scored, the score is now 0-1.\n")
        lost_first_speed_kickoff_1()

username = input("What is your username?\n>")
time.sleep(1)
input("Press any button to continue.\n")

def game_welcome():
    print("Welcome To Rocket League!")
    gamemode_selection = input("Would You Like To \nA) Play 1s \nB) Play 2s \nC) Play 3s\n").lower()
    if gamemode_selection == "a":
        one_v_one()
    if gamemode_selection == "b":
        two_v_two
    if gamemode_selection == "c":
        three_v_three
    else:
        print("Invalid choice, try again.")
        game_welcome()

game_welcome()

def won_first_speed_kickoff_1():


    print("Kickoff in 3\n")
    time.sleep(1)
    print("Kickoff in 2\n")
    time.sleep(1)
    print("Kickoff in 1\n")
    second_kickoff_selection_1 = input("What kickoff are you gonna use?\nA) Speed Flip Kickoff\nB)Delayed Kickoff\nC)Fake Kickoff").lower()
    if second_kickoff_selection_1 == "a":
        print("")


def two_v_two():
    print("Matchmaking... (Ranked 2v2 - Champion 2 Division 3)")


def three_v_three():
    print("Matchmaking...  (Ranked 3v3 - Platinum 1 Division 4)")


#r = random.randrange(0,10) ozowski
