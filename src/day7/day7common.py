# Common stuff for day 7

def create_instruction(line: str, list_of_i: dict) -> dict:
    halves = line.split(' bags contain ')
    rhs = {}

    if halves[1] == 'no other bags.':
        list_of_i[halves[0]] = 0
        return list_of_i

    for part in halves[1].split(', '):
        rhs[part.split(' ')[1] + ' ' + part.split(' ')[2]] = int(part.split(' ')[0])

    list_of_i[halves[0]] = rhs
    return list_of_i


def create_list_of_instructions() -> dict:
    list_of_instructions = {}

    f = open("day7input.txt", "r")
    for file_line in f:
        list_of_instructions = create_instruction(file_line.rstrip(), list_of_instructions)
    f.close()

    return list_of_instructions
