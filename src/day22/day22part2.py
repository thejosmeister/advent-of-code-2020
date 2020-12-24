"""
Day 22 Part 2

A bit of recursion, solutions are getting slower (takes about 20 secs)
"""
from day22.day22common import set_up

[player_1_cards, player_2_cards] = set_up()


# Recursive game function, flag is used to denote the game that is the 'top' level
def play_game(p1_cards, p2_cards, flag: bool) -> list:
    set_of_states = []
    rounds = 0
    while len(p1_cards) > 0 and len(p2_cards) > 0:
        # Some logging for the round number of the top game
        rounds += 1
        if flag:
            print('round ' + str(rounds))
        p1_card = p1_cards.pop(0)
        p2_card = p2_cards.pop(0)

        # We can assume the top game does not need to keep track of the previous states.
        if not flag:
            state = str(p1_card) + ',' + str(p2_card) + str(p1_cards) + str(p2_cards)
            if state in set_of_states:
                return [1, 0]
            set_of_states.append(state)

        # The recursive situation
        if p1_card <= len(p1_cards) and p2_card <= len(p2_cards):
            game_result = play_game(p1_cards[0:p1_card], p2_cards[0:p2_card], False)
            if game_result[0] == 1:
                p1_cards.append(p1_card)
                p1_cards.append(p2_card)
            if game_result[0] == 2:
                p2_cards.append(p2_card)
                p2_cards.append(p1_card)
        # Plays out like part 1 otherwise
        else:
            if p1_card > p2_card:
                p1_cards.append(p1_card)
                p1_cards.append(p2_card)
            if p1_card < p2_card:
                p2_cards.append(p2_card)
                p2_cards.append(p1_card)

    # Calculate score of winner if it is the 'top' level game
    winning_score = 0
    mult = 1
    if len(p1_cards) > 0:
        winner = 1
        if flag:
            for card in p1_cards[::-1]:
                winning_score += card * mult
                mult += 1
    else:
        winner = 2
        if flag:
            for card in p2_cards[::-1]:
                winning_score += card * mult
                mult += 1
    return [winner, winning_score]


out = play_game(player_1_cards, player_2_cards, True)

print('Winning score: ' + str(out))
