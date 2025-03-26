# rock_paper_scissors.py
import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)

user = input("Enter rock, paper, or scissors: ").lower()
print(f"Computer chose: {computer}")

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "scissors" and computer == "paper") or \
     (user == "paper" and computer == "rock"):
    print("You win!")
else:
    print("Computer wins!")