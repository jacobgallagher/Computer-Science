                                                # Exception Handling
                                                # Write a program that asks for two numbers and divides them

                                                # if        =   try
                                                # else      =   except

def divide_two_numbers():
    try:                                        # We always enter the try block, there is no  condition
        x = int(input("What is the first number?\n>"))
        y = int(input("What is the second number?\n>"))
        print(x / y)
        
    except ZeroDivisionError:
        print("Cannot divide by zero, try again.")
    
    except ValueError:
        print("Please enter a valid numerical symbol, try again.")
    
    except:                                     # if anything in the try block causes an error, 
                                                # the try block stops immediatly, and the except is ran
                                                # if the try block executes withuot an error, the except is skipped
                                                # the only way to get into the except is to "throw" an error
        print("Invalid input, try again.")
        divide_two_numbers()                    # Tell the function to run again

divide_two_numbers()

