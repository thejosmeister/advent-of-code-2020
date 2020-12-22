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


def play_game(p1_cards, p2_cards, flag: bool) -> list:
    # print('playing game')
    set_of_states = []
    rounds = 0
    while len(p1_cards) > 0 and len(p2_cards) > 0:
        rounds += 1
        if flag:
            print('round ' + str(rounds))
        p1_card = p1_cards.pop(0)
        p2_card = p2_cards.pop(0)

        if not flag:
            state = str(p1_card) + ',' + str(p2_card) + str(p1_cards) + str(p2_cards)
            if state in set_of_states:
                return [1, 0]
            set_of_states.append(state)

        if p1_card <= len(p1_cards) and p2_card <= len(p2_cards):
            game_result = play_game(p1_cards[0:p1_card], p2_cards[0:p2_card], False)
            if game_result[0] == 1:
                p1_cards.append(p1_card)
                p1_cards.append(p2_card)
            if game_result[0] == 2:
                p2_cards.append(p2_card)
                p2_cards.append(p1_card)

        else:
            # print('p1 ' + str(p1_card) + ' p2 ' + str(p2_card))
            # print('p1 ' + str(p1_cards))
            # print('p2 ' + str(p2_cards))
            if p1_card > p2_card:
                p1_cards.append(p1_card)
                p1_cards.append(p2_card)
            if p1_card < p2_card:
                p2_cards.append(p2_card)
                p2_cards.append(p1_card)

    result = 0
    mult = 1
    win = 0
    if len(p1_cards) > 0:
        win = 1
        if flag:
            for card in p1_cards[::-1]:
                result += card * mult
                mult += 1
    else:
        win = 2
        if flag:
            for card in p2_cards[::-1]:
                result += card * mult
                mult += 1
    print(str(win) + ' wins!')
    return [win, result]


out = play_game(player_1_cards, player_2_cards, True)


print(out)
