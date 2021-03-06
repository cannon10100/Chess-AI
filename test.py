#!/usr/bin/python
import pieces
import board
import branch
import player
import random
import time

start_time = time.time()

foo = board.Board()

piece = pieces.Pawn()
print str(piece.points) + ": " + piece.name

foo.add_piece(piece)
bar = branch.Branch(piece, (1, 1))
foo.apply_branch(bar)

piece = pieces.Knight()
print str(piece.points) + ": " + piece.name

foo.add_piece(piece)
bar = branch.Branch(piece, (2, 2))
foo.apply_branch(bar)

piece = pieces.Bishop()
print str(piece.points) + ": " + piece.name

foo.add_piece(piece)
bar = branch.Branch(piece, (3, 3))
foo.apply_branch(bar)

piece = pieces.Rook()
print str(piece.points) + ": " + piece.name

foo.add_piece(piece)
bar = branch.Branch(piece, (4, 4))
foo.apply_branch(bar)

piece = pieces.Queen()
print str(piece.points) + ": " + piece.name

foo.add_piece(piece)
bar = branch.Branch(piece, (5, 5))
foo.apply_branch(bar)

spaz = board.Board()
spaz.add_piece(piece)

piece = pieces.King()
print str(piece.points) + ": " + piece.name

foo.add_piece(piece)
bar = branch.Branch(piece, (6, 6))
foo.apply_branch(bar)
bap = foo.create_branch_board(branch.Branch(piece, (7, 7)))
bap.add_piece(piece)

print foo.pieces
print bap.pieces
print foo.evaluate(0)
print foo.check_tile_empty((5,5))
print foo.check_tile_empty((5,3))

boards = [foo, spaz, bap]
boards.sort(key=board.Board.compare_board, reverse=True)

print boards[0].evaluate()
print boards[1].evaluate()
print boards[2].evaluate()

game_board = board.Board()
self_player = player.Player(0, game_board) #white player
enemy_player = player.Player(1, game_board) #black player

print "\nGame Board:\n"
moves = game_board.get_possible_moves(0)
print len(moves)
print "\nRandom Move:"
random_move = moves[random.randint(0, len(moves) - 1)]
print "From: " + str(random_move.previous_branch.from_location) + "  To: " + str(random_move.previous_branch.to_location) + "  Piece: " + str(random_move.previous_branch.piece)

print "\nTime: %f" % (time.time() - start_time)

