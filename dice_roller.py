# dice_roller.py
import random

num_dice = int(input("How many dice to roll? "))
for _ in range(num_dice):
    roll = random.randint(1, 6)
    print(f"Dice roll: {roll}")