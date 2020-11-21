import shared
from graphics import *
from board import *

class Piece:
    _highlight_colour = (color_rgb(50, 205, 50))

    def __init__(self, start_square, is_black):  # colours the pieces
        self._square = start_square
        self._is_black = is_black
        self._fill_colour = (color_rgb(255, 255, 255))
        self._outline_colour = (color_rgb(0, 0, 0))
        if is_black:
           self._fill_colour = (color_rgb(0, 0, 0))
           self._outline_colour = (color_rgb(255, 255, 255))
        else:
            self._fill_colour = (color_rgb(255, 255, 255))
            self._outline_colour = (color_rgb(0, 0, 0))

    def draw_piece(self):
        pass

    def can_i_move_to(self):  # not used yet
        pass

    def move_to(self, file, rank):
        self._square = Square(file, rank)

    def is_selected(self):  # determines if a sqare has been selected, if so the piece will be highlighted
        if shared.selected_square is not None:
            if self._square._rank == selected_square._rank and self._square._file == selected_square._file:
                return True
            else:
                return False
        else:
            return False


class Pawn(Piece):
    def draw_piece(self, win):
        j = self._square.get_file_as_int()
        i = self._square.get_rank()
        pawn = Polygon(Point(60 + j * 50, 545 - i * 50), Point(65 + j * 50, 540 - i * 50),
                       Point(65 + j * 50, 520 - i * 50), Point(75 + j * 50, 520 - i * 50),
                       Point(68 + j * 50, 513 - i * 50), Point(75 + j * 50, 506 - i * 50),
                       Point(82 + j * 50, 513 - i * 50), Point(75 + j * 50, 520 - i * 50),
                       Point(85 + j * 50, 520 - i * 50), Point(85 + j * 50, 540 - i * 50),
                       Point(90 + j * 50, 545 - i * 50))
        pawn.setFill(self._fill_colour)
        if self.is_selected():
            pawn.setOutline(self._highlight_colour)
        else:
            pawn.setOutline(self._outline_colour)
        pawn.draw(win)


class King(Piece):
    def draw_piece(self, win):
        j = self._square.get_file_as_int()
        i = self._square.get_rank()

        king = Polygon(Point(62 + j * 50, 545 - i * 50), Point(62 + j * 50, 540 - i * 50),
                       Point(66 + j * 50, 540 - i * 50), Point(66 + j * 50, 520 - i * 50),
                       Point(63 + j * 50, 520 - i * 50), Point(63 + j * 50, 517 - i * 50),
                       Point(73 + j * 50, 517 - i * 50), Point(73 + j * 50, 513 - i * 50),
                       Point(69 + j * 50, 513 - i * 50), Point(69 + j * 50, 509 - i * 50),
                       Point(73 + j * 50, 509 - i * 50), Point(73 + j * 50, 505 - i * 50),
                       Point(77 + j * 50, 505 - i * 50), Point(77 + j * 50, 509 - i * 50),
                       Point(81 + j * 50, 509 - i * 50), Point(81 + j * 50, 513 - i * 50),
                       Point(77 + j * 50, 513 - i * 50), Point(77 + j * 50, 517 - i * 50),
                       Point(87 + j * 50, 517 - i * 50), Point(87 + j * 50, 520 - i * 50),
                       Point(84 + j * 50, 520 - i * 50), Point(84 + j * 50, 540 - i * 50),
                       Point(88 + j * 50, 540 - i * 50), Point(88 + j * 50, 545 - i * 50))
        king.setFill(self._fill_colour)
        if self.is_selected():
            king.setOutline(self._highlight_colour)
        else:
            king.setOutline(self._outline_colour)
        king.draw(win)


class Queen(Piece):
    def draw_piece(self, win):
        j = self._square.get_file_as_int()
        i = self._square.get_rank()

        queen = Polygon(Point(60 + j * 50, 545 - i * 50), Point(65 + j * 50, 542 - i * 50),
                        Point(65 + j * 50, 525 - i * 50), Point(65 + j * 50, 515 - i * 50),
                        Point(60 + j * 50, 511 - i * 50), Point(70 + j * 50, 513 - i * 50),
                        Point(75 + j * 50, 505 - i * 50), Point(80 + j * 50, 513 - i * 50),
                        Point(90 + j * 50, 511 - i * 50), Point(85 + j * 50, 515 - i * 50),
                        Point(85 + j * 50, 525 - i * 50), Point(85 + j * 50, 542 - i * 50),
                        Point(90 + j * 50, 545 - i * 50))
        queen.setFill(self._fill_colour)
        if self.is_selected():
            queen.setOutline(self._highlight_colour)
        else:
            queen.setOutline(self._outline_colour)
        queen.draw(win)


