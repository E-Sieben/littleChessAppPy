import chess
from bots import BogoBot

board = chess.Board()
turns = 0
whiteWins = 0
blackWins = 0
ties = 0
for i in range(1000):
    # ? Game
    while not board.is_stalemate() and not board.is_insufficient_material() and turns < 1000 and len(list(board.legal_moves)) > 0:
        move = BogoBot.move(board)
        board.push_uci(move)
        if not board.is_stalemate() and not board.is_insufficient_material() and turns < 1000 and len(list(board.legal_moves)) > 0:
            move = BogoBot.move(board)
            board.push_uci(move)
        turns += 1
    # ? Eval
    try:
        outcome = board.outcome().winner
        if outcome == True:
            whiteWins = + 1
        elif outcome == False:
            blackWins += 1
        else:
            ties += 1
    except:
        outcome = None
    board.clear()
print(
    f"White won {whiteWins} times \nBlack won {blackWins} times \nThe Game tied {ties} times")
