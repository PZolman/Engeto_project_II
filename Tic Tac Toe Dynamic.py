import itertools

border = ("|")
floor = ("--")
star = ("*")
triplestar = ("***")

def separ():
    print(("=")*30)

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

def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return

# Horizontal win
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True

# Diagonals win
    diags = []
    for col, row in (enumerate(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (/)!")
        return True

    diags = []
    for i in range(len(game)):
        diags.append(game[i][i])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (\\)!")
        return True

# Vertical win
    vertic = []
    for col in range(len(game)):
        for row in game:
            vertic.append(row[col])
        if all_same(vertic):
            print(f"Player {vertic[0]} is the winner vertically (|)!")
            return True

    return False

# Game logic

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is used! Chosse another one!")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
             game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError as e:
        print("Error? make sure you input row/column as 0 1 or 2?", e)
        return game_map, False

    except Exception as e:
        print("Something went very wrong", e)
        return game_map, False

# Game variables
play = True
players = [1, 2]
border = ("|")
while play:
    game_size = int(input("Please enter game size of Tic Tac Toe:  "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play?: "))
            row_choice = int(input("What row do you want to play?: "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n)")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Good Bye")
                play = False
            else:
                print("Not a valid answer")
                play = False
