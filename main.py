import shared
from graphics import *
import board
from player import *
from pieces import *


def file_from_int(file_as_int):  # one method of converting from an int value to a string value for the file of a square
    return chr(ord("a")+file_as_int)


for x in range(8):
    Pawn(Square(file_from_int(x), 2), False)


def redraw():  # redraws both sets of pieces and the board
    board = Board()
    board.draw()
    white.draw()
    black.draw()


def captureWhite():  # determines if a piece has landed on the same square as a white piece, if so it removes it from the piece array
    global mouseClick
    file = files[int((mouseClick.x - 100)/50)]
    rank = 8 - int((mouseClick.y - 100)/50)
    i = 0
    for piece in white._pieces:
        rankOk = piece._square._rank == rank
        fileOk = piece._square._file == file
        if rankOk and fileOk:
            white._pieces.pop(i)
            break
        else:
            i += 1


def captureBlack():  # determines if a piece has landed on the same square as a black piece, if so it removes it from the piece array
    global mouseClick
    file = files[int((mouseClick.x - 100)/50)]
    rank = 8 - int((mouseClick.y - 100)/50)
    i = 0
    for piece in black._pieces:
        rankOk = piece._square._rank == rank
        fileOk = piece._square._file == file
        if rankOk and fileOk:
            black._pieces.pop(i)
            break
        else:
            i += 1


def captureOwnPiece():  # determines is a piece is attempting to capture it's own piece, and if so it prevents it
    global mouseClick
    global movingPiece
    global unoccupied
    unoccupied = True
    file = files[int((mouseClick.x - 100)/50)]  # checks the square a piece is trying to move to 
    rank = 8 - int((mouseClick.y - 100)/50)
    if movingPiece == None:
        unoccupied = False
    else:
        if movingPiece._is_black:  # if the moving piece is black then it checks for black pieces on the target square 
            for piece in black._pieces:
                rankOk = piece._square._rank == rank
                fileOk = piece._square._file == file
                if rankOk and fileOk:
                    unoccupied = False
                    shared.selected_square = None
                    redraw()
                    break
        else:
            for piece in white._pieces:  # if the moving piece is white then it checks for white pieces on the target square 
                rankOk = piece._square._rank == rank
                fileOk = piece._square._file == file
                if rankOk and fileOk:
                    unoccupied = False
                    shared.selected_square = None
                    redraw()
                    break



def moveWhite():  # allows the white pieces to move
    global selected_square
    global mouseClick
    global movingPiece
    global unoccupied
    shared.selected_square = None
    redraw()
    mouseClick = shared.win.getMouse()  # takes a mouse input, uses the co-ordinates of the click to determine a square, searches for a piece in the array of white pieces with a square matching the one clicked on
    if 100 <= mouseClick.x < 500 and 100 <= mouseClick.y < 500:
        shared.file_as_int_start = int((mouseClick.x - 100)/50)
        file = files[shared.file_as_int_start]
        rank = 8 - int((mouseClick.y - 100)/50)
        shared.selected_square = Square(file, rank)
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
            mouseClick = shared.win.getMouse()  # takes a second mouse input, uses the co-ordinates of the click to determine a square, then changes the pieces current square to that square
            if 100 <= mouseClick.x < 500 and 100 <= mouseClick.y < 500:
                shared.file_as_int_end = int((mouseClick.x - 100)/50)
                file = files[shared.file_as_int_end]
                rank = 8 - int((mouseClick.y - 100)/50)
                shared.end_square = Square(file, rank)
                white.legal_move()
                if shared.legal:
                    captureOwnPiece()
                    if unoccupied:
                        if movingPiece:
                            captureBlack()
                            movingPiece.move_to(file, rank)
                            move = shared.turn, shared.initial, file, rank
                            yes = Text(Point(650, 100 + shared.turn * 20), move)
                            yes.draw(shared.win)
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


def moveBlack():# allows the black pieces to move
    global selected_square
    global mouseClick
    global movingPiece
    shared.selected_square = None
    redraw()
    mouseClick = shared.win.getMouse()  # takes a mouse input, uses the co-ordinates of the click to determine a square, searches for a piece in the array of white pieces with a square matching the one clicked on
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
            mouseClick = shared.win.getMouse()  # takes a second mouse input, uses the co-ordinates of the click to determine a square, then changes the pieces current square to that square
            print(mouseClick)
            if 100 <= mouseClick.x < 500 and 100 <= mouseClick.y < 500:
                shared.file_as_int_end = int((mouseClick.x - 100)/50)
                file = files[shared.file_as_int_end]
                rank = 8 - int((mouseClick.y - 100)/50)
                shared.end_square = Square(file, rank)
                black.legal_move()
                if shared.legal:
                    captureOwnPiece()
                    if unoccupied:
                        if movingPiece:
                            captureWhite()
                            movingPiece.move_to(file, rank)
                            move = shared.turn, shared.initial, file, rank
                            yes = Text(Point(775, 100 + shared.turn * 20), move)
                            yes.draw(shared.win)
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


shared.win = GraphWin("My window", 950, 600)  # main block of code, creates the instances of the players and runs the movement code, then redraws everything
movesBox = Rectangle(Point(600, 100), Point(850, 500))
movesBox.draw(shared.win)
shared.win.setBackground(color_rgb(255, 255, 255))
print("My Chess Program")
board = Board()
board.draw()
white = Player(False)
white.draw()
black = Player(True)
black.draw()
shared.turn = 1
for i in range(100):  # not indefinite as there is no current way for the game to end
    moveWhite()
    moveBlack()
    shared.turn += 1
shared.win.getMouse()
shared.win.close()
