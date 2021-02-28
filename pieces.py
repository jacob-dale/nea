from shared import *
from graphics import *
from board import *


# This is the base class for all pieces. Specialised classes override draw_piece and
# can_i_move_to.
class Piece:
    _highlight_colour = (color_rgb(50, 205, 50))  # used for the outline colour of the selected piece

    def __init__(self, start_square, is_black):  
        self._square = start_square  # determines the colour of the piece
        self._is_black = is_black
        self.value = 0
        self._fill_colour = (color_rgb(255, 255, 255))
        self._outline_colour = (color_rgb(0, 0, 0))
        self._not_moved = True
        if is_black:
           self._fill_colour = (color_rgb(0, 0, 0))  # outline colour of the piece, opposite to the fill colour
           self._outline_colour = (color_rgb(255, 255, 255))
        else:
            self._fill_colour = (color_rgb(255, 255, 255))
            self._outline_colour = (color_rgb(0, 0, 0))

    def draw_piece(self):
        pass

    def can_i_move_to(self, file, rank):
        pass

    # Returns the file of a square as an integer.
    def get_file_as_int(self):
        return ord(self._file) - ord("a") + 1  # ord returns the character code of the requested character

    def move_to(self, file, rank):
        self._square = Square(file, rank)

    # Determines if a square has been selected, if so the piece will be highlighted.
    def is_selected(self):
        if shared.selected_square is not None:
            if (self._square._rank == shared.selected_square._rank and self._square._file == shared.selected_square._file):
                return True
            else:
                return False
        else:
            return False


# Class defining the pawn pieces.
class Pawn(Piece):  # class defining the pawn pieces
    def __init__(self, start_square, is_black):
        super().__init__(start_square, is_black)
        self.en_passant = False

    def draw_piece(self, win):
        j = self._square.get_file_as_int()
        i = self._square.get_rank()
        self.value = 1
        # Defines the shape of a pawn.
        pawn = Polygon(Point(60 + j * 50, 545 - i * 50), Point(65 + j * 50, 540 - i * 50),
                       Point(65 + j * 50, 520 - i * 50), Point(75 + j * 50, 520 - i * 50),
                       Point(68 + j * 50, 513 - i * 50), Point(75 + j * 50, 506 - i * 50),
                       Point(82 + j * 50, 513 - i * 50), Point(75 + j * 50, 520 - i * 50),
                       Point(85 + j * 50, 520 - i * 50), Point(85 + j * 50, 540 - i * 50),
                       Point(90 + j * 50, 545 - i * 50))
        pawn.setFill(self._fill_colour)  # colours the pawn
        if self.is_selected():
            pawn.setOutline(self._highlight_colour)
            shared.initial = "."
        else:
            pawn.setOutline(self._outline_colour)
        pawn.draw(win)


    def can_i_move_to(self, file, rank):
        move_ok = False
        if self._is_black == True:
            move_ok = False
            if self._square._rank - rank == 1  and self._square._file == file:
                move_ok = True
                for piece in shared.all_pieces:
                    rankOk = piece._square._rank == rank
                    fileOk = piece._square._file == file
                    if fileOk and rankOk:
                        move_ok = False
            elif self._square._rank == 7 and self._square._rank - rank == 2 and self._square._file == file:
                move_ok = True
                self.en_passant = True
                for piece in shared.all_pieces:
                    rankOk = (piece._square._rank == rank) or (piece._square._rank == rank + 1)
                    fileOk = piece._square._file == file
                    if rankOk == True and fileOk == True:
                        move_ok = False
                        self.en_passant = False
            elif self._square._rank - 1 == rank and (self._square.get_file_as_int() - 1 == file_to_int(file) or self._square.get_file_as_int()+ 1 == file_to_int(file)):
                move_ok = False
                for piece in shared.all_pieces:
                    rankOk = piece._square._rank == rank
                    fileOk = piece._square._file == file
                    if rankOk and fileOk:
                        move_ok = True
                    elif isinstance(piece, Pawn):
                        if rank == 3 and fileOk and piece._square._rank == 4 and piece.en_passant == True:
                            move_ok = True
        else:
            move_ok = False
            if self._square._rank - rank == -1 and self._square._file == file:
                move_ok = True
                for piece in shared.all_pieces:
                    rankOk = piece._square._rank == rank
                    fileOk = piece._square._file == file
                    if fileOk and rankOk:
                        move_ok = False
            elif self._square._rank == 2 and self._square._rank - rank == -2 and self._square._file == file:
                move_ok = True
                self.en_passant = True
                for piece in shared.all_pieces:
                    rankOk = (piece._square._rank == rank) or (piece._square._rank == rank - 1)
                    fileOk = piece._square._file == file
                    if rankOk == True and fileOk == True:
                        move_ok = False
                        self.en_passant = False
            elif self._square._rank + 1 == rank and (
                    self._square.get_file_as_int() - 1 == file_to_int(file) or self._square.get_file_as_int() + 1 == file_to_int(file)):
                move_ok = False
                for piece in shared.all_pieces:
                    rankOk = piece._square._rank == rank
                    fileOk = piece._square._file == file
                    if rankOk and fileOk:
                        move_ok = True
                    elif isinstance(piece, Pawn):
                        if rank == 6 and fileOk and piece._square._rank == 5 and piece.en_passant == True:
                            move_ok = True
                            shared.en_passant_capture = piece
        return move_ok


