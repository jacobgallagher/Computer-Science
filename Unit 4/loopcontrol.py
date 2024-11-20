# loop control statements
# allow you to change how loops operate
# they do things like quit the loop early, skip the loop, or even do nothing at all
# break, continue, pass

# break
# exits a loop prematurely, before it was supposed to end
# happens immediately when ran
# program continues where the loop ended

# example

bag_of_fruit = ["apple", "orange", "bug", "kiwi", "watermelon", "mango"]

for fruit in bag_of_fruit:
    if fruit == "bug":
        print("You found a nasty bug...")
        break              # the break statement exits the loop immediately and continues on
    print("You ate a " + fruit)

print("All done!")

# continue
# skips the current loop
# it does not exit entire loop, just moves on to the next iteration

# example

orders = [15, 30, 35, 23, 100, 3 , 10, 22]

# discount applying program
# only want to apply the discount for above $20

for order in orders:
    if order <= 20:
        continue
    print("$" + str(order) + " order discounted 5% to $" + str(order * 0.95))

# pass
# does nothing!!!
# usually used as a placeholder while writing code
# text adnveture project
    
# write a lline of code that does nothing
    
def enter_forest():
    pass