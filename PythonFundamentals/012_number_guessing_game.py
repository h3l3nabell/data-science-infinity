"""
  Number Guessing Game
"""

# Version 1
import random
CORRECT_NUMBER = 26

user_guess = int(input("Guess a number: "))


if user_guess == CORRECT_NUMBER:
    print("Wow! you won!")
else:
    print("Sorry, better luck next time!")

# Verison 2
CORRECT_NUMBER = 26

while True:
    user_guess = int(input("Guess a number: "))

    if user_guess == CORRECT_NUMBER:
        print("Wow! you won!")
    else:
        print("Sorry, better luck next time!")

# Version 3
LOWER_BOUND = 1
UPPER_BOUND = 100
GUESS_LIMIT = 5
GUESS_COUNTER = 0
CORRECT_NUMBER = random.randint(LOWER_BOUND, UPPER_BOUND)

print("Try to guess the number I'm thinking of.")
print(f"It is between {LOWER_BOUND} and {UPPER_BOUND}.")
print(f"You have {GUESS_LIMIT} guesses.  Good Luck!")

while GUESS_COUNTER < GUESS_LIMIT:
    user_guess = int(input("Guess a number: "))
    GUESS_COUNTER += 1
    remaining_guesses = GUESS_LIMIT - GUESS_COUNTER
    if user_guess == CORRECT_NUMBER:
        print("Wow! you won in {GUESS_COUNTER} guesses!")
        break
    elif user_guess > CORRECT_NUMBER:
        print(f"{user_guess} is too high")
        print(
            f"Try again, you have {remaining_guesses} guesses left")
    else:
        print(f"{user_guess} is too low")
        print(
            f"Try again, you have {remaining_guesses} guesses left")

print("Sorry, you have no more guesses. Better luck next time!")
print(f"The number was {CORRECT_NUMBER}")
