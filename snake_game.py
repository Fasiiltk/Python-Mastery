# snake_game.py
import random

grid = [[" " for _ in range(5)] for _ in range(5)]
snake = [(2, 2)]
food = (random.randint(0, 4), random.randint(0, 4))
direction = "right"

while True:
    # Display grid
    for i in range(5):
        for j in range(5):
            if (i, j) in snake:
                print("S", end=" ")
            elif (i, j) == food:
                print("F", end=" ")
            else:
                print(".", end=" ")
        print()
    
    move = input("Move (up/down/left/right): ").lower()
    head = snake[0]
    if move == "up": new_head = (head[0] - 1, head[1])
    elif move == "down": new_head = (head[0] + 1, head[1])
    elif move == "left": new_head = (head[0], head[1] - 1)
    else: new_head = (head[0], head[1] + 1)

    if not (0 <= new_head[0] < 5 and 0 <= new_head[1] < 5) or new_head in snake:
        print("Game Over!")
        break
    snake.insert(0, new_head)
    if new_head == food:
        food = (random.randint(0, 4), random.randint(0, 4))
    else:
        snake.pop()