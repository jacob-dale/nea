import shared
from graphics import *
import board
from player import *
from pieces import *

def file_from_int(file_as_int):
    return chr(ord("a")+file_as_int)


for x in range(8):
    Pawn(Square(file_from_int(x), 2), False)


def redraw():
    board = Board()
    board.draw()
    white.draw()
    black.draw()


def captureWhite():
    global mouseClick
    file = files[int((mouseClick.x - 100)/50)]
    rank = 8 - int((mouseClick.y - 100)/50)
    i = 0
    for piece in white._pieces:
        rankOk = piece._square._rank == rank
        fileOk = piece._square._file == file
        captureOwnPiece()
        if rankOk and fileOk:
            white._pieces.pop(i)
            break
        else:
            i += 1


def captureBlack():
    global mouseClick
    file = files[int((mouseClick.x - 100)/50)]
    rank = 8 - int((mouseClick.y - 100)/50)
    i = 0
    for piece in black._pieces:
        rankOk = piece._square._rank == rank
        fileOk = piece._square._file == file
        captureOwnPiece()
        if rankOk and fileOk:
            black._pieces.pop(i)
            break
        else:
            i += 1


def captureOwnPiece():
    global mouseClick
    global movingPiece
    file = movingPiece._square.get_file_as_int()
    rank = movingPiece._square.get_rank()
    i = 0
    if movingPiece._is_black:
        for piece in black._pieces:
            rankOk = piece._square._rank == rank
            fileOk = piece._square._file == file
            if rankOk and fileOk:
                moveBlack()
                break
            else:
                i += 1
    else:
        for piece in white._pieces:
            rankOk = piece._square._rank == rank
            fileOk = piece._square._file == file
            if rankOk and fileOk:
                moveWhite()
                break
            else:
                i += 1



def moveWhite():
    global selected_square
    global mouseClick
    global movingPiece
    mouseClick = shared.win.getMouse()
    print(mouseClick)
    file = files[int((mouseClick.x - 100)/50)]
    rank = 8 - int((mouseClick.y - 100)/50)
    shared.selected_square = Square(file, rank)
    redraw()
    movingPiece = None
    for piece in white._pieces:
        rankOk = piece._square._rank == rank
        fileOk = piece._square._file == file
        if rankOk and fileOk:
            movingPiece = piece
            break
    mouseClick = shared.win.getMouse()
    print(mouseClick)
    file = files[int((mouseClick.x - 100)/50)]
    rank = 8 - int((mouseClick.y - 100)/50)
    if movingPiece:
        captureBlack()
        movingPiece.move_to(file, rank)
    else:
        moveWhite()


def moveBlack():
    global selected_square
    global mouseClick
    global movingPiece
    mouseClick = shared.win.getMouse()
    print(mouseClick)
    file = files[int((mouseClick.x - 100)/50)]
    rank = 8 - int((mouseClick.y - 100)/50)
    shared.selected_square = Square(file, rank)
    redraw()
    movingPiece = None
    for piece in black._pieces:
        rankOk = piece._square._rank == rank
        fileOk = piece._square._file == file
        if rankOk and fileOk:
            movingPiece = piece
            break
    mouseClick = shared.win.getMouse()
    print(mouseClick)
    file = files[int((mouseClick.x - 100)/50)]
    rank = 8 - int((mouseClick.y - 100)/50)
    if movingPiece:
        captureWhite()
        movingPiece.move_to(file, rank)
    else:
        moveBlack()


shared.win = GraphWin("My window", 600, 600)
shared.win.setBackground(color_rgb(255, 255, 255))
print("My Chess Program")
board = Board()
board.draw()
white = Player(False)
white.draw()
black = Player(True)
black.draw()
for i in range(100):
    moveWhite()
    redraw()
    moveBlack()
    redraw()
shared.win.getMouse()
shared.win.close()