
list_of_sums = []

# Create a list of lists to become an array of seats.
f = open("day17input.txt", "r")
for file_line in f:
    list_of_sums.append(list(file_line.rstrip()))
f.close()

def find_trailing_bracket(calc: str) -> int:


def evaluate_calc(calc: str) -> int:


def evaluate_brackets(calc: str) -> int:
    if '(' not in calc:
        return evaluate_calc(calc)

    return evaluate_brackets(calc[calc.find('(') + 1:find_trailing_bracket(calc)])

def evaluate_line(line: str) -> int:
    evaluate_brackets(line)