import os

# --- Conversions ---
def safe_convert(str, type):
    '''
    Tries to convert a string (or anything, really) into a different type
    If it fails, returns None
    '''
    try:
        return type(str)
    except:
        return None


def str_to_coords(str):
    '''
    Given a str, such as "a1", returns the battleship grid coords
    "a1" -> (0,0)
    "c7" -> (2,6)
    if it is an invalid string, returns (-1,-1)
    '''
    if type(str) is tuple:
        return str

    try:
        x_req = ord(str[0]) - 97
        y_req =  int(str[1:]) - 1
    except:
        return (-1,-1)

    if x_req > 9 or y_req > 9:
        return (0,0)

    return (x_req,y_req)


class UserInterface:
    def __init__(self):
        '''
        Creates default coordinate system, then makes a default drawn board
        drawn boards are just lists of strings to print in the 10 x 10 grid
        '''
        self.placing_ship = False
        self.COORD_LIST = []
        for x in range(10):
            for y in range(10):
                self.COORD_LIST.append((x, y))
        
        self.DEFAULT_DRAWN_COORDS = ["default"] * 100
        
    # --- Printing Player Board Methods ---

    def __replace_default(self, symbol, drawn_board):
        '''
        retuns a list of strings:
        Any string left from the DEFAULT_DRAWN_BOARD is replaced with str "symbol"
        '''
        new_board = drawn_board[:]
        for i in range(len(new_board)):
            if new_board[i] == "default":
                new_board[i] = symbol
        return new_board

    def __replace_locs(self, locs, symbol, drawn_board):
        '''
        Given a list of COORDINATES (tuples),
        replaces any str at location loc referencing COORD_LIST with str "symbol"
        '''
        new_board = drawn_board[:]
        for loc in locs:
            i = self.COORD_LIST.index(loc)
            new_board[i] = symbol
        return new_board

    def print_full_board(self, board, cls = True, message = ""):
        '''
        Takes in a player's board, from there adds all info about their board.
        This "new_draw_board" is passed into print_raw_board
        '''
        new_draw_board = self.DEFAULT_DRAWN_COORDS[:]
        new_draw_board = self.__replace_locs(board.all_ship_locs, " \u25A0", new_draw_board)
        new_draw_board = self.__replace_locs(board.all_hits, " x", new_draw_board)
        new_draw_board = self.__replace_locs(board.all_misses, " -", new_draw_board)
        new_draw_board = self.__replace_default(" o", new_draw_board)
        if cls:
            os.system("cls")
        print(message)
        self.__print_raw_board(new_draw_board)

    def print_hidden_board(self, board, cls = True,  message = ""):
        '''
        Takes in a player's board, from there adds all info EXCEPT for ship locations.
        This "new_draw_board" is passed into print_raw_board
        '''
        new_draw_board = self.DEFAULT_DRAWN_COORDS[:]
        new_draw_board = self.__replace_locs(board.all_hits, " x", new_draw_board)
        new_draw_board = self.__replace_locs(board.all_misses, " -", new_draw_board)
        new_draw_board = self.__replace_default(" o", new_draw_board)
        if cls:
            os.system("cls")
        print(message)
        self.__print_raw_board(new_draw_board)

    def __print_raw_board(self, drawn_board):
        """
        Separates and prints a "drawn_board" Not a board object, jsut a list of values.
        Puts the previous list of values in a 10 x 10 grid accordingly
        Prints as a return
        """
        end_string = "   1  2  3  4  5  6  7  8  9  10"
        column_print = ["A ","B ","C ","D ","E ","F ","G ","H ","I ","J "]
        for x in range(10):
            end_string +=  "\n" + column_print[x]
            for y in range(10):
                i = self.COORD_LIST.index((x, y))
                end_string += drawn_board[i] + " "
        print(end_string)

    # --- Firing On Board ---

    def request_shoot_loc(self):
        """
        Requests the user to fire at a location such as "a1", then interacts with a board to do the action if it is valid
        """
        valid_ans = False
        while not valid_ans:
            respond = str(input("\nFire at: "))
            shot_loc = str_to_coords(respond)
            if shot_loc != (-1,-1):
                valid_ans = True
        return shot_loc

    # --- Adding Ships (mostly UI) ---

    def is_valid_ship_loc(self, board, loc):
        """
        Returns a boolean for if a ship_loc can reside at that point
        returns false if off the board or if there is a ship there
        else, returns true
        """
        if loc[0] < 0 or loc[0] > 9:
            return False
        elif loc[1] < 0 or loc[1] > 9:
            return False
        elif loc in board.all_ship_locs:
            return False
        return True

    def __ship_placing_print(self, board, size, rot):
        """
        Prints Unicode empty and filled boxes to visually rotate the ship
        Used to let the user see where place it, and in what orientation
        """
        marked = "\u25A0  "
        norm = "\u25A1  "
        space_hoz = [[""] * ((size)//2), [""] * size]
        correct_rot = []

        match rot:
            case 1: correct_rot = space_hoz[0] + [marked + norm * (size - 1)] + space_hoz[1]
            case 3: correct_rot = space_hoz[0] + [norm * (size - 1) + marked] + space_hoz[1]
            case 2: correct_rot = [marked] + [norm] * (size - 1)
            case 4: correct_rot = [norm] * (size - 1) + [marked]

        os.system("cls")
        for i in range(size):
            print(correct_rot[i])
        self.print_full_board(board, False)

    def req_opt_or_coord(self, board, size):
        rot = 1
        self.__ship_placing_print(board, size, rot)
        while True:
            respond = input("Enter 1 to rotate ship\nEnter coordinate to place highlighted square: ")
            poss_loc = str_to_coords(respond)

            if poss_loc != (-1, -1) or safe_convert(respond, int) == 1:
                if safe_convert(respond, int) == 1:  # Rotate ship
                    rot = rot + 1 if rot < 4 else 1
                    self.__ship_placing_print(board, size, rot)
                else:
                    break
        return respond, rot

    def user_ship_request(self, board, size):
        valid_placing = True
        while valid_placing:
            respond, rot = self.req_opt_or_coord(board, size)
            if self.__ship_place_success(board, size, rot, respond):
                valid_placing = False

    def robot_ship_request(self, board, size, rot, coord):
        return self.__ship_place_success(board, size, rot, coord)

    def __ship_place_success(self, board, size, rot, coord):
        '''
        Default Parameters are for the AI to pass in, not the user.
        This calls ship placement UI (as seen above) to have the user interact with the board and place ships
        '''

        loc = str_to_coords(coord)
        locs = [
            (loc[0], loc[1] + segment) if rot == 1 else
            (loc[0] + segment, loc[1]) if rot == 2 else
            (loc[0], loc[1] - segment) if rot == 3 else
            (loc[0] - segment, loc[1]) # rot == 4
            for segment in range(size)
        ]

        if all(self.is_valid_ship_loc(board, location) for location in locs):
            board.create_ship(locs)
            return True
        return False