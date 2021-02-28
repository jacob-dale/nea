from board import *
# Allows certain variables to be shared across files.
files = ["a", "b", "c", "d", "e", "f", "g", "h"]  # array useful for converting between int and str values
white_pieces = []
black_pieces = []
all_pieces = []
eval_storage_B = []
eval_storage_W = []
selected_square = None
redraw_square = Square("a", 4)
redraw_end_square = Square("a", 4)
win = None
white = None
black = None
board = None
turn = 0
move1 = []
initial = None
end_square = None
file_as_int_start = None
file_as_int_end = None
opponent_piece = False
legal = False
value = 0
best_value = 0
best_value_W = 0
depth = 0
deepness = 0
castle = None
en_passant_capture = None
castle_square = None


# Helper functions to convert the file to an int.
def file_to_int(file):
    return ord(file) - ord('a') + 1


# Do the square selection.
def select_square(file, rank):
    global selected_square
    global file_as_int_start
    if selected_square is None:
        selected_square = Square(file, rank)
    else:
        selected_square._file = file
        selected_square._rank = rank
    file_as_int_start = file_to_int(file)


# Set the square to move to.
def set_end_square(file, rank):
    global end_square
    global file_as_int_end
    if end_square is None:
        end_square = Square(file, rank)
    else:
        end_square._file = file
        end_square._rank = rank
    file_as_int_end = file_to_int(file)