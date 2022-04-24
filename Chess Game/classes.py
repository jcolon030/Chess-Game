# Classes for each of the pieces


class WhitePawn():
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

        source = self.gameboard[8 - int(self.s[1])][numEquivalentS]
        destination = self.gameboard[8 - int(self.d[1])][numEquivalentD]

        S1 = 8 - int(self.s[1])
        S2 = numEquivalentS
        D1 = 8 - int(self.d[1])
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
