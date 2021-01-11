# Day 6 part 2


# Does what it says on the tin.
def number_of_q_everyone_answered_yes(answers: str) -> int:
    list_of_answers = answers.split()

    common = list_of_answers[0]

    # If there is only one lot of answers
    if len(list_of_answers) == 1:
        return len(common)

    for answers_for_person in list_of_answers[1:]:
        change = ''
        list_of_chars = list(answers_for_person)
        # common is reduced if answer in common cannot be found in answers_for_person
        for letter in common:
            if letter in list_of_chars:
                change += letter
        common = change

    return len(common)


list_of_q_answered = []
answers = ''

f = open("day6input.txt", "r")
for file_line in f:
    if file_line == '\n':
        list_of_q_answered.append(number_of_q_everyone_answered_yes(answers))
        answers = ''
        continue
    # create space delimited list of people's answers
    answers += file_line.rstrip() + ' '

f.close()


print('Questions that everyone in the group answered yes to: ' + str(sum(list_of_q_answered)))
