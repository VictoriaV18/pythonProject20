class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass
def rps_game_winner(players):
    if len(players) != 2:
        raise WrongNumberOfPlayersError
    player1, move1 = players[0]
    player2, move2 = players[1]

    valid_moves = {'R', 'S', 'P'}

    if move1 not in valid_moves or move2 not in valid_moves:
        raise NoSuchStrategyError

    if move1 == move2:
        return f'{player1} {move1}'
    if (move1 == 'R' and move2 == 'S') or (move1 == 'S' and move2 == 'P') or (move1 =='P' or move2 == 'R'):
        return f'{player2} {move2}'
    return f'{player2} {move2}'
print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))