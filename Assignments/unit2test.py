animal = input("please enter your favorite animal.\n>")  #1st challenge
location= input("please enter where the " + animal + " lives.\n>")
weight = input("please enter how much the "+ animal + " weighs (in lbs).\n>")

print("\n")

print("Your favorite animal is the " + animal + ". The " + animal + " lives in " + location + ", and it weighs " + weight + " Lbs. Great Pick!\n")


def add_three(x, y, z):             #2nd challenge
    sum = (x + y + z)
    sum = str(sum)
    print("\n")
    print(sum + " is the sum of " + str(x) + ", " + str(y) + ", and " + str(z) + ".\n")
    print("\n")

x = input("please enter a number.\n>")
y = input("please enter a number.\n>")
z = input("please enter a number.\n>")

x = int(x)
y = int(y)
z = int(z)

add_three(x, y, z)


def data_three():                   #3rd challenge
    num = input("please enter a number.\n>")
    dec = input("please enter a decimal number.\n>")
    word = input("please enter a word.\n>")
    num = float(num)
    dec = float(dec)
    sum = float(num + dec)
    print("\n")
    print(str(sum) + " " + word)

data_three()