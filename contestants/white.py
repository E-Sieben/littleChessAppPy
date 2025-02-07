from random import randint


def move(board) -> str:
    legalMoves: list = list(board.legal_moves)
    maxMoves: int = len(legalMoves)-1
    if not board.is_stalemate() and not board.is_insufficient_material() and maxMoves > 0:
        return str(legalMoves[randint(0, maxMoves)])
