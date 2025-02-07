'''
pip install chess tqdm
'''

import chess
from contestants import white, black
from tqdm import tqdm

#! Settings
total_games: int = 100
white_wins: int = 0
black_wins: int = 0
ties: int = 0
last_winner: str = None

progress_bar = tqdm(range(total_games), desc="Games")
for i in progress_bar:
    #! Init/Reset Game
    progress_bar.set_description(f"Games (Last winner: {last_winner})")
    board: chess.Board = chess.Board()
    turns: int = 0
    #! Start Game
    while not board.is_game_over() and turns < 1000:
        # * Player 1 move
        move: str = white.move(board)
        if move is not None:
            board.push_uci(move)
        turns += 1
        if board.is_game_over():
            break
        # * Player 2 move
        move: str = black.move(board)
        if move is not None:
            board.push_uci(move)
        turns += 1
    #! Evaluate game outcome
    outcome = board.outcome()
    if outcome is not None:
        winner: bool = outcome.winner
        if winner is True:
            white_wins += 1
            last_winner: str = "White"
        elif winner is False:
            black_wins += 1
            last_winner: str = "Black"
    else:
        ties += 1

print("----------------------------------------------")
print(
    f"♚  White won {int(round((white_wins/total_games)*100, 1))}% of Games, that's {white_wins} times")
print(
    f"♔  Black won {int(round((black_wins/total_games)*100, 1))}% of Games, that's {black_wins} times")
print(
    f"⚔️  Game tied {int(round((ties/total_games)*100, 1))}% of Games, that's {ties} times")
print("-----------------------------------------------")
if white_wins == black_wins:
    print("=> No one Won! ⚔️  It's a Tie!")
else:
    print(
        f"=> The Winner is {"♚  White!" if white_wins > black_wins else "♔  Black!"}"
    )
