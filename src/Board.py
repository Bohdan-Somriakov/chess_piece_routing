import numpy as np
class Board:
    def __init__(self, size):
        self.board_coords = self.make_board(size)
        self.board_id = self.make_board_id(size)

    def print_boards(self):
        print("board_id:\n" + "\n".join([" ".join(f"{elem:4}" for elem in row) for row in self.board_id]))
        print("board_coords:\n" + "\n".join(["  ".join(str(elem) for elem in row) for row in self.board_coords]))

    def make_board(self, size):
        return np.fromiter(((i, j) for i in range(size) for j in range(size)), dtype=object, count=size * size).reshape(
            (size, size))

    def make_board_id(self, size):
        return np.fromiter((count + 1 for count in range(size * size)), dtype=object, count=size * size).reshape(
            (size, size))