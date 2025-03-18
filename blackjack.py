# blackjack.py
import random

player = [random.randint(1, 10), random.randint(1, 10)]
dealer = [random.randint(1, 10), random.randint(1, 10)]

print(f"Your cards: {player}, Total: {sum(player)}")
while sum(player) < 21 and input("Hit? (y/n): ").lower() == "y":
    player.append(random.randint(1, 10))
    print(f"Your cards: {player}, Total: {sum(player)}")

print(f"Dealer's cards: {dealer}, Total: {sum(dealer)}")
if sum(player) > 21:
    print("Bust! You lose!")
elif sum(dealer) > 21 or sum(player) > sum(dealer):
    print("You win!")
else:
    print("Dealer wins!")