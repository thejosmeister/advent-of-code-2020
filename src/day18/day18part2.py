
list_of_sums = []

# Create a list of lists to become an array of seats.
f = open("test.txt", "r")
for file_line in f:
    list_of_sums.append(file_line.rstrip().replace(" ",""))
f.close()


def find_trailing_bracket(calc: str) -> int:
    num_of_leading = 0
    for i in range(len(calc) - 1, -1, -1):
        if calc[i] == ')':
            num_of_leading += 1
        elif calc[i] == '(':
            if num_of_leading == 0:
                return i
            else:
                num_of_leading -= 1






def reduce(calc: str, top_level: bool) -> str:
    if calc.find('(') == -1:
        if top_level:
            return calc
        return str(evaluate_calc(calc))

    index_of_1st_close = calc.rfind(')')
    index_of_open = find_trailing_bracket(calc[:index_of_1st_close])

    if index_of_open == 0 and index_of_1st_close == len(calc) - 1:
        return reduce(calc[index_of_open + 1:-1], False)

    if index_of_open == 0 and index_of_1st_close != len(calc) - 1:
        return reduce(calc[index_of_open + 1: index_of_1st_close], False) + calc[index_of_1st_close + 1:]

    if index_of_1st_close == len(calc) - 1:
        return reduce(calc[:index_of_open - 1], True) + calc[index_of_open - 1] + reduce(calc[index_of_open + 1:-1], False)

    return reduce(calc[:index_of_open - 1], True) + calc[index_of_open - 1] + reduce(calc[index_of_open + 1:index_of_1st_close], False) + calc[index_of_1st_close + 1:]


def evaluate_calc(calc: str) -> int:
    things_to_mult = [sum(list(map(int, elts))) for elts in [_sum.split('+') for _sum in list(calc.split('*'))]]
    out = 1
    for num in things_to_mult:
        out *= num

    return out


def evaluate_line(line: str) -> int:
    reduced_line = reduce(line, True)
    print('reduced' + str(reduced_line))
    return evaluate_calc(reduced_line)


# print(evaluate_calc('3*4+1*2'))
list_of_answers = []

for a_sum in list_of_sums:
    print(a_sum)
    list_of_answers.append(evaluate_line(a_sum))
    print(list_of_answers)

print(list_of_answers)
print(sum(list_of_answers))