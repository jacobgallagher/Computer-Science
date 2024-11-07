# There are a couple types of lloops in python
# the for loop lets you iterate through a list
# -great for looping a set number of times
# but what if we need to loop an uncertain number of times
# ex. entering your password
# you could get it right the first time or not

import time

real_pass = "ninjalowtaper"
entered_pass = ""
attempt = 0

while entered_pass != real_pass:
    #ask for the password
    entered_pass = input("Please enter the password\n>").lower()

    #check if password is corret
    if entered_pass == real_pass:
        print("ACCESS GRANTED")
    else:
        attempt = attempt + 1
        print("ACCESS DENIED")
        print("Attempts: " + str(attempt))
        print("try again...")

print("Welcome!")

# with while loops, you need to be careful for infinite loop
#infinite loop - loop cannot be escapes

#count = 0
#while True:
    #count = count + 1
    #print(count)

user_input = ""

while user_input != "exit":
    user_input = input("Enter something!\n>").lower()
    print("type 'exit to quit")
    print("You typed: " + user_input)

    print("All done!")