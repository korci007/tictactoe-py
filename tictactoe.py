import os


def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


# Display a small guide
def display_guide():
    print('Placement positions for the game are:')
    print('7|8|9\n4|5|6\n1|2|3')


# returns the order of players
def chose_player():
    valid_choices = ['X', 'O']
    choice = 'WRONG'

    while choice not in valid_choices:
        choice = input("Player 1 please choose 'X' or 'O' :")

    print(f"\nPlayer 1 has chosen option {choice!r}.")

    if choice == 'X':
        return 'P1', 'P2'
    else:
        return 'P2', 'P1'


# Drawing the board
def display_board(move_db, order):
    clean()
    row_a = [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' \n']
    row_b = ['-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-\n']
    board = [row_a[:], row_a[:], row_a[:], row_b[:],
             row_a[:], row_a[:], row_a[:], row_b[:],
             row_a[:], row_a[:], row_a[:]]
    # coordinates for 'X' and 'O' placements
    positions = {1: [9, 1], 2: [9, 5], 3: [9, 9],
                 4: [5, 1], 5: [5, 5], 6: [5, 9],
                 7: [1, 1], 8: [1, 5], 9: [1, 9]}

    # place 'X' on all his/her coordinates for the player who started first
    for move in move_db[order[0]]:
        board[positions[move][0]][positions[move][1]] = 'X'

    # place 'O' for the player who started 2nd
    for move in move_db[order[1]]:
        board[positions[move][0]][positions[move][1]] = 'O'

    # Draw the board
    str_out = ''
    for place in board:
        str_out += ''.join(place)
    print(str_out)


def user_choice(player, db):
    valid_options = list(range(1, 10))
    valid_input = False

    while not valid_input:
        display_guide()
        move = int(input(f'{player} please enter a move (1-9): '))
        if move in valid_options and move not in db[player]:
            db[player].append(move)
            valid_input = True
        else:
            print('Move not valid (1-9)')
    return db


# If someone won, the party is finished. Check moves against the winning patters.
def party_finished(player, player_moves):
    win_patterns = ({1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7})
    for pattern in win_patterns:
        # check if one of the winning paters is a subset of the moves from one of the players
        # using sets so the input order does not matter
        if pattern.issubset(set(player_moves[player])):
            print(f'Player {player[1]} wins!\n')
            return True
        # check to see if the game was a draw
        elif len(player_moves[player]) == 5:
            print('The game was a draw!\n')
            return True
    return False


#  Check if the players want to start a new game.
def finish_playing():
    options = ['Yes', 'No']
    play_more = 'WRONG'
    while play_more not in options:
        play_more = input("Do you want to play another game? (Yes/No) : ")
        if play_more not in options:
            print("Please enter 'Yes' or 'No' : ")
        else:
            if play_more == 'No':
                print('\nSee you next time!\n')
                return True
            else:
                return False


# Let's start this party
def party():
    # record all the moves players make
    moves = {'P1': [], 'P2': []}
    # determine the order
    order = chose_player()

    # here comes the game loop: draw, chose, test
    display_board(moves, order)
    while True:
        user_choice(order[0], moves)
        display_board(moves, order)
        if party_finished(order[0], moves):
            break
        user_choice(order[1], moves)
        display_board(moves, order)
        if party_finished(order[1], moves):
            break


# Game starts here    
while True:
    clean()

    party()

    if finish_playing():
        break
