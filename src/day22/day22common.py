"""
Common stuff for day 22
"""


def set_up() -> list:
    player_1_cards = []
    player_2_cards = []

    p = 1

    f = open("day22input.txt", "r")
    for file_line in f:
        if 'Player 1' in file_line:
            continue
        if 'Player 2' in file_line:
            p = 2
            continue
        if file_line == '\n':
            continue
        if p == 1:
            player_1_cards.append(int(file_line.rstrip()))
        if p == 2:
            player_2_cards.append(int(file_line.rstrip()))
    f.close()

    return [player_1_cards, player_2_cards]
