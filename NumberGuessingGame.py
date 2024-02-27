# -------------------Number Guessing Game-------------------

import random
attempts = 0
maxRangeNumber = int(input("Enter the maximum number of the range : "))
randomNumber = random.randint(0, maxRangeNumber)

# check the number validation 
if maxRangeNumber <= 0 :
    print("Enter the input is graterthan 0")
    quit()

while True:
    userInput = int(input(f"\nEnter the number between {0} to {maxRangeNumber} : "))
    attempts += 1
    if userInput == randomNumber:
        print(f"{userInput} is correct")
        break

    else:
        print("Your guessing is incorrect, Your guessing number")
        if userInput > randomNumber:
            print(f"{userInput} is too high")
        else:
            print(f"{userInput} is too low")


print(f"You guess the correct value in {attempts} attempts")