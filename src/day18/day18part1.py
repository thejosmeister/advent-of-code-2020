"""
Day 18 Part 1

A bit of parsing fun.
"""

from day18.day18common import set_up, find_leading_bracket
list_of_sums = set_up()


# Recursively evaluates a calculation.
def evaluate_calc(calc: str) -> int:
    # Just a number
    if len(calc) == 1:
        return int(calc)

    # Have a number and an operation at the end.
    if calc[-1].isnumeric():
        if calc[-2] == '+':
            return evaluate_calc(calc[:-2]) + int(calc[-1])
        if calc[-2] == '*':
            return evaluate_calc(calc[:-2]) * int(calc[-1])

    # Calculation ends with a bracket so must do that.
    index_of_bracket = find_leading_bracket(calc[:-1])

    # Whole calculation is in the brackets.
    if index_of_bracket == 0:
        return evaluate_calc(calc[index_of_bracket + 1:-1])

    # Some more of the calculation to the left of the open bracket.
    if calc[index_of_bracket - 1] == '+':
        return evaluate_calc(calc[:index_of_bracket - 1]) + evaluate_calc(calc[index_of_bracket + 1:-1])
    if calc[index_of_bracket - 1] == '*':
        return evaluate_calc(calc[:index_of_bracket - 1]) * evaluate_calc(calc[index_of_bracket + 1:-1])


print('Sum of answers: ' + str(sum([evaluate_calc(_sum) for _sum in list_of_sums])))
