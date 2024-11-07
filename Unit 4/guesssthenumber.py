import random

number = random.randint(1, 100)
user_input = ""
attempt = 0

while user_input != number:
    user_input = input("Guess the number 1-100!\n>")
    user_input = int(user_input)
    attempt = attempt + 1

    if user_input == number:
        print("\nYou guessed it! The number was " + str(number) + ". It took you " + str(attempt) + " attempts, Great job!\n")
    else:
        if user_input >= number:
            print("Incorrect, too high.")
        elif user_input <= number:
            print("Incorrect, too low.")
        else:
            print("Invalid input, try again.")
