import random

r = random.randrange(0,10)  #we can roll a zero, but not a 10. first number is inclusive, second is exclusive 
print(r)

print("You have a 25 chance to win")
p =random.random()
# random.random generates a random float between 0 and 1
if p <= 0.25:
    print("YOU WIN!!")
else:
    print("You Lose")