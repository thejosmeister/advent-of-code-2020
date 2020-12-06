# Day 6 part 1


# Output a list containing all the different questions answered
def create_set_of_q(answers: str) -> list:
    out = []
    for ans in answers:
        if ans not in out:
            out.append(ans)

    return out


list_of_q_answered = []
answers = ''

f = open("day6input.txt", "r")
for file_line in f:
    if file_line == '\n':
        list_of_q_answered.append(create_set_of_q(answers))
        answers = ''
        continue
    # shoving all answers into one big line
    answers += file_line.rstrip()

f.close()

count_of_all_answers = 0

# just sum the lengths of each list
for an in list_of_q_answered:
    count_of_all_answers += len(an)

print('Number of questions answered yes: ' + str(count_of_all_answers))
