class UserInterface:
    def __init__(self):
        self.default_board = []
        for x in range(10):
            for y in range(10):
                self.default_board.append((x,y))
        
        self.default_drawn_board = ["\u134C\u134C"] * 100
        
    
    def draw_full_board(self,board):
        return board

    def draw_board(self,board):
        hit_locs = board
        new_board = self.default_drawn_board[:]
        for loc in hit_locs:
            print(self.default_board,10)
            loc_index = self.default_board.index(loc)
            new_board[loc_index] = "\u25A0 "
        
        for x in range(10):
            print("\n")
            for y in range(10):
                i = self.default_board.index((x,y))
                print(new_board[i], end= '  ')
        