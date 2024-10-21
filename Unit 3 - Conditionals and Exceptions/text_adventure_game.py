import time
import random

def one_v_one(): #define what happens when the player chooses
        
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

def two_v_two():    #define what happens when the player chooses 2v2

    print("Matchmaking... (Ranked 2v2 - Champion 2 Division 3)")
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

def three_v_three(): #define what happens when the player chooses 3v3

    print("Matchmaking...  (Ranked 3v3 - Platinum 1 Division 4)")
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

def player_got_off():
    print("Invalid decision, choose a gamemode.")
    game()

def game():
    print("Welcome To Rocket League!")
    gamemode_selection = input("Would You Like To \nA) Play 1s \nB) Play 2s \nC) Play 3s\nD) Get Off Of Rocket League\n").lower()
    if gamemode_selection == "a":
        one_v_one()
    if gamemode_selection == "b":
        two_v_two
    if gamemode_selection == "c":
        three_v_three
    if gamemode_selection == "d":
        player_got_off

game()
