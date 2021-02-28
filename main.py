import shared
from graphics import *
import board
from player import *
from pieces import *
import random


# This function is key to the AI decision making. It takes into account both the inherent and positional
# value of a piece.
def evaluate():
    shared.value = 0
    for piece in shared.all_pieces:
        if piece._is_black:
            if isinstance(piece, King):
                shared.value -= (piece.value - (1 /(abs(4.5 - piece._square._rank)) * 1 / (abs(4.5 - (ord(piece._square._file) - ord('a') + 1)))))
            else:
                shared.value -= (piece.value + (1/(abs(4.5 - piece._square._rank)) * 1/(abs(4.5 - (ord(piece._square._file) - ord('a') + 1)))))
        else:
            if isinstance(piece, King):
                shared.value += (piece.value - (1/(abs(4.5 - piece._square._rank)) * 1/(abs(4.5 - (ord(piece._square._file) - ord('a') + 1)))))
            else:
                shared.value += (piece.value + (1 / (abs(4.5 - piece._square._rank)) * 1 /(abs(4.5 - (ord(piece._square._file) - ord('a') + 1)))))
        if shared.turn > 10:
            if piece._is_black:
                for Piece in shared.white_pieces:
                    if isinstance(Piece, King):
                        if isinstance(piece, Queen):
                            if piece._square._rank == Piece._square._rank or piece._square._file == Piece._square._file or abs(piece._square._rank - Piece._square._rank) == abs(ord(piece._square._file) - ord(Piece._square._file)):
                                shared.value -= 1
                        elif isinstance(Piece, Rook):
                            if piece._square._rank == Piece._square._rank or piece._square._file == Piece._square._file:
                                shared.value -= 1
                        elif isinstance(Piece, Bishop):
                            if abs(piece._square._rank - Piece._square._rank) == abs(
                                ord(piece._square._file) - ord(Piece._square._file)):
                                shared.value -= 1
                        elif isinstance(Piece, Knight):
                            if (abs(Piece._square._rank - piece._square._rank) == 2 and abs(ord(Piece._square._file) - ord(piece._square._file)) == 1) or (abs(Piece._square._rank - piece._square._rank) == 1 and abs(ord(Piece._square._file) - ord(piece._square._file)) == 2):
                                shared.value -= 1
                        elif isinstance(Piece, Pawn):
                            if piece._square._rank - Piece._square._rank == 1 and abs(ord(piece._square._file) - ord(Piece._square._file)) == 1:
                                shared.value -= 1
            else:
                for Piece in shared.black_pieces:
                    if isinstance(Piece, King):
                        if isinstance(piece, Queen):
                            if piece._square._rank == Piece._square._rank or piece._square._file == Piece._square._file or abs(piece._square._rank - Piece._square._rank) == abs(ord(piece._square._file) - ord(Piece._square._file)):
                                shared.value += 1
                        elif isinstance(Piece, Rook):
                            if piece._square._rank == Piece._square._rank or piece._square._file == Piece._square._file:
                                shared.value += 1
                        elif isinstance(Piece, Bishop):
                            if abs(piece._square._rank - Piece._square._rank) == abs(
                                ord(piece._square._file) - ord(Piece._square._file)):
                                shared.value += 1
                        elif isinstance(Piece, Knight):
                            if (abs(Piece._square._rank - piece._square._rank) == 2 and abs(ord(Piece._square._file) - ord(piece._square._file)) == 1) or (abs(Piece._square._rank - piece._square._rank) == 1 and abs(ord(Piece._square._file) - ord(piece._square._file)) == 2):
                                shared.value += 1
                        elif isinstance(Piece, Pawn):
                            if piece._square._rank - Piece._square._rank == -1 and abs(ord(piece._square._file) - ord(Piece._square._file)) == 1:
                                shared.value -= 1
    shared.value = round(shared.value, 4)
    return shared.value


