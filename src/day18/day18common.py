"""
Common stuff for day 18
"""


def set_up() -> list:
    list_of_sums = []

    f = open("day18input.txt", "r")
    for file_line in f:
        list_of_sums.append(file_line.rstrip().replace(" ", ""))
    f.close()

    return list_of_sums


# Looks back along string for the matching open bracket.
def find_leading_bracket(calc: str) -> int:
    num_of_leading = 0
    for i in range(len(calc) - 1, -1, -1):
        if calc[i] == ')':
            num_of_leading += 1
        elif calc[i] == '(':
            if num_of_leading == 0:
                return i
            else:
                num_of_leading -= 1