# Class defining the king pieces.
class King(Piece):
    def __init__(self, start_square, is_black):
        super().__init__(start_square, is_black)
        self.not_moved = True

    def draw_piece(self, win):
        j = self._square.get_file_as_int()
        i = self._square.get_rank()
        self.value = 10000

        # Defines the shape of a king points with an x and y coord to show where the piece is located
        # all points combine to make up the 'king' polygon  this polygon can be drawn into the window.
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
        king.setFill(self._fill_colour)  # colours the king
        if self.is_selected():
            king.setOutline(self._highlight_colour)
            shared.initial = ".K"
        else:
            king.setOutline(self._outline_colour)
        king.draw(win)


    def can_i_move_to(self, file, rank):
        move_ok = False
        if (abs(rank - self._square._rank) == 1 and file_to_int(file) == self._square.get_file_as_int()) or (abs(file_to_int(file) - self._square.get_file_as_int()) == 1 and rank == self._square._rank) or (abs(rank - self._square._rank) == 1 and abs(file_to_int(file) - self._square.get_file_as_int()) == 1):
            move_ok = True
            self.not_moved = False
            '''elif rank == self._square._rank and abs(ord(file) - ord(self._square._file)) == 2:
                if self._is_black == True:
                    if rank == 8 and file == "g":
                        for piece in shared.all_pieces:
                            if piece._square._rank == 8 and (piece._square._file == "f" or piece._square._file == "g"):
                                pass
                            else:
                                move_ok = True
                    elif rank == 8 and file == "c":
                        for piece in shared.all_pieces:
                            if piece._square._rank == 8 and (piece._square._file == "d" or piece._square._file == "c"or piece._square._file == "b"):
                                pass
                            else:
                                move_ok = True
                else:
                    if rank == 1 and file == "g":
                        move_ok = True
                        for piece in shared.all_pieces:
                            if piece._square._rank == 1 and (piece._square._file == "f" or piece._square._file == "g"):
                                move_ok = False
                            else:
                                for piece in shared.all_pieces:
                                    if isinstance(piece, Rook) and piece._square._rank == 1 and piece._square._file == 'h':
                                        shared.eval_storage_W.append(piece)
                                        shared.castle_square = Square(piece._square._file, piece._square._rank)
                                        piece.move_to('f', 1)
                                        shared.castle = piece
                    elif rank == 1 and file == "c":
                        move_ok = True
                        for piece in shared.all_pieces:
                            if piece._square._rank == 1 and (piece._square._file == "d" or piece._square._file == "c"or piece._square._file == "b"):
                                move_ok = False
                            else:
                                pass'''
        else:
            move_ok = False
        return move_ok


