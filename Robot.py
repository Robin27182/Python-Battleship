import random as rand
from UserInterface import UserInterface

class Robot:
    def __init__(self, board):
        self.board = board
        self.ui = UserInterface()
    def __coord_to_string(self,coord):
        return
    def place_ship(self, size):
        placed_ship = False
        while not placed_ship:
            coord = (rand.randint(1,10),rand.randint(1,10))
            rot = rand.randint(1, 4)
            placed_ship = self.ui.robot_ship_request(self.board, size, rot, coord)