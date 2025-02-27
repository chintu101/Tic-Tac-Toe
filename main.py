import numpy as np
import random
from time import sleep
import tkinter as tk
from tkinter import messagebox

def create_board():
    return np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])

def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return l

def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return board

def row_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue
        if win:
            return win
    return win


def col_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue
        if win:
            return win
    return win

def diag_win(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != player:
                win = False
    return win

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if (row_win(board, player) or
                col_win(board, player) or
                diag_win(board, player)):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    sleep(2)

    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print("Board after " + str(counter) + " move")
            print(board)
            sleep(2)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break

    return winner

def update_board(button, row, col):
    global current_player, game_board, counter

    if game_board[row][col] == 0:
        game_board[row][col] = current_player
        button.config(text="X" if current_player == 1 else "O")
        counter += 1

        if evaluate(game_board) == 0:
            if counter == 9:
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                reset_game()
            else:
                current_player = 3 - current_player  # Switch player
        else:
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_game()

def reset_game():
    global game_board, current_player, counter

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=tk.NORMAL)

    game_board = create_board()
    current_player = 1
    counter = 0

# GUI setup
root = tk.Tk()
root.title("Tic-Tac-Toe")

game_board = create_board()
current_player = 1
counter = 0

buttons = [[None, None, None] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Helvetica", 24), width=6, height=3,
                                  command=lambda row=i, col=j: update_board(buttons[row][col], row, col))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()