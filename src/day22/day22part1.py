"""
Day 22 Part 1

A fun game
"""
from day22.day22common import set_up

[player_1_cards, player_2_cards] = set_up()


def play_round(p1_card: int, p2_card: int):
    global player_1_cards, player_2_cards
    if p1_card > p2_card:
        player_1_cards.append(p1_card)
        player_1_cards.append(p2_card)
    if p1_card < p2_card:
        player_2_cards.append(p2_card)
        player_2_cards.append(p1_card)


# Play a game
while len(player_1_cards) > 0 and len(player_2_cards) > 0:
    play_round(player_1_cards.pop(0), player_2_cards.pop(0))


# Work out winning score
out = 0
mult = 1
if len(player_1_cards) > 0:
    for card in player_1_cards[::-1]:
        out += card * mult
        mult += 1
else:
    for card in player_2_cards[::-1]:
        out += card * mult
        mult += 1

print('Winning score: ' + str(out))
