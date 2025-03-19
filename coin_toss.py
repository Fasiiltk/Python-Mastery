# coin_toss.py
import random

tosses = int(input("How many times to toss the coin? "))
results = {"Heads": 0, "Tails": 0}

for _ in range(tosses):
    result = random.choice(["Heads", "Tails"])
    results[result] += 1

print(f"Heads: {results['Heads']}, Tails: {results['Tails']}")