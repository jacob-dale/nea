from shared import *
from pieces import *


class Player:
    def __init__(self, is_black):  # gives the pieces a parameter to determine there colour
        self._is_black = is_black
        self._pieces = []  # creates arrays to store the pieces
        rank = 2
        if self._is_black:  # determines the pawns starting rank
            rank = 7
        for i in range(8):
            file = shared.files[i]
            self._pieces.append(Pawn(Square(file, rank), is_black))  # adds the pawns to the piece array for the player

        if self._is_black:  # determines the kings starting rank
            rank = 8
        else:
            rank = 1
        file = shared.files[4]
        self._pieces.append(King(Square(file, rank), is_black))  # creates a king

        file = shared.files[3]
        self._pieces.append(Queen(Square(file, rank), is_black))  # creates a queen

        file = shared.files[2]
        self._pieces.append(Bishop(Square(file, rank), is_black))  # creates the bishops
        file = shared.files[5]
        self._pieces.append(Bishop(Square(file, rank), is_black))

        file = shared.files[1]
        self._pieces.append(Knight(Square(file, rank), is_black))  # creates the knights
        file = shared.files[6]
        self._pieces.append(Knight(Square(file, rank), is_black))

        file = shared.files[0]
        self._pieces.append(Rook(Square(file, rank), is_black))  # creates the rooks
        file = shared.files[7]
        self._pieces.append(Rook(Square(file, rank), is_black))

    def draw(self):
        if self._is_black:
            print("Draw the black pieces")
        else:
            print("Draw the white pieces")
        for piece in self._pieces:
            piece.draw_piece(shared.win)