import os
from xml.dom import UserDataHandler

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

# returns the order of players
def chose_player():
    valid_choices = ['X','O']
    choice = 'WRONG'
    
    while choice not in valid_choices:
        choice = input("Player 1 please choose 'X' or 'O' :")

    print(f"\nPlayer 1 has chosen option {choice!r}.") 
    
    if choice == 'X':
        return ('P1','P2')
    else:
        return ('P2','P1')


def display_board(movedb):
    clean()
    print(f"Player 1 moves: { movedb['P1'] }")
    print(f"Player 2 moves: { movedb['P2'] }")


def user_choice(player, movedb):
    valid_options = list(range(1,10))
    valid_input = False

    while not valid_input:
        move = int(input('Enter a move: '))
        if move in valid_options and move not in movedb[player]:      
            movedb[player].append(move)
            valid_input = True
        else:
            print('Move not valid (1-9)')
    return movedb
   


def party_finished(player,player_moves):
    '''
    If someone won, the party is finished. Check moves against the winning patters.
    '''
    win_patterns = ({1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7})
    for pattern in win_patterns:
        if pattern.issubset(set(player_moves[player])):
            print(f'Player {player} wins!')
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
                print('Good Bye!')
                return True
            else:
                return False

def party():
    # recod all the moves players make
    moves = {'P1':[],'P2':[]}
    # determine the order
    order = chose_player()
    
    #here comes the game loop: draw, chose, test
    party_on = True
    while party_on:
        display_board(moves)
        user_choice(order[0], moves)
        display_board(moves)
        party_finished(order[0],moves)
        user_choice(order[1], moves)
        display_board(moves)
        party_finished(order[1],moves)


# Game starts here    
game_on = True

while game_on: 
    clean()
    
    party()

    if finish_playing():
        break

##Test are
#moves = {'P1':[1,2],'P2':[7]}
#order = ('P1','P2')

#print(moves.values())

#user_choice(order[0],moves)

#print(moves)