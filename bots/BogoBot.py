from random import randint


def move(board) -> str:
    legalMoves: list = list(board.legal_moves)
    return str(legalMoves[randint(0, len(legalMoves)-1)])
