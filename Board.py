from Ship import Ship

class Board:
    def __init__(self, player_board):
        '''
        Initalizes a list of Class Ship
        bool player_board is to see if player controls this board
        '''
        self.player_board = player_board
        self.ships = []
        self.all_hits = []
        self.all_misses = []
        self.all_ship_locs = []
        self.amount_sunk = 0

    def shoot_at(self, loc):
        '''
        Given a tuple loc, checks if tuple is at any loc in ships
        Returns a hit_and_sunk list, bool1 is hit, bool2 is sunk
        Calls ship.hit_attempt, updating hit_locs and sunk accordingly
        '''
        for ship in self.ships:
            hit_and_sunk = ship.hit_attempt(loc)
            if hit_and_sunk[0] == True:
                self.all_hits.append(loc)
                return True
        self.all_misses.append(loc)
        return False
    
    def create_ship(self, locs):
        '''
        Creates ship object with according locations, 
        adds obj to class's list 
        no return
        '''
        for loc in locs:
            self.all_ship_locs.append(loc)
        self.ships.append(Ship(locs))

    def update_amount_sunk(self):
        '''
        Counts and changes self.amount_sunk to be correct
        no return
        '''
        ships_sunk = 0
        for ship in self.ships:
            if ship.sunk:
                ships_sunk += 1
        self.amount_sunk = ships_sunk

    def check_loss(self):
        '''
        returns True if all ships are sunk
        else, returns false
        '''
        for ship in self.ships:
            if ship.sunk == False:
                return False
        return True        