class Rook(Piece):
    def draw_piece(self, win):
        j = self._square.get_file_as_int()
        i = self._square.get_rank()

        rook = Polygon(Point(91 + j * 50, 545 - i * 50), Point(91 + j * 50, 535 - i * 50),
                        Point(87 + j * 50, 535 - i * 50), Point(87 + j * 50, 515 - i * 50),
                        Point(90 + j * 50, 515 - i * 50), Point(90 + j * 50, 505 - i * 50),
                        Point(82 + j * 50, 505 - i * 50), Point(82 + j * 50, 508 - i * 50),
                        Point(79 + j * 50, 508 - i * 50), Point(79 + j * 50, 505 - i * 50),
                        Point(71 + j * 50, 505 - i * 50), Point(71 + j * 50, 508 - i * 50),
                        Point(68 + j * 50, 508 - i * 50), Point(68 + j * 50, 505 - i * 50),
                        Point(60 + j * 50, 505 - i * 50), Point(60 + j * 50, 515 - i * 50),
                        Point(63 + j * 50, 515 - i * 50), Point(63 + j * 50, 535 - i * 50),
                        Point(59 + j * 50, 535 - i * 50), Point(59 + j * 50, 545 - i * 50))
        rook.setFill(self._fill_colour)
        if self.is_selected():
            rook.setOutline(self._highlight_colour)
        else:
            rook.setOutline(self._outline_colour)
        rook.draw(win)


class Bishop(Piece):
    def draw_piece(self, win):
        j = self._square.get_file_as_int()
        i = self._square.get_rank()

        bishop = Polygon(Point(60 + j * 50, 545 - i * 50), Point(70 + j * 50, 525 - i * 50),
                         Point(67 + j * 50, 522 - i * 50), Point(70 + j * 50, 519 - i * 50),
                         Point(70 + j * 50, 515 - i * 50), Point(68 + j * 50, 513 - i * 50),
                         Point(75 + j * 50, 507 - i * 50), Point(74 + j * 50, 506 - i * 50),
                         Point(75 + j * 50, 505 - i * 50), Point(76 + j * 50, 506 - i * 50),
                         Point(75 + j * 50, 507 - i * 50), Point(82 + j * 50, 513 - i * 50),
                         Point(80 + j * 50, 515 - i * 50), Point(80 + j * 50, 519 - i * 50),
                         Point(83 + j * 50, 522 - i * 50), Point(80 + j * 50, 525 - i * 50),
                         Point(90 + j * 50, 545 - i * 50))
        bishop.setFill(self._fill_colour)
        if self.is_selected():
            bishop.setOutline(self._highlight_colour)
        else:
            bishop.setOutline(self._outline_colour)
        bishop.draw(win)


class Knight(Piece):
    def draw_piece(self, win):
        j = self._square.get_file_as_int()
        i = self._square.get_rank()

        knight = Polygon(Point(55 + j * 50, 545 - i * 50), Point(60 + j * 50, 535 - i * 50),
                         Point(72 + j * 50, 520 - i * 50), Point(64 + j * 50, 522 - i * 50),
                         Point(55 + j * 50, 510 - i * 50), Point(73 + j * 50, 507 - i * 50),
                         Point(77 + j * 50, 502 - i * 50), Point(82 + j * 50, 505.5 - i * 50),
                         Point(85 + j * 50, 505 - i * 50), Point(95 + j * 50, 515 - i * 50),
                         Point(90 + j * 50, 535 - i * 50), Point(95 + j * 50, 545 - i * 50))
        knight.setFill(self._fill_colour)
        if self.is_selected():
            knight.setOutline(self._highlight_colour)
        else:
            knight.setOutline(self._outline_colour)
        knight.draw(win)