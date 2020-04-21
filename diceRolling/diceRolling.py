import random

print("Rolling dice simulator !!!")

finish = "y"
while finish == "y":

    sum = 0
    dices = input("How many dices do you want to roll?: ")

    # Check if numeric user input
    if dices.isdigit():
        # User input is str, cast to int
        dices = int(dices)
        # Generate random numbers for all dices        
        for i in range(dices):
            dice = random.randint(1,6)
            print(dice, end=" ")
            # Make a sum of all dices
            sum += dice

        print()  # New Line
        print(f"All together, you rolled: {sum}")
        print(f"The average of the rolls is {sum/dices}")
        finish = input("Do you want to play again? (y/n)")
    else:
        print("I need a number")