# Called by move_maker_B to add an extra level of depth to the decision making process.
def move_maker_W():
    global movingPiece
    shared.best_value_W = -100000
    shared.select_square("a", 4)
    for piece in white._pieces:
        start_file = piece._square._file
        start_rank = piece._square._rank
        for k in range(8):
            for l in range(8):
                file = chr(ord('a') + k)
                rank = 1 + l
                promoted = False
                if piece.can_i_move_to(file, rank):
                    movingPiece = piece
                    captureOwnPiece(file, rank)
                    if unoccupied:
                        shared.all_pieces.pop(shared.all_pieces.index(piece))
                        piece.move_to(file, rank)
                        shared.all_pieces.append(piece)
                        captureBlack(file, rank)
                        if isinstance(piece, Pawn) and rank == 8:
                            white._pieces.pop(white._pieces.index(piece))
                            shared.all_pieces.pop(shared.all_pieces.index(piece))
                            promoted_piece = Queen(Square(file, rank), False)
                            white._pieces.append(promoted_piece)
                            shared.all_pieces.append(promoted_piece)
                            promoted = True
                        evaluate()
                        if shared.best_value_W < shared.value:
                            shared.best_value_W = shared.value
                        elif shared.best_value_W == shared.value:
                            number = random.randint(0, 1)
                            if number == 0:
                                shared.best_value_W = shared.value
                        if promoted:
                            white._pieces.pop(white._pieces.index(promoted_piece))
                            shared.all_pieces.pop(shared.all_pieces.index(promoted_piece))
                            white._pieces.append(piece)
                            shared.all_pieces.append(piece)
                        shared.all_pieces.pop(shared.all_pieces.index(piece))
                        piece.move_to(start_file, start_rank)
                        shared.all_pieces.append(piece)
                        for x in shared.eval_storage_B:
                            black._pieces.append(x)
                            shared.all_pieces.append(x)
                        shared.eval_storage_B.clear()
                        #if shared.castle != None:
                            #shared.castle.move_to(shared.castle_square._file, shared.castle_square._rank)
                            #shared.castle = None
                            #shared.castle_square = None


# Allows the AI to cycle through all the legal moves it can make and evaluate which is the best.
def move_maker_B():
    global movingPiece
    redraw()
    shared.best_value = 100000
    for Piece in black._pieces:
        # Store the start square of the piece - we need to restore it later. 
        start_file = Piece._square._file
        start_rank = Piece._square._rank
        for i in range(8):
            for j in range(8):
                file = chr(ord('a') + i)
                rank = 1 + j
                Promoted = False
                
                if Piece.can_i_move_to(file, rank):
                    movingPiece = Piece
                    captureOwnPiece(file, rank)
                    if unoccupied:
                        shared.all_pieces.pop(shared.all_pieces.index(Piece))
                        Piece.move_to(file, rank)
                        shared.all_pieces.append(Piece)
                        captureWhite(file, rank)
                        if isinstance(Piece, Pawn) and rank == 1:
                            black._pieces.pop(black._pieces.index(Piece))
                            shared.all_pieces.pop(shared.all_pieces.index(Piece))
                            Promoted_piece = Queen(Square(file, rank), True)
                            black._pieces.append(Promoted_piece)
                            shared.all_pieces.append(Promoted_piece)
                            Promoted = True
                        move_maker_W()
                        #shared.select_square(Piece._square._file, Piece._square._rank)
                        if shared.best_value > shared.best_value_W:
                            shared.best_value = shared.best_value_W
                            best_piece = Piece
                            best_square = Square(file, rank)
                            print(best_square._file, best_square._rank)
                            shared.redraw_square = Square(start_file, start_rank)
                            shared.redraw_end_square = best_square
                        elif shared.best_value == shared.best_value_W:
                            number = random.randint(0, 1)
                            if number == 0:
                                shared.best_value = shared.best_value_W
                                best_piece = Piece
                                best_square = Square(file, rank)
                                shared.redraw_square = Square(start_file, start_rank)
                                shared.redraw_end_square = best_square
                if Promoted:
                    black._pieces.pop(black._pieces.index(Promoted_piece))
                    shared.all_pieces.pop(shared.all_pieces.index(Promoted_piece))
                    black._pieces.append(Piece)
                    shared.all_pieces.append(Piece)
                shared.all_pieces.pop(shared.all_pieces.index(Piece))
                # Restore the start position of the piece.
                Piece.move_to(start_file, start_rank)
                shared.all_pieces.append(Piece)
                for x in shared.eval_storage_W:
                        white._pieces.append(x)
                        shared.all_pieces.append(x)
                shared.eval_storage_W.clear()
    print("~~~~~~ Black Move ~~~~~~~~~")
    print(type(best_piece))
    print(best_piece._square._file, best_piece._square._rank, " to ", best_square._file, best_square._rank )
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    best_piece.move_to(best_square._file, best_square._rank)
    if isinstance(best_piece, Pawn) and best_square._rank == 1:
        black._pieces.pop(black._pieces.index(best_piece))
        shared.all_pieces.pop(shared.all_pieces.index(best_piece))
        Promoted_piece = Queen(Square(best_square._file, best_square._rank), True)
        black._pieces.append(Promoted_piece)
        shared.all_pieces.append(Promoted_piece)
    shared.set_end_square(best_piece._square._file, best_piece._square._rank)
    captureWhite(best_square._file, best_square._rank)
    shared.eval_storage_W.clear()
    move = shared.turn, best_square._file, best_square._rank
    yes = Text(Point(775, 100 + shared.turn * 20), move)
    yes.draw(shared.win)
    for piece in white._pieces:
        if isinstance(piece, Pawn):
            piece.en_passant = False
    redraw()


