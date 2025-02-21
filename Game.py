import Board

class Game:
    def __init__(self):
        '''
        Declares player and ai board,
        sets game into a play mode
        '''
        self.game_in_progress = True
        self.player_board = Board(True)
        self.ai_board = Board(False)

    def create_ship(self, locs, is_player):
        '''
        Creates a ship on the appropriate board.
        No return
        '''
        if is_player:
            board = self.player_board
        else:
            board = self.ai_board
        
        board.create_ship(locs)
    
    def shoot(self, loc, at_player):
        '''
        Shoots at loc at correct user, if a ship is sunk, check for game loss.
        Returns a hit_and_sunk list. Bool1 is hit, bool2 is sunk
        Calls board.shoot_at Alters hit and sunk values of ships accordingly
        '''
        if at_player:
            board = self.player_board
        else:
            board = self.ai_board

        hit_and_sunk = self.board.shoot_at(loc)
        if hit_and_sunk[1] and board.check_loss:
            self.end_game(board)
        return hit_and_sunk
    
    def end_game(self, board):
        self.game_in_progress = False
        if board == self.player_board:
            print("You won")
        else:
            print("You lost")