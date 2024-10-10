hurricane_speed = input("How fast is the hurricane (in mph)?\n>")
hurricane_speed = int(hurricane_speed)

if hurricane_speed < 74:
    print("The hurricane is actually a tropical storm.\n")

elif hurricane_speed < 96:
    print("The hurricane is a category 1 hurricane.\n")

elif hurricane_speed < 111:
    print("The hurricane is a category 2 hurricane.\n")

elif hurricane_speed < 130:
    print("The hurricane is a category 3 hurricane.\n")

elif hurricane_speed < 157:
    print("The hurricane is a category 4 hurricane.\n")


elif hurricane_speed >= 157:
    print("The hurricane is a category 5 hurricane.\n")
