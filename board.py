import shared
from graphics import *

class Square:
    _file = "a"
    _rank = 1

    def __init__(self, file, rank):  # gives squares the parameters of file and rank
        self._file = file
        self._rank = rank

    def get_file(self):  # returns the file of a square
        return self._file

    def get_file_as_int(self):  # returns the file of a square as an integer
        return ord(self._file) - ord("a") + 1  # ord returns the character code of the requested character

    def get_rank(self):  # returns the rank of a square
        return self._rank


class Board:
    def draw(self):  # draws the board
        for i in range(8):
            for j in range(8):
                rect = Rectangle(Point(100 + j * 50, 100 + i * 50), Point(150 + j * 50, 150 + i * 50))
                rect.setOutline(color_rgb(0, 0, 0))
                pnt = Point(125 + j * 50, 125 + i * 50)
                if (i + j) % 2 == 0:
                    rect.setFill(color_rgb(255, 255, 255))
                    pnt.setFill(color_rgb(255, 255, 255))
                else:
                    rect.setFill(color_rgb(0, 0, 0))
                    pnt.setFill(color_rgb(0, 0, 0))

                rect.draw(shared.win)
                pnt.draw(shared.win)