# Class defining the queen piece.
class Queen(Piece):
    def draw_piece(self, win):
        j = self._square.get_file_as_int()
        i = self._square.get_rank()
        self.value = 9

        # Defines the shape of a queen.
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
            shared.initial = ".Q"
        else:
            queen.setOutline(self._outline_colour)
        queen.draw(win)


    def can_i_move_to(self, file, rank):
        move_ok = True
        if self._square._rank == rank:
            if file_to_int(file) > self._square.get_file_as_int():
                for i in range(abs(file_to_int(file) - self._square.get_file_as_int()) - 1):
                    for piece in shared.all_pieces:
                        if piece._square._rank == self._square._rank and piece._square._file == chr(
                                ord(self._square._file) + i + 1):
                            move_ok = False
            else:
                for i in range(abs(file_to_int(file) - self._square.get_file_as_int()) - 1):
                    for piece in shared.all_pieces:
                        if piece._square._rank == self._square._rank and piece._square._file == chr(
                                ord(self._square._file) - i - 1):
                            move_ok = False
        elif self._square._file == file:
            if rank > self._square._rank:
                for i in range(abs(self._square._rank - rank) - 1):
                    for piece in shared.all_pieces:
                        if piece._square._rank == self._square._rank + i + 1 and piece._square._file == self._square._file:
                            move_ok = False
            else:
                for i in range(abs(self._square._rank - rank) - 1):
                    for piece in shared.all_pieces:
                        if piece._square._rank == self._square._rank - i - 1 and piece._square._file == self._square._file:
                            move_ok = False
        elif abs(rank - self._square._rank) == abs(
                file_to_int(file) - self._square.get_file_as_int()):
            move_ok = True

            for i in range(abs(rank - self._square._rank) - 1):
                if rank - self._square._rank > 0:
                    if file_to_int(file) - self._square.get_file_as_int() > 0:
                        for piece in shared.all_pieces:
                            if piece._square._rank == self._square._rank + i + 1 and piece._square._file == chr(
                                    ord(self._square._file) + i + 1):
                                move_ok = False
                    else:
                        for piece in shared.all_pieces:
                            if piece._square._rank == self._square._rank + i + 1 and piece._square._file == chr(
                                    ord(self._square._file) - i - 1):
                                move_ok = False
                else:
                    if file_to_int(file) - self._square.get_file_as_int() > 1:
                        for piece in shared.all_pieces:
                            if piece._square._rank == self._square._rank - i - 1 and piece._square._file == chr(
                                    ord(self._square._file) + i + 1):
                                move_ok = False
                    else:
                        for piece in shared.all_pieces:
                            if piece._square._rank == self._square._rank - i - 1 and piece._square._file == chr(
                                    ord(self._square._file) - i - 1):
                                move_ok = False
        else:
            move_ok = False
        return move_ok


# Class defining the rook piece.
class Rook(Piece):
    def draw_piece(self, win):
        j = self._square.get_file_as_int()
        i = self._square.get_rank()
        self.value = 5

        # Defines the shape of a rook.
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
        rook.setFill(self._fill_colour)  # colours the rook
        if self.is_selected():
            rook.setOutline(self._highlight_colour)
            shared.initial = ".R"
        else:
            rook.setOutline(self._outline_colour)
        rook.draw(win)


    def can_i_move_to(self, file, rank):
        move_ok = True
        if self._square._rank == rank:
            if file_to_int(file) > self._square.get_file_as_int():
                for i in range(abs(file_to_int(file) - self._square.get_file_as_int())-1):
                    for piece in shared.all_pieces:
                        if piece._square._rank == self._square._rank and piece._square._file == chr(ord(self._square._file) + i + 1):
                            move_ok = False
                        else:
                            self._not_moved = False
            else:
                for i in range(abs(file_to_int(file) - self._square.get_file_as_int())-1):
                    for piece in shared.all_pieces:
                        if piece._square._rank == self._square._rank and piece._square._file == chr(ord(self._square._file) - i - 1):
                            move_ok = False
                        else:
                            self._not_moved = False
        elif self._square._file == file:
            if rank > self._square._rank:
                for i in range(abs(self._square._rank - rank)-1):
                    for piece in shared.all_pieces:
                        if piece._square._rank == self._square._rank + i + 1 and piece._square._file == self._square._file:
                            move_ok = False
                        else:
                            self._not_moved = False
            else:
                for i in range(abs(self._square._rank - rank) - 1):
                    for piece in shared.all_pieces:
                        if piece._square._rank == self._square._rank - i -1 and piece._square._file == self._square._file:
                            move_ok = False
                        else:
                            self._not_moved = False
        else:
            move_ok = False
        return move_ok


