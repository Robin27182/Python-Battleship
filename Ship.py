class Ship:
    def __init__(self, board_locs):
        '''
        Initializes the locations on the board the ship resides in, 
        the locations that the ship has been hit,
        and if it has been sunk or not
        '''
        self.board_locs = board_locs # Holds tuples
        self.hit_locs = [] # Holds tuples
        self.sunk = False

    def check_sunk(self):
        '''
        if sunk, return true and alter "sunk", else returns false
        '''
        for ship_segment in self.board_locs:
            if ship_segment not in self.hit_locs:
                return False
        self.sunk = True
        return True
                
    def hit_attempt(self, loc):
        """
        Given a tuple, if the tuple is one of its locs, it is hit 
        returns a hit_and_sunk list, bool1 for hit, bool2 for sunk
        """
        hit_and_sunk = [False, False]
        print(loc,self.board_locs)
        if loc in self.board_locs:
            self.hit_locs.append(loc)
            hit_and_sunk[0] = True
            hit_and_sunk[1] = self.check_sunk()
        return hit_and_sunk
    
