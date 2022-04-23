
blackUnits = ['bR','bN','bB','bK','bQ','bB','bN','bR','bp']
whiteUnits = ['wR','wN','wB','wK','wQ','wB','wN','wR','wp']

gameboard = [['bR','bN','bB','bK','bQ','bB','bN','bR'],\
             ['bp','bp','bp','bp','bp','bp','bp','bp'],\
             ['  ','  ','  ','  ','  ','  ','  ','  '],\
             ['  ','  ','  ','  ','  ','  ','  ','  '],\
             ['  ','  ','  ','  ','  ','  ','  ','  '],\
             ['  ','  ','  ','  ','  ','  ','  ','  '],\
             ['wp','wp','wp','wp','wp','wp','wp','wp'],\
             ['wR','wN','wB','wK','wQ','wB','wN','wR']]

backupgameboard = [['bR','bN','bB','bK','bQ','bB','bN','bR'],\
                   ['bp','bp','bp','bp','bp','bp','bp','bp'],\
                   ['  ','  ','  ','  ','  ','  ','  ','  '],\
                   ['  ','  ','  ','  ','  ','  ','  ','  '],\
                   ['  ','  ','  ','  ','  ','  ','  ','  '],\
                   ['  ','  ','  ','  ','  ','  ','  ','  '],\
                   ['wp','wp','wp','wp','wp','wp','wp','wp'],\
                   ['wR','wN','wB','wK','wQ','wB','wN','wR']]

cordPlane = [['A8','B8','C8','D8','E8','F8','G8','H8'],\
             ['A7','B7','C7','D7','E7','F7','G7','H7'],\
             ['A6','B6','C6','D6','E6','F6','G6','H6'],\
             ['A5','B5','C5','D5','E5','F5','G5','H5'],\
             ['A4','B4','C4','D4','E4','F4','G4','H4'],\
             ['A3','B3','C3','D3','E3','F3','G3','H3'],\
             ['A2','B2','C2','D2','E2','F2','G2','H2'],\
             ['A1','B1','C1','D1','E1','F1','G1','H1']]


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
        while againstFriend != False:
            print_main_board(gameboard)
            current_move = input('Please input your position (current position):\n')
            for i in cordPlane:
                for j in i:
                    player_position = cordPlane[j].index(current_move)
            player_piece = gameboard.index(player_position)
            move = input('Where would you like to move:\n')
            print(player_piece)
    elif selection == '3':
        game = False
        return game
    

def main():
    game = True
    while game != False:
        print(starting_menu())
        selection = input('Please pick a choice: ')
        option_tree(selection)
        

if __name__ == "__main__":
    main()
    