class UserInterface:
    def __init__(self):
        self.COORD_LIST = []
        for x in range(10):
            for y in range(10):
                self.COORD_LIST.append((x, y))
        
        self.DEFAULT_DRAWN_COORDS = ["default"] * 100
        
    
    def draw_full_board(self,board):
        new_draw_board = self.DEFAULT_DRAWN_COORDS[:]
        new_draw_board = self.replace_locs(board.all_ship_locs, " #", new_draw_board)
        new_draw_board = self.replace_locs(board.all_hits, " x", new_draw_board)
        new_draw_board = self.replace_locs(board.all_misses, " -", new_draw_board)
        new_draw_board = self.replace_default(" o", new_draw_board)
        self.print_board(new_draw_board)

    def draw_hidden_board(self, board):
        new_draw_board = self.DEFAULT_DRAWN_COORDS[:]
        new_draw_board = self.replace_locs(board.all_hits, " x", new_draw_board)
        new_draw_board = self.replace_locs(board.all_misses, " -", new_draw_board)
        new_draw_board = self.replace_default(" o", new_draw_board)
        self.print_board(new_draw_board)

    def print_board(self, drawn_board):
        print("   A  B  C  D  E  F  G  H  I  J", end= '')
        column_print = ["1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10"]
        for x in range(10):
            print( "\n" + column_print[x], end= '')
            for y in range(10):
                i = self.COORD_LIST.index((x, y))
                print(drawn_board[i], end= ' ')

    def replace_default(self, symbol, drawn_board):
        new_board = drawn_board[:]
        for i in range(len(new_board)):
            if new_board[i] == "default":
                new_board[i] = symbol
        return new_board

    def replace_locs(self, locs, symbol, drawn_board):
        new_board = drawn_board[:]
        for loc in locs:
            i = self.COORD_LIST.index(loc)
            new_board[i] = symbol
        return new_board

