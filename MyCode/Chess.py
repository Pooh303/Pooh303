import chess

# Create a new chess game
game = chess.Board()

# Make a move
game.push_san("e4")
game.push_san("e5")

# Print the current board position
print(game)
