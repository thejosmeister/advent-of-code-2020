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


def play_round(p1_card: int, p2_card: int):
    global player_1_cards, player_2_cards
    if p1_card > p2_card:
        player_1_cards.append(p1_card)
        player_1_cards.append(p2_card)
    if p1_card < p2_card:
        player_2_cards.append(p2_card)
        player_2_cards.append(p1_card)


while len(player_1_cards) > 0 and len(player_2_cards) > 0:
    play_round(player_1_cards.pop(0), player_2_cards.pop(0))

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

print(out)
