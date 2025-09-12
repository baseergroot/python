import random
import math


try:
    user_number = int(input("Quess number between 1 - 100: "))

    comp_number = math.floor(random.random() * 100)
    print("computer select " , comp_number)

    if comp_number < user_number:
        
        if user_number - comp_number > 0 and user_number - comp_number <= 5:
            print("Too close")
        else:
            print("Too High")


    elif comp_number > user_number:

        if comp_number - user_number  > 0 and comp_number - user_number <= 5:
            print("Too close")
        else:
            print("Too Low")

    elif comp_number == user_number:
        print("You win")

    else:
        print("Error: Invalid choice")

except ValueError:
    print("Invalid input. Please enter a valid number.")



# today i explored modules function, try and except, variables, type conversion, usage of math and random module, if else statement, and nested if else statement by building simple number quessing game project in python.