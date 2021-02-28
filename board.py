import shared
from graphics import *


# Defines a square on the board.
class Square():
    _file = "a"
    _rank = 1

    def draw(self):
        rect = Rectangle(Point(100 + (ord(self._file) - ord("a")) * 50, 550 - (self._rank * 50)), Point(150 + ((ord(self._file) - ord("a")) * 50), 500 - (self._rank * 50)))
        rect.setOutline(color_rgb(0, 0, 0))
        if (self._rank + ord(self._file) - ord("a")) % 2 == 0:
            rect.setFill(color_rgb(255, 255, 255))
        else:
            rect.setFill(color_rgb(0, 0, 0))
        rect.draw(shared.win)

    def __init__(self, file, rank):
        # Gives squares the parameters of file and rank.
        self._file = file
        self._rank = rank

    # Returns the file of a square.
    def get_file(self):
        return self._file

    # Returns the file of a square as an integer.
    def get_file_as_int(self):
        return ord(self._file) - ord("a") + 1  # ord returns the character code of the requested character.

    # Returns the rank of a square.
    def get_rank(self):
        return self._rank


class Board:
    # Draws the board.
    def draw(self):
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
