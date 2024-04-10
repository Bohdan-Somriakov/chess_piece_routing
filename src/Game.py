from Bishop import Bishop
from Board import Board
from Knight import Knight

class Game:
    def __init__(self, size):
        self.board = Board(size)

    def play(self):
        piece = input("Enter the name of the piece ('knight' or 'bishop') or ('k' or 'b'): ")
        target = input("Enter the target or None: ")
        self.board.print_boards()
        piece_obj = self.create_piece(piece, target)
        self.print_piece_info(piece_obj)
        self.visualize_path(piece_obj, target)

    def create_piece(self, piece, target):
        first_vertex = 1

        if piece == 'knight' or piece == 'k':
            return self.create_knight(first_vertex, target)
        elif piece == 'bishop' or piece == 'b':
            return self.create_bishop(first_vertex, target)

    def create_knight(self, first_vertex, target):
        if target != "None":
            return Knight(self.board.board_coords, self.board.board_id, first_vertex, int(target))
        else:
            return Knight(self.board.board_coords, self.board.board_id, first_vertex, None)

    def create_bishop(self, first_vertex, target):
        if target != "None":
            return Bishop(self.board.board_coords, self.board.board_id, first_vertex, int(target))
        else:
            return Bishop(self.board.board_coords, self.board.board_id, first_vertex, None)

    def print_piece_info(self, piece_obj):
        print(piece_obj)
        piece_obj.show_edges_by_vertices()

    def visualize_path(self, piece_obj, target):
        strategy = input("Enter the strategy (width, depth, random) or (w, d, r): ")

        if target == "None":
            if strategy == "width" or strategy == "w":
                print("PATH: " + str(piece_obj.path_width))
                piece_obj.visual_path_width()
            elif strategy == "depth" or strategy == "d":
                print("PATH: " + str(piece_obj.path_depth))
                piece_obj.visual_path_depth()
            elif strategy == "random" or strategy == "r":
                print("PATH: " + str(piece_obj.path_random))
                piece_obj.visual_path_random()
        else:
            if strategy == "width" or strategy == "w":
                print("PATH: " + str(piece_obj.path_to_target_width))
                piece_obj.visual_path_width()
            elif strategy == "depth" or strategy == "d":
                print("PATH: " + str(piece_obj.path_to_target_depth))
                piece_obj.visual_path_depth()
            elif strategy == "random" or strategy == "r":
                print("PATH: " + str(piece_obj.path_to_target_random))
                piece_obj.visual_path_random()