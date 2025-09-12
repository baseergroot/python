from random  import random, randint
from math import floor


lower_range = int(input("Enter the lower range: "))
higher_range = int(input("Enter the higher range: "))

if lower_range > higher_range:
    print("Incorrect range: lower_range can not be greater that higher_range")
    
else:
    comp_number = randint(lower_range, higher_range)

    for i in range(3):
        try:
            user_number = int(input("Quess number between 1 - 100: "))

            if comp_number < user_number:
                
                if user_number - comp_number > 0 and user_number - comp_number <= 6:
                    print("close")
                elif user_number - comp_number > 0 and user_number - comp_number <= 3:
                    print("Too close")
                else:
                    print("Too High")

            elif comp_number > user_number:

                if comp_number - user_number  > 0 and comp_number - user_number <= 6:
                    print("Close")
                elif comp_number - user_number  > 0 and comp_number - user_number <= 3:
                    print("Too close")
                else:
                    print("Too Low")

            elif comp_number == user_number:
                print("You win")

            else:
                print("Error: Invalid choice")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("computer selection was " , comp_number)


# today i explored modules function, try and except, variables, type conversion, usage of math and random module, if else statement, and nested if else statement, for in loop, by building simple number quessing game project in python.