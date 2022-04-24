from in_game_settings import classes
#from classes import WhitePawn
from test_code import WhitePawn
# Classes for each of the pieces
class WhitePawn():
    def __init__(self, gameboard, position, end_position):
        self.gameboard = gameboard
        self.s = position
        self.d = end_position

    def double_space(self):
        pass

    def single_space(self):
        LETTERS = 'ABCDEFGH'

        source = self.gameboard[8 - int(self.s[1])][LETTERS.index(self.s[0])]
        destination = self.gameboard[8 - int(self.d[1])][LETTERS.index(self.d[0])]

        source.replace(source, destination)
        destination.replace(destination, source)

        return self.gameboard

        

    def attack_left(self):
        pass

    def attack_right(self):
        pass

    def remove(self):
        pass

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
            COORDINATE = "ABCDEFGH"
            current_position = input("Input current position (ex. B5):\n")
            end_position = input('Where would you like to go (ex: C3):\n')
            piece = gameboard[8 - int(current_position[1])][COORDINATE.index(current_position[0])]
            if piece in whiteUnits:
                player = classes[piece]
            
            elif piece in blackUnits:
                player = classes[piece()]
            else:
                print('Invalid Pick')
            #Done on new Patch
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
    