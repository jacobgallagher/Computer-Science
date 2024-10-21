import time
import random

def game():
    print("Welcome To Rocket League!")
    gamemode_selection = input("Would You Like To \nA) Play 1s \nB) Play 2s \nC) Play 3s\n").lower()
    if gamemode_selection == "a":
        one_v_one()
    if gamemode_selection == "b":
        two_v_two
    if gamemode_selection == "c":
        three_v_three

def one_v_one():
        
    print("Matchmaking... (Ranked Duel - Diamond 1 Division 4)")
    time.sleep(1)
    print("Match Found\n")
    time.sleep(1)
    print("Entering match in 3")
    time.sleep(1)
    print("Entering match in 2")
    time.sleep(1)
    print("Entering match in 1")
    time.sleep(1)
    print("Match Entered.")
    time.sleep(1)
    print("You are playing against Megagamer768.\n")
    time.sleep(1)
    print("Kickoff in 3\n")
    time.sleep(1)
    print("Kickoff in 2\n")
    time.sleep(1)
    print("Kickoff in 1\n")

    kickoff_selection = input("What kickoff are you gonna use?")

def two_v_two():
    print("Matchmaking... (Ranked 2v2 - Champion 2 Division 3)")
def three_v_three():
    print("Matchmaking...  (Ranked 3v3 - Platinum 1 Division 4)")
game()

import random

r = random.randrange(0,10)  
print(r)

print("You have a 25 chance to win")
p =random.random()

if p <= 0.25:
    print("YOU WIN!!")
else:
    print("You Lose")