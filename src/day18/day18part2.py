"""
Day 18 Part 2

The parsing fun continues.
"""
from day18.day18common import set_up, find_leading_bracket
list_of_sums = set_up()


# Evaluates a calculation with no brackets present i.e '1 + 2 * 3'
def evaluate_calc(calc: str) -> int:
    things_to_mult = [sum(list(map(int, elts))) for elts in [_sum.split('+') for _sum in list(calc.split('*'))]]
    out = 1
    for num in things_to_mult:
        out *= num

    return out


# 'Reduces' what is inside a pair of brackets. / Evaluates whats inside a pair of brackets
def reduce(calc: str) -> str:

    # No brackets so no reducing needed.
    if calc.find('(') == -1:
        return calc

    # Find 1st close bracket and corresponding open.
    index_of_1st_close = calc.rfind(')')
    index_of_open = find_leading_bracket(calc[:index_of_1st_close])

    # There are 4 cases:
    # - ( calc )
    # - ( calc1 ) calc2, calc2 has no brackets
    # - calc1 ( calc2 )
    # - calc1 ( calc2 ) calc3, calc3 has no brackets
    if index_of_open == 0 and index_of_1st_close == len(calc) - 1:
        return str(evaluate_calc(reduce(calc[index_of_open + 1:-1])))
    if index_of_open == 0 and index_of_1st_close != len(calc) - 1:
        return str(evaluate_calc(reduce(calc[index_of_open + 1: index_of_1st_close]))) + calc[index_of_1st_close + 1:]
    if index_of_1st_close == len(calc) - 1:
        return reduce(calc[:index_of_open - 1]) + calc[index_of_open - 1] + str(evaluate_calc(reduce(calc[index_of_open + 1:-1])))
    return reduce(calc[:index_of_open - 1]) + calc[index_of_open - 1] + str(evaluate_calc(reduce(calc[index_of_open + 1:index_of_1st_close]))) + calc[index_of_1st_close + 1:]


print('Sum of answers: ' + str(sum([evaluate_calc(reduce(_sum)) for _sum in list_of_sums])))
