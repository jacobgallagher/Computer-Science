def least_squares_regression_line():
    try:
        correlation = float(input("What is the correlation (r value)?\n>"))
        standard_x = float(input("What is the standard deviation of X values?\n>"))
        standard_y = float(input("What is the standard deviation of Y values?\n>"))

        b = correlation * standard_x / standard_y
        b = float(b)

        mean_x = float(input("What is the mean of the X values?\n>"))
        mean_y = float(input("What is the mean of the Y values?\n>"))

        multiplied_mean_and_b = float(mean_x * b)
        a = float(mean_y - multiplied_mean_and_b)

        print("The least squares regression line for your data is Y (predicted) = " + str(b) + " + " + str(a) + "(x)")

    except:
        print("invalid input, try again")
        least_squares_regression_line()

least_squares_regression_line()