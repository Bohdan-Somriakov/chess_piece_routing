from Chess_piece import Chess_piece


class Knight(Chess_piece):
    def __init__(self, board_coords, board_id, first_vertex, target):
        super().__init__(board_coords, board_id, first_vertex, target)

    def valid_moves(self): #override
     valid_moves = []
     for elem in self.all_cells:
         for to_go in self.all_cells:
             condition_to_valid_moves = \
                 (abs(to_go[0] - elem[0]) == 1 and abs(to_go[1] - elem[1]) == 2) or (
                         abs(to_go[0] - elem[0]) == 2 and abs(to_go[1] - elem[1]) == 1)
             if (condition_to_valid_moves):
                 valid_moves.append((elem, to_go))
     return valid_moves