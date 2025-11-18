import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import random

# ---------------- GAME VARIABLES --------------------
current_player = "X"           # Human starts
board = [""] * 9
game_over = False


# --------------- CHECK WINNER -----------------------
def check_winner():
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a,b,c in win_patterns:
        if board[a] == board[b] == board[c] != "":
            return board[a]  # "X" or "O"

    if "" not in board:
        return "Draw"

    return None


# --------------- COMPUTER MOVE -----------------------
def computer_move():
    global current_player, game_over

    if game_over:
        return

    empty_cells = [i for i, v in enumerate(board) if v == ""]
    if not empty_cells:
        return

    move = random.choice(empty_cells)
    board[move] = "O"

    buttons[move].config(text="O", bootstyle="danger")

    winner = check_winner()
    if winner:
        finish_game(winner)
        return

    current_player = "X"


# --------------- HUMAN CLICK -------------------------
def on_click(index):
    global current_player, game_over

    if game_over:
        return

    if board[index] != "":
        return

    if current_player == "X":
        board[index] = "X"
        buttons[index].config(text="X", bootstyle="success")

        winner = check_winner()
        if winner:
            finish_game(winner)
            return

        current_player = "O"
        app.after(500, computer_move)  # delay for realism


# --------------- FINISH GAME -------------------------
def finish_game(winner):
    global game_over
    game_over = True

    if winner == "Draw":
        messagebox.showinfo("Result", "😄 Match Draw!")
    elif winner == "X":
        messagebox.showinfo("Winner", "🎉 YOU WIN! (Player X)")
    else:
        messagebox.showinfo("Winner", "🤖 Computer Wins! (Player O)")


# ---------------- RESET GAME -------------------------
def reset_game():
    global board, current_player, game_over
    board = [""] * 9
    current_player = "X"
    game_over = False

    for btn in buttons:
        btn.config(text="", bootstyle="primary")


# ---------------- GUI SETUP --------------------------
app = ttk.Window(themename="superhero")
app.title("OX Game – Human vs Computer (3D GUI)")
app.geometry("400x450")

title = ttk.Label(app, text="🎮 O-X Game (Human vs Computer)",
                  font=("Arial", 20, "bold"), bootstyle="info")
title.pack(pady=20)

frame = ttk.Frame(app)
frame.pack()

buttons = []

for i in range(9):
    btn = ttk.Button(
        frame,
        text="",
        width=8,
        bootstyle="primary-outline",
        command=lambda i=i: on_click(i)
    )
    btn.grid(row=i//3, column=i%3, padx=10, pady=10, ipadx=10, ipady=10)
    buttons.append(btn)

reset_btn = ttk.Button(app, text="Reset Game",
                       bootstyle="warning-outline", command=reset_game)
reset_btn.pack(pady=20)

app.mainloop()
