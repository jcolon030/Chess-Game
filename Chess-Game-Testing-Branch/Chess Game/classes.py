# Classes for each of the pieces
from config import *

class WhitePawn():
    def __init__(self, gameboard, cordPlane, position, end_position, cordPlaneDict):
        self.gameboard = gameboard
        self.s = position
        self.d = end_position
        self.cordPlane = cordPlane
        self.Dict = cordPlaneDict 

    def double_space(self):
        column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        numEquivalentS = column.index(self.s[0])
        numEquivalentD = column.index(self.d[0]) 

        source = self.gameboard[8 - int(self.s[1])][numEquivalentS]
        destination = self.gameboard[8 - int(self.d[1])][numEquivalentD]


        S1 = 8 - int(self.s[1])
        S2 = numEquivalentS
        D1 = 8 - int(self.d[1])
        D2 = numEquivalentD

        self.gameboard[S1][S2] = '  '
        self.gameboard[D1][D2] = source 
        
        return self.gameboard
    
    def single_space(self):
        column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        numEquivalentS = column.index(self.s[0])
        numEquivalentD = column.index(self.d[0]) 

        source = self.gameboard[8 - int(self.s[1])][numEquivalentS]
        destination = self.gameboard[8 - int(self.d[1])][numEquivalentD]


        S1 = 8 - int(self.s[1])
        S2 = numEquivalentS
        D1 = 8 - int(self.d[1])
        D2 = numEquivalentD

        self.gameboard[S1][S2] = '  '
        self.gameboard[D1][D2] = source 
        
        return self.gameboard

    def attack_left(self):
        pass

    def attack_right(self):
        pass

    def remove(self):
        pass

class BlackPawn():
    def __init__(self, gameboard, cordPlane, position, end_position):
        self.gameboard = gameboard
        self.s = position
        self.d = end_position
        self.cordPlane = cordPlane

    def double_space(self):
        pass

    def single_space(self):
        column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        numEquivalentS = column.index(self.s[0])
        numEquivalentD = column.index(self.d[0]) 

        source = self.gameboard[int(self.s[1])][numEquivalentS]
        destination = self.gameboard[int(self.d[1])][numEquivalentD]

        S1 = int(self.s[1])
        S2 = numEquivalentS
        D1 = int(self.d[1])
        D2 = numEquivalentD

        self.gameboard[S1][S2] = ' '
        self.gameboard[D1][D2] = source
        
        return self.gameboard

    def attack_left(self):
        pass

    def attack_right(self):
        pass

    def remove(self):
        pass



if __name__ == "__main__":
    my_pawn = WhitePawn(gameboard=gameboard,
                        cordPlane=cordPlane,
                        position="A2",
                        end_position="-")
    print(my_pawn.__dict__["gameboard"])
    my_pawn.double_space()
    print(my_pawn.__dict__["gameboard"])