# One method of converting from an int value to a string value for the file of a square.
def file_from_int(file_as_int):
    return chr(ord("a")+file_as_int)


# Redraws only pieces and squares involved in the move.
def redraw():
    shared.redraw_square.draw()
    shared.redraw_end_square.draw()
    white.draw()
    black.draw()


# Determines if a piece has landed on the same square as a white piece, if so it removes it from the piece array.
def captureWhite(file, rank):
    if shared.en_passant_capture != None:
        black._pieces.pop(white._pieces.index(shared.en_passant_capture))
        shared.all_pieces.pop(shared.all_pieces.index(shared.en_passant_capture))
        shared.eval_storage_W.append(shared.en_passant_capture)
        shared.en_passant_capture = None
        Square(file, rank + 1).draw()
    else:
        i = 0
        for piece in white._pieces:
            rankOk = piece._square._rank == rank
            fileOk = piece._square._file == file
            if rankOk and fileOk:
                white._pieces.pop(i)
                shared.all_pieces.pop(shared.all_pieces.index(piece))
                shared.eval_storage_W.append(piece)
                shared.opponent_piece = True
                break
            else:
                i += 1


# Determines if a piece has landed on the same square as a black piece, if so it removes it from the piece array.
def captureBlack(file, rank):
    if shared.en_passant_capture != None:
        black._pieces.pop(black._pieces.index(shared.en_passant_capture))
        shared.all_pieces.pop(shared.all_pieces.index(shared.en_passant_capture))
        shared.eval_storage_B.append(shared.en_passant_capture)
        shared.en_passant_capture = None
        Square(file, rank - 1).draw()
    else:
        i = 0
        for piece in black._pieces:
            rankOk = piece._square._rank == rank
            fileOk = piece._square._file == file
            if rankOk and fileOk:
                black._pieces.pop(i)
                shared.all_pieces.pop(shared.all_pieces.index(piece))
                shared.eval_storage_B.append(piece)
                shared.opponent_piece = True
                break
            else:
                i += 1


# Determines is a piece is attempting to capture it's own piece, and if so it prevents it.
def captureOwnPiece(file, rank):
    global movingPiece
    global unoccupied
    unoccupied = True
    if movingPiece == None:
        unoccupied = False
    else:
        # If the moving piece is black then it checks for black pieces on the target square.
        if movingPiece._is_black:
            for piece in black._pieces:
                rankOk = piece._square._rank == rank
                fileOk = piece._square._file == file
                if rankOk and fileOk:
                    unoccupied = False
                    break
        else:
            # If the moving piece is white then it checks for white pieces on the target square.
            for piece in white._pieces:
                rankOk = piece._square._rank == rank
                fileOk = piece._square._file == file
                if rankOk and fileOk:
                    unoccupied = False
                    shared.selected_square = None
                    break



# Allows the white pieces to move.
def moveWhite():
    global selected_square
    global mouseClick
    global movingPiece
    global unoccupied
    shared.select_square("a", 4)
    # Takes a mouse input, uses the co-ordinates of the click to determine a square, searches for a piece
    # in the array of white pieces with a square matching the one clicked on.
    mouseClick = shared.win.getMouse()
    if 100 <= mouseClick.x < 500 and 100 <= mouseClick.y < 500:
        shared.file_as_int_start = int((mouseClick.x - 100)/50)
        file = files[shared.file_as_int_start]
        rank = 8 - int((mouseClick.y - 100)/50)
        shared.selected_square = Square(file, rank)
        shared.redraw_square = shared.selected_square
        movingPiece = None
        for piece in white._pieces:
            rankOk = piece._square._rank == rank
            fileOk = piece._square._file == file
            if rankOk and fileOk:
                movingPiece = piece
                break
        if movingPiece == None:
            moveWhite()
        else:
            redraw()
            # Takes a second mouse input, uses the co-ordinates of the click to determine a square,
            # then changes the pieces current square to that square.
            mouseClick = shared.win.getMouse()
            if 100 <= mouseClick.x < 500 and 100 <= mouseClick.y < 500:
                #shared.file_as_int_end = int((mouseClick.x - 100)/50)
                file = files[int((mouseClick.x - 100)/50)]
                rank = 8 - int((mouseClick.y - 100)/50)
                #shared.set_end_square(file, rank)
                
                if movingPiece.can_i_move_to(file, rank):# white.legal_move(file, rank):
                    captureOwnPiece(file, rank)
                    if unoccupied:
                        if movingPiece:
                            captureBlack(file, rank)
                            shared.eval_storage_B.clear()
                            movingPiece.move_to(file, rank)
                            if isinstance(movingPiece, Pawn) and rank == 8:
                                white._pieces.pop(white._pieces.index(movingPiece))
                                shared.all_pieces.pop(shared.all_pieces.index(movingPiece))
                                white._pieces.append(Queen(Square(file, rank), False))
                                shared.all_pieces.append(Queen(Square(file, rank), False))
                            shared.redraw_end_square = Square(file, rank)
                            #shared.redraw_end_square.draw()
                            move = shared.turn, shared.initial, file, rank
                            yes = Text(Point(650, 100 + shared.turn * 20), move)
                            yes.draw(shared.win)
                            shared.white_pieces.clear()
                            shared.black_pieces.clear()
                            shared.all_pieces.clear()
                            redraw()
                            for piece in white._pieces:
                                shared.white_pieces.append(piece)
                                shared.all_pieces.append(piece)
                            for piece in black._pieces:
                                shared.black_pieces.append(piece)
                                shared.all_pieces.append(piece)
                                if isinstance(piece, Pawn):
                                    piece.en_passant = False
                                #shared.castle = None
                                #shared.castle_square = None
                        else:
                            moveWhite()
                    else:
                        moveWhite()
                else:
                    moveWhite()
            else:
                moveWhite()
    else:
        moveWhite()


