# guess_the_number.py
import random

number = random.randint(1, 100)
guesses = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Correct! It took you {guesses} guesses.")
        break