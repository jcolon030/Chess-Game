from classes import WhitePawn, BlackPawn
from in_game_settings import classes
from config import *



def print_main_board(gameboard):
    print('\n')
    print("-" * 41)
    for row in gameboard:
        print(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]} |")
        print(f'-' * 41)
    print('\n')

def starting_menu():
    starting = '''
    
    (1) Play against a computer
    (2) Play against a friend
    (3) Quit 
    (4) Dev Tools 

    '''
    return starting

def option_tree(selection):
    if selection == '1':
        pass
    elif selection == '2':
        againstFriend = True
        whitesTurn = True
        turn = 0
        while againstFriend != False:
            print_main_board(gameboard)
            coordinate = ["A", "B", "C", "D", "E", "F", "G", "H"]
            current_position = input("Input current position (ex. B5):\n")
            end_position = input('Where would you like to go (ex: C3):\n')
            piece = gameboard[8 - int(current_position[1])][coordinate.index(current_position[0])]
            end_index = cordPlaneDict[end_position]
            if piece in whiteUnits:
                if WhitePawn:
                    player = classes[piece]
                    if end_index == cordPlaneDict[str(current_position[0]) + str(int(current_position[1]) + 1)]: # try statement for far end of board (out of index)
                            player(gameboard, cordPlane, current_position, end_position, cordPlaneDict).single_space()
                    elif end_index == cordPlaneDict[str(current_position[0]) + str(int(current_position[1]) + 2)] and current_position[1] == '2':
                        player(gameboard, cordPlane, current_position, end_position, cordPlaneDict).double_space()
                    else:
                        print('Invalid Move')
                else:
                    print("Please select again")
            elif piece in blackUnits:
                if BlackPawn:
                    player = classes[piece]
                    S1 = coordinate.index(current_position[0])
                    S2 = str(f'{coordinate[S1]}{str(int(current_position[1]) + 1)}')
                    if end_position == S2:
                        player(gameboard, cordPlane, current_position, end_position).single_space()
                        turn += 1
                    else:
                        print('Invalid Move')
            else:
                print('Invalid Pick')
            #Done on new Patch
    elif selection == '3':
        game = False
        return game
    

def main():
    game = True
    while game != False:
        print(cordPlaneDict)
        print(starting_menu())
        selection = input('Please pick a choice: ')
        option_tree(selection)
        

if __name__ == "__main__":
    main()
    