# Allows the black pieces to move. This is no longer used. For testing purposes both black and white were
# moved by the player in early versions.
def moveBlack():
    global mouseClick
    global movingPiece
    shared.select_square("a", 4)
    redraw()
    # Takes a mouse input, uses the co-ordinates of the click to determine a square, searches for a
    # piece in the array of white pieces with a square matching the one clicked on.
    mouseClick = shared.win.getMouse()
    print(mouseClick)
    if 100 <= mouseClick.x < 500 and 100 <= mouseClick.y < 500:
        shared.file_as_int_start = int((mouseClick.x - 100)/50)
        file = files[shared.file_as_int_start]
        rank = 8 - int((mouseClick.y - 100)/50)
        shared.selected_square = Square(file, rank)
        movingPiece = None
        for piece in black._pieces:
            rankOk = piece._square._rank == rank
            fileOk = piece._square._file == file
            if rankOk and fileOk:
                movingPiece = piece
                break
        if movingPiece == None:
            moveBlack()
        else:
            redraw()
            # Takes a second mouse input, uses the co-ordinates of the click to determine a square,
            # then changes the pieces current square to that square.
            mouseClick = shared.win.getMouse()
            print(mouseClick)
            if 100 <= mouseClick.x < 500 and 100 <= mouseClick.y < 500:
                shared.file_as_int_end = int((mouseClick.x - 100)/50)
                file = files[shared.file_as_int_end]
                rank = 8 - int((mouseClick.y - 100)/50)
                shared.set_end_square(file, rank)
                black.legal_move(file, rank)
                if shared.legal:
                    captureOwnPiece(file, rank)
                    if unoccupied:
                        if movingPiece:
                            captureWhite(file, rank)
                            movingPiece.move_to(file, rank)
                            move = shared.turn, shared.initial, file, rank
                            yes = Text(Point(775, 100 + shared.turn * 20), move)
                            yes.draw(shared.win)
                            shared.white_pieces.clear()
                            shared.black_pieces.clear()
                            shared.all_pieces.clear()
                            for piece in white._pieces:
                                shared.white_pieces.append(piece)
                                shared.all_pieces.append(piece)
                            for piece in black._pieces:
                                shared.black_pieces.append(piece)
                                shared.all_pieces.append(piece)
                        else:
                            moveBlack()
                    else:
                        moveBlack()
                else:
                    moveBlack()
            else:
                moveBlack()
    else:
        moveBlack()


# Main block of code, creates the instances of the players and runs the movement code, then redraws everything.
shared.win = GraphWin("My window", 950, 600)
movesBox = Rectangle(Point(600, 100), Point(850, 500))
movesBox.draw(shared.win)
shared.win.setBackground(color_rgb(255, 255, 255))
board = Board()
board.draw()
white = Player(False)
for i in white._pieces:
    shared.white_pieces.append(i)
white.draw()
black = Player(True)
for i in black._pieces:
    shared.black_pieces.append(i)
black.draw()
shared.turn = 1
for i in shared.white_pieces:
    shared.all_pieces.append(i)
for i in shared.black_pieces:
    shared.all_pieces.append(i)
while abs(shared.value) < 5000:
    moveWhite()
    move_maker_B()
    value = evaluate()
    print(value)
    print(shared.move1)
    shared.turn += 1
if shared.best_value_W > 5000:
    print("You Win")
else:
    print("You Lose")
shared.win.close()
