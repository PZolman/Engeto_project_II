# Formatting variables
border = ("|")
floor = ("--")
star = ("*")
triplestar = ("***")

# Separator fnc
def separ():
    print(("=")*30)

# board display fnc
def board_print():
    board_display = ("T1{0}T2{0}T3"'\n'"{1} {1} {1}"'\n'"M1{0}M2{0}M3"'\n'"{1} {1} {1}"'\n'"D1{0}D2{0}D3\n").format(border,floor)
    print("This is a game board")
    print(board_display)

separ()
print("Welcome to Tic Tac Toe Game")
separ()
print("{0}GAME RULES{0}".format(border))
print("""
At first of all you can choose size of game map
Then each player can place one mark (or stone) per turn on the 3x3 grid.
The WINNER is who succeeds in placing stones of their marks in a
{0} horizontal,
{0} vertical or
{0} diagonal row

{1} Let's start the game {1}
""".format(star,triplestar))

separ()

# Game variables
board = {
    "T1": " ", "T2": " ", "T3": " ",
    "M1": " ", "M2": " ", "M3": " ",
    "D1": " ", "D2": " ", "D3": " ",
        }
player = 1
total_moves = 0
end_check = 0

def check():
# Checking win of player one: "X"
# Horizontal
    if board["T1"] == "X" and board["T2"] == "X" and board["T3"] == "X":
        print("Player one won horizontally (-)!")
        return 1
    if board["M1"] == "X" and board["M2"] == "X" and board["M3"] == "X":
        print("Player one won horizontally (-)!")
        return 1
    if board["D1"] == "X" and board["D2"] == "X" and board["D3"] == "X":
        print("Player one won horizontally (-)!")
        return 1

# Diagonal
    if board["T1"] == "X" and board["M2"] == "X" and board["D3"] == "X":
        print("Player one won diagonally (/)!")
        return 1
    if board["T3"] == "X" and board["M2"] == "X" and board["D1"] == "X":
        print("Player one won diagonally (\\)!")
        return 1

# Vertical
    if board["T1"] == "X" and board["M1"] == "X" and board["D1"] == "X":
        print("Player one won vertically (|)!")
        return 1
    if board["T2"] == "X" and board["M2"] == "X" and board["D2"] == "X":
        print("Player one won vertically (|)!")
        return 1
    if board["T3"] == "X" and board["M3"] == "X" and board["D3"] == "X":
        print("Player one won vertically (|)!")
        return 1

# Checking win of player Two: "O"
# Horizontal
    if board["T1"] == "0" and board["T2"] == "O" and board["T3"] == "O":
        print("Player two won horizontally (-)!")
        return 1
    if board["M1"] == "O" and board["M2"] == "O" and board["M3"] == "O":
        print("Player two won horizontally (-)!")
        return 1
    if board["D1"] == "O" and board["D2"] == "O" and board["D3"] == "O":
        print("Player two won! horizontally (-)!")
        return 1

# Diagonal
    if board["T1"] == "O" and board["M2"] == "O" and board["D3"] == "O":
        print("Player two won diagonally (/)!")
        return 1
    if board["T3"] == "O" and board["M2"] == "O" and board["D1"] == "O":
        print("Player two won diagonally (\\)!")
        return 1

# Vertical
    if board["T1"] == "O" and board["M1"] == "O" and board["D1"] == "O":
        print("Player two won vertically (|)!")
        return 1
    if board["T2"] == "O" and board["M2"] == "O" and board["D2"] == "O":
        print("Player two won vertically (|)!")
        return 1
    if board["T3"] == "O" and board["M3"] == "O" and board["D3"] == "O":
        print("Player two won vertically (|)!")
        return 1
    return 0

board_print()
separ()

# Game logic
while True:
    print(board["T1"] + "|" + board["T2"] + "|" + board["T3"])
    print("-+-+-")
    print(board["M1"] + "|" + board["M2"] + "|" + board["M3"])
    print("-+-+-")
    print(board["D1"] + "|" + board["D2"] + "|" + board["D3"])
    end_check = check()
    if total_moves == 9 or end_check == 1:
        break
    while True:
        if player == 1:
            p1_input = input("Player one ""X"": ")
            if p1_input.upper() in board and board[p1_input.upper()] == " ":
                board[p1_input.upper()] = "X"
                player = 2
                break
            else:
                print("Invalid input, please try again")
                continue
        else:                       #player two
            p2_input = input("Player two ""0"": ")
            if p2_input.upper() in board and board[p2_input.upper()] == " ":
                board[p2_input.upper()] = "O"
                player = 1
                break
            else:
                print("Invalid input, please try again")
                continue

    total_moves += 1
