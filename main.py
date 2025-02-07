'''
pip install chess tqdm
'''

import chess
from contestants import white, black
from tqdm import tqdm

total_games = 100
white_wins = 0
black_wins = 0
ties = 0
last_winner = None

progress_bar = tqdm(range(total_games), desc="Games")

for i in progress_bar:
    board = chess.Board()
    turns = 0
    while not board.is_game_over() and turns < 1000:
        # * Player 1 move
        move = white.move(board)
        if move is not None:
            board.push_uci(move)
        turns += 1
        if board.is_game_over():
            break
        # * Player 2 move
        move = black.move(board)
        if move is not None:
            board.push_uci(move)
        turns += 1
    # Evaluate game outcome
    outcome = board.outcome()
    if outcome is not None:
        winner = outcome.winner
        if winner is True:
            white_wins += 1
            last_winner = "White"
        elif winner is False:
            black_wins += 1
            last_winner = "Black"
    else:
        ties += 1
    # Update progress bar description
    progress_bar.set_description(f"Games (Last winner: {last_winner})")

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
