print("Math Test!\n")

score = 0

answer_one = input("What is 2 + 2\n>")
answer_one =int(answer_one)
if answer_one == 4:
    score = int(score) + 1
    print(str(answer_one) + " Is Correct!\n>")

answer_two = input("What is 100 + 100\n>")
answer_two =int(answer_two)
if answer_two == 200:
    score = int(score) + 1
    print(str(answer_two) + " Is Correct!\n>")

answer_three = input("What is 10 x 34\n>")
answer_three =int(answer_three)
if answer_three == 340:
    score = int(score) + 1
    print(str(answer_three) + " Is Correct!\n>")

answer_four = input("What is 100 / 10\n>")
answer_four =int(answer_four)
if answer_four == 10:
    score = int(score) + 1
    print(str(answer_four) + " Is Correct!\n>")

answer_five = input("What is 999 x 999\n>")
answer_five =int(answer_five)
if answer_five == 998001:
    score = int(score) + 1
    print(str(answer_five) + " Is Correct!\n>")

print("Your score is: " + str(score) + " / 5!")