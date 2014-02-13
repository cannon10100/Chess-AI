import pieces
from board import Board
from player import Player
from agent import Agent

game_board = Board()
self_player = Player(0, game_board) #white player
enemy_player = Player(1, game_board) #black player


game_agent = Agent(self_player, enemy_player, game_board)

print game_agent.run(game_board)