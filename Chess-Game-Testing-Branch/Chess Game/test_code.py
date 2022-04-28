from numpy import *
import numpy as np
from config import *
'''
elif end_position == doublePushPosition:
                        player(gameboard, cordPlane, current_position, end_position).double_space(turn)
                        turn += 1

'''


if __name__ == "__main__":

    gameboard = np.array([['A8','B8','C8','D8','E8','F8','G8','H8'],\
                          ['A7','B7','C7','D7','E7','F7','G7','H7'],\
                          ['A6','B6','C6','D6','E6','F6','G6','H6'],\
                          ['A5','B5','C5','D5','E5','F5','G5','H5'],\
                          ['A4','B4','C4','D4','E4','F4','G4','H4'],\
                          ['A3','B3','C3','D3','E3','F3','G3','H3'],\
                          ['A2','B2','C2','D2','E2','F2','G2','H2'],\
                          ['A1','B1','C1','D1','E1','F1','G1','H1']])

    cordPlaneDict = {}
    for i in range(8):
        for j in range(8):
            cordPlaneDict[gameboard[7 - i][j]] = (i,j)  
    
    print(cordPlaneDict)


'''
for i in range(8):
    for j in range(8):
        print((i, j), end=' ')
    print('\n')
    '''

'''

            source = cordPlaneDict[self.s]
            destination = (source[0]-2, source[1])



            self.gameboard[source[0]][source[1]] = '  '
            self.gameboard[destination[0]][destination[1]] = source
        
            return self.gameboard
'''