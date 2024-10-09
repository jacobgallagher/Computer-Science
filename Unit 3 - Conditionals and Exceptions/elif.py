# the if statement has two buddies
# the first little buddy is the else statement

x = input("Enter a number.\n>")
x = int(x)
if x > 0:     # not every if needs an else
    print(str(x) + " is a positive number!")

# the second buddy is the elif statement
elif x < 0:
    print(str(x) + " is a negative number!")

else:         # else always needs an if
    print(str(x) + " is zero!")

light = input("what color is the light?\n")

if light.lower() == "green":
    print("GO")

elif light.lower() == "yellow":
    print("STOP IF SAFE")

elif light.lower() == "red":
    print("STOP")

else:
    print("YIELD")

x = 10

if x > 5:
    print("x is greater than 5")

elif x > 8:
    print("x is greater than 8")