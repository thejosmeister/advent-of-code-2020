"""
Day 16 Part 1

Made this a lot harder than it needed to be as I was originally finding tickets where all the values didn't match up.
Should have read the question more carefully.
"""

rules = {}
my_ticket = []
other_tickets = []
# Used to work out where we are in the doc.
state = 0


# Takes line and turns into dict entry with a list of valid values for the rule.
def format_as_rule(line: str) -> list:
    valid_nums = []
    for i in range(int(line.split(': ')[1].split('-')[0]), int(line.split(': ')[1].split(' or ')[0].split('-')[1]) + 1):
        valid_nums.append(i)
    for i in range(int(line.split(' or ')[1].split('-')[0]), int(line.split(' or ')[1].split('-')[1]) + 1):
        valid_nums.append(i)

    return valid_nums


# Add file lines to the relevant lists.
f = open("day16input.txt", "r")
for file_line in f:
    if file_line == '\n':
        continue
    if file_line.rstrip() == 'your ticket:':
        state = 1
        continue
    if file_line.rstrip() == 'nearby tickets:':
        state = 2
        continue
    if state == 0:
        rules[file_line.split(':')[0]] = format_as_rule(file_line.rstrip())
    if state == 1:
        my_ticket = [int(i) for i in file_line.rstrip().split(',')]
    if state == 2:
        other_tickets.append([int(i) for i in file_line.rstrip().split(',')])
f.close()

rule_names = rules.keys()


# Returns the amount of error in the ticket (the values that don't adhere to any rules)
def check_validity_of_ticket(_ticket: list) -> int:
    out = 0
    _rules = list(rule_names)
    for value in ticket:
        rules_satisfied = []
        for rule in _rules:
            if value in rules[rule]:
                rules_satisfied.append(rule)

        if len(rules_satisfied) == 0:
            out += value
            continue
    return out


error = 0
# Add all the error together.
for ticket in other_tickets:
    error += check_validity_of_ticket(ticket)

print('Sum of error ' + str(error))

