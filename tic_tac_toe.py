# tic_tac_toe.py
board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("-" * 9)

def check_win(player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

player = "X"
while " " in board:
    print_board()
    move = int(input(f"Player {player}, enter position (0-8): "))
    if board[move] == " ":
        board[move] = player
        if check_win(player):
            print_board()
            print(f"Player {player} wins!")
            break
        player = "O" if player == "X" else "X"
else:
    print_board()
    print("It's a draw!")