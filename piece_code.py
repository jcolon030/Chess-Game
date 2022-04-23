COORDINATE = "ABCDEFGH"
current_position = input("Input current position (ex. B5:) ")
piece = gameboard[8 - int(current_position[1])][COORDINATE.index(current_position[0])]
