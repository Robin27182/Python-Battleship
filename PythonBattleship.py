from UserInterface import UserInterface
from Board import Board
ui = UserInterface()
user_board = Board(True)
user_board.create_ship([(1,1),(1,2),(1,3),(1,4)])
user_board.create_ship([(4,1),(3,1),(2,1),(1,1)])
user_board.shoot_at((1,1))
user_board.shoot_at((5,1))
user_board.shoot_at((0,0))

ui.draw_hidden_board(user_board)