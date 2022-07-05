import os

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def chose_player():
    '''
    Determine the order of players in the game
    '''
    valid_choices = ['X','O']
    choice = 'WRONG'
    
    while choice not in valid_choices:
        choice = input("Player 1 please choose 'X' or 'O' :")

    print(f"\nPlayer 1 has chosen option {choice!r}.") 
    
    if choice == 'X':
        return ('P1','P2')
    else:
        return ('P2','P1')


def initialize_records(order,player1,player2):
    '''
    Initialize player records
    '''
    if order == ('P1','P2'):
        print("Player 1 starts the game with 'X'!\n")
        set_player('X',player1)
        set_player('O',player2)
    else:
        print("Player 2 starts the game with 'X'!\n")
        set_player('O',player1)
        set_player('X',player2)


def set_player(value,player):
    '''
    Set X or O to the chosen player as the first value
    '''
    return player.append(value)       


def display_board(p1,p2):
    clean()
    print(f'Player 1 moves: {p1}')
    print(f'Player 2 moves: {p2}')


def user_choice():
    pass


def party_finished(player_moves):
    '''
    If someone won, the party is finished. Check moves against the winning patters.
    '''
    win_patterns = ({1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7})
    for pattern in win_patterns:
        if pattern.issubset(set(player_moves)):
            print('Player wins!')
            return True
    return False


def finish_playing():
    '''
    Check if the players want to start a new game.
    '''
    options = ['Yes','No']
    play_more = 'WRONG'
    while play_more not in options:
        play_more = input("Do you want to play another game? (Yes/No) :")
        if play_more not in options:
            print("Please enter 'Yes' or 'No' : ")
        else:
            if play_more == 'No':
                return True
            else:
                return False

def party():
    # recod all the moves players make
    p1_moves = []
    p2_moves = []
    # determine the order
    order = chose_player()
    initialize_records(order, p1_moves, p2_moves)

    #here comes the game loop: draw, chose, test
    party_on = True
    while party_on:
        display_board(p1_moves,p2_moves)
        break
        #user_choice(order[0])
        #party_finished()
        #user_choice(order[1])
        #party_finished()


# Game starts here    
game_on = True

while game_on: 
    clean()
    
    party()

    if finish_playing():
        break

print('Good Bye!')

