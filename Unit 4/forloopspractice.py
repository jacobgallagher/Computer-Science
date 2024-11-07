#For loops review
#for loops allow us to iterate through a list!
#Iterate: perform repeatedly
#to do something repeatedly
# to look at every item in a list, one by one

#Basic syntax
#Syntax: the "grammer" of the code

pokemon_cards = ["squirtle", "bidoof", "zigzagoon", "charizard"]

for card in pokemon_cards:
    print("The nexy card is...")
    print(card)

route = ["Home", "Taco Bell", "The Park", "Goodwill", "Home"]

#if you need to look at multiple list items during one iteration
# doing "for item in list", doesnt really work
# for item in list only allows you to access one list item per iteration

#for location in route:
    #print("You are traveling from " + location + " to " + location[1])
    #this doesnt work!

#if you need to access multiple list items during the same iteration
# using "for varibale in range()" is preferred

for i in range(0, len(route)): #creates a list [0,1,2,3,4]
    try:
        print("You are trvaeling from " + route[i] + " to " + route[i + 1])
    except:
        print("Route finished!")
