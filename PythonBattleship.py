from UserInterface import UserInterface
from Board import Board
from Robot import Robot
import os
ui = UserInterface()
user_board = Board(True)
robot_board = Board(False)
rob = Robot(robot_board)
for ship in [2, 3, 3, 4, 5]:
    rob.place_ship(ship)
ui.print_full_board(robot_board)
while True:
    hit = robot_board.shoot_at(ui.request_shoot_loc())
    ui.print_hidden_board(robot_board, message = hit)
