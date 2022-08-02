import itertools

def win(current_game):
    
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    # Horizontal
    for line in game:
        print(line)
        if all_same(line):
           print(f"Player {line[0]} won the game Horizontally")
           return True

    # Diagonal
    diagonals = []
    for col, row, in enumerate(reversed(range(len(game)))):
        diagonals.append(game[row][col])
    if all_same(diagonals):
        print(f"Player {diagonals[0]} won the game Diagonally!")
        return True

    diagonals = []
    for i in range(len(game)):
        diagonals.append(game[i][i])
    if all_same(diagonals):
        print(f"Player {diagonals[0]} won the game Diagonally!")
        return True


    # Vertical
    for col in range(len(game)):
        check = []

        for line in game:
            check.append(line[0])

        if all_same(check):
            print(f"Player {check[0]} won the game Vertically!")
            return True
    return False


def tictactoe(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This place is occupied!, Try another!")
            return game_map, False
        s = "   "+"  ".join([str(i) for i in range(len(game_map))])
        if not just_display:
            game_map[row][column] = player
        for count, lines in enumerate(game_map):
            print(count, lines)
        return game_map, True
    except IndexError as x:
        print("Error: make sure you input row or column as 0, 1, 2?", x)
        return game_map, False

    except Exception as x:
        print("Something went very wrong!", x)
        return game_map, False

play = True
players = [1, 2]
while play:
    game_size = int(input("What size of game you want to play?: "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]

    game_won = False
    game, _ = tictactoe(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            game, played = tictactoe(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n): ")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("Bye")
                play = False
            else:
                print("Not a valid answer")
                playe = False