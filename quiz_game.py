# quiz_game.py
questions = {
    "What is 2 + 2?": ["4", "3", "5", "6"],
    "What color is the sky?": ["Blue", "Green", "Red", "Yellow"]
}
answers = ["4", "Blue"]
score = 0

for i, (q, options) in enumerate(questions.items()):
    print(q)
    for j, opt in enumerate(options, 1):
        print(f"{j}. {opt}")
    ans = input("Your answer (1-4): ")
    if options[int(ans) - 1] == answers[i]:
        score += 1

print(f"Your score: {score}/{len(questions)}")