# Class defining the bishop piece.
class Bishop(Piece):
    def draw_piece(self, win):
        j = self._square.get_file_as_int()
        i = self._square.get_rank()
        self.value = 3

        # Defines the shape of a bishop.
        bishop = Polygon(Point(60 + j * 50, 545 - i * 50), Point(70 + j * 50, 525 - i * 50),
                         Point(67 + j * 50, 522 - i * 50), Point(70 + j * 50, 519 - i * 50),
                         Point(70 + j * 50, 515 - i * 50), Point(68 + j * 50, 513 - i * 50),
                         Point(75 + j * 50, 507 - i * 50), Point(74 + j * 50, 506 - i * 50),
                         Point(75 + j * 50, 505 - i * 50), Point(76 + j * 50, 506 - i * 50),
                         Point(75 + j * 50, 507 - i * 50), Point(82 + j * 50, 513 - i * 50),
                         Point(80 + j * 50, 515 - i * 50), Point(80 + j * 50, 519 - i * 50),
                         Point(83 + j * 50, 522 - i * 50), Point(80 + j * 50, 525 - i * 50),
                         Point(90 + j * 50, 545 - i * 50))
        bishop.setFill(self._fill_colour)  # colours the bishop
        if self.is_selected():
            bishop.setOutline(self._highlight_colour)
            shared.initial = ".B"
        else:
            bishop.setOutline(self._outline_colour)
        bishop.draw(win)




    def can_i_move_to(self, file, rank):
        move_ok = False 
        if abs(rank - self._square._rank) == abs(file_to_int(file) - self._square.get_file_as_int()):
            move_ok = True
            
            for i in range(abs(rank - self._square._rank) - 1):
                if rank - self._square._rank > 0:
                    if file_to_int(file) - self._square.get_file_as_int() > 0:
                        for piece in shared.all_pieces:
                            if piece._square._rank == self._square._rank + i + 1 and piece._square._file ==  chr(ord(self._square._file) + i + 1):
                                move_ok = False
                    else:
                        for piece in shared.all_pieces:
                            if piece._square._rank == self._square._rank + i + 1 and piece._square._file ==  chr(ord(self._square._file) - i - 1):
                                move_ok = False
                else:
                    if file_to_int(file) - self._square.get_file_as_int() > 1:
                        for piece in shared.all_pieces:
                            if piece._square._rank == self._square._rank - i - 1 and piece._square._file ==  chr(ord(self._square._file) + i + 1):
                                move_ok = False
                    else:
                        for piece in shared.all_pieces:
                            if piece._square._rank == self._square._rank - i - 1 and piece._square._file ==  chr(ord(self._square._file) - i - 1):
                                move_ok = False
        return move_ok


# Class defining the knight piece.
class Knight(Piece):
    def draw_piece(self, win):
        j = self._square.get_file_as_int()
        i = self._square.get_rank()
        self.value = 3

        # Defines the shape of a knight.
        knight = Polygon(Point(55 + j * 50, 545 - i * 50), Point(60 + j * 50, 535 - i * 50),
                         Point(72 + j * 50, 520 - i * 50), Point(64 + j * 50, 522 - i * 50),
                         Point(55 + j * 50, 510 - i * 50), Point(73 + j * 50, 507 - i * 50),
                         Point(77 + j * 50, 502 - i * 50), Point(82 + j * 50, 505.5 - i * 50),
                         Point(85 + j * 50, 505 - i * 50), Point(95 + j * 50, 515 - i * 50),
                         Point(90 + j * 50, 535 - i * 50), Point(95 + j * 50, 545 - i * 50))
        knight.setFill(self._fill_colour)  # colours the knight
        if self.is_selected():
            knight.setOutline(self._highlight_colour)
            shared.initial = ".N"
        else:
            knight.setOutline(self._outline_colour)
        knight.draw(win)


    def can_i_move_to(self, file, rank):
        move_ok = False
        if (abs(file_to_int(file) - self._square.get_file_as_int()) == 1  and abs(self._square._rank - rank) == 2) or (abs(file_to_int(file) - self._square.get_file_as_int()) == 2 and abs(rank - self._square._rank)) == 1:
            move_ok = True
        else:
            move_ok = False
        return move_ok
