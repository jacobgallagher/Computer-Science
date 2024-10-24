import time
import random


score = 0
opponent_score = 0


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
    kickoff()


def kickoff():
    kickoff_selection = input("What kickoff are you gonna use?\nA) Speed Flip Kickoff\nB)Delayed Kickoff\nC)Fake Kickoff\n").lower()
    if kickoff_selection == "a":
        kickoff_outcome_1()
    if kickoff_selection == "b":
        kickoff_outcome_2()
    if kickoff_selection == "c":
        kickoff_outcome_3()
       


def kickoff_outcome_1():
    win_chance = random.random()
    if win_chance <= .4:
        print("You won the kickoff And scored, the score is now " + score + 1 + " - " + opponent_score + "\n")
        time.sleep(3)
        print("Kickoff in 3...\n")
        time.sleep(1)
        print("Kickoff in 2...\n")
        time.sleep(1)
        print("Kickoff in 1...\n")
        second_kickoff_1()
    if win_chance  > .4 and win_chance <= .8:
        print("You won the kickoff and the ball is on Megagamer768's side!")
        choose_to_shoot()
    elif win_chance > .8:
        print("You lost the kickoff and your opponent scored, the score is now " + score + + " - " + opponent_score + 1 + "\n")
        time.sleep(3)
        print("Kickoff in 3...\n")
        time.sleep(1)
        print("Kickoff in 2...\n")
        time.sleep(1)
        print("Kickoff in 1...\n")
        second_kickoff_1()

def choose_to_shoot():
    choice = input("Would you like to\nA) Shoot the ball\nB) Play defensive and go back to your goal post")
    if choice == "a":
        shooting_ball()
    if choice == "b":
        defend_2()
    else:
        print("Invalid input, try again.")
        choose_to_shoot()





    if selection == "a":
        win_chance = random.random()
        if win_chance <= .8:
            print("You got to the ball first!")
            win_chance = random.random()
            if win_chance <= .85:
                print(username + "scored! The score is now " + score + 1 + " - " + opponent_score + "\n")
                third_kickoff()
            else:
                print("You hit the ball off of the crossbar.")
                crossbar_decision()
               
           
        else:
            print("Megagamer768 got to the ball before you, the ball is now on your side. Defend.")
            defend()
def go_to_goal():
    win_chance = random.random()
    if win_chance <= .5:
        print("You made it back to the goal!")
        defend()
    else: 
        print("You didnt make it back in time. The score is now " + score + 1 + " - " + opponent_score + "\n")

def press_f():
    F = input("Press F to go to try to get to your goal and defend!").lower()
    if F == "f":
            go_to_goal()
    else:
        print("Invalid input, try again.")
        press_f()

def rush_ball():
    win_chance = random.random()
    if win_chance <= .3:
        print("You didn't make it to the ball fast enough\n")
        press_f()
def boost_over_ball():
    win_chance = random.random()
    if win_
def select_after_kickoff():
    selection = input("You won the kickoff, would you like to \nA) Rush the ball without boost. \nB) Go to boost instead of the ball. \nC) Try to demolish Megagamer768.\n").lower()
    if selection == "a":
        rush_ball()
    if selection == "b":
        boost_over_ball()
    if selection == "c":
        demolish()
    else:
        print("Invalid input, try again.")


def kickoff_outcome_2():
    win_chance = random.random()
    if win_chance <= .7:
        select_after_kickoff()
    if win_chance > .7:
        print("You lost the kickoff, the ball is going towards your goal.")
        defend()
        second_kickoff_1()


def second_kickoff_1():
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
        second_kickoff_1()


def defend():
    button_press = input("Press X to defend.\n").lower()
    if button_press == "x":
        win_chance = random.random()
        if win_chance <= .50:
            print("You saved the ball and scored on Megagamer768's goal! The score is now " + score + 1 + " - " + opponent_score + "\n")
        else:
            print("You failed to defend. Megagamer768 scored on you and the score is now " + score + " - " + opponent_score + 1 + "\n")

def defend_2():
    button_press = input("Press X to defend.\n").lower()
    if button_press == "x":
        win_chance = random.random()
        if win_chance <= .50:
            print("Megagamer768 hit the ball towards you. You managed to defend!")
            shooting_ball()
        else:
            print("You failed to defend. Megagamer768 scored on you and the score is now " + score + " - " + opponent_score + 1 + "\n")

def shooting_ball():
    input("Press X to shoot the ball!\n")
    score_chance = random.random()
    if score_chance <= .7:
        print("You scored! The score is now " + score + 1 + " - " + opponent_score + "\n")
    else:
        print("You missed the shot.\n")
        a_to_defend()



def a_to_defend():
    press = input("Press A to go back and defend!").lower()
    if press == "a":
        defend()
    else:
        print("Invalid input, try again.")
        a_to_defend()

def defending_shot():
    button_press = input("Press X to defend.\n").lower()
    if button_press == "x":
        win_chance = random.random()
        if win_chance <= .50:
            print("You saved the ball!")
            shooting_ball()
        else:
            print("You failed to defend. Megagamer768 scored on you and the score is now .")


def double_touch():
    win_chance  = random.random()
    if win_chance <= .6:
        print("You scored the double touch! The score is now ")
    else:
        x = input("You missed the double touch. Press X to go back to your goal and defend!").lower()
        if x == "x":
            defending()
           
        else:
            print("Invalid input, try again.")
            double_touch()


def crossbar_decision():
    choice = input("Would you like to\nA) Jump for the double touch\nB) Back off and defend.").lower()
    if choice == "a":
        double_touch()
    if choice == "a":
        defending()
        print("Megagamer768 scored on you and the score is now ")


           


def offensive_kickoff():
    selection = input("Would you like to \nA) Rush the ball without boost. \nB) Go to boost instead of the ball. \nC) Try to demolish Megagamer768.\n").lower()
    if selection == "a":
        win_chance = random.random()
        if win_chance <= .8:
            print("You got to the ball first!")
            win_chance = random.random()
            if win_chance <= .85:
                print(username + "scored! The score is now 2-0.")
                third_kickoff()
            else:
                print("You hit the ball off of the crossbar.")
                crossbar_decision()
               
           
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


