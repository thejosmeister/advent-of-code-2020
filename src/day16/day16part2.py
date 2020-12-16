
rules = {}
my_ticket = []
other_tickets = []

state = 0


def format_as_rule(line: str) -> list:
    valid_nums = []
    for i in range(int(line.split(': ')[1].split('-')[0]), int(line.split(': ')[1].split(' or ')[0].split('-')[1]) + 1):
        valid_nums.append(i)
    for i in range(int(line.split(' or ')[1].split('-')[0]), int(line.split(' or ')[1].split('-')[1]) + 1):
        valid_nums.append(i)

    return valid_nums


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


# def check_validity_of_ticket(_ticket: list) -> bool:
#     _rules = list(rule_names)
#
#     for value in ticket:
#         rules_satisfied = []
#         for rul in _rules:
#             if value in rules[rul]:
#                 rules_satisfied.append(rul)
#
#         if len(rules_satisfied) == 0:
#             print(str(value) + ': ' + str(ticket.index(value)))
#             return False
#
#     return True

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



# remove non valid tickets
tickets_to_remove = []
for ticket in other_tickets:
    if not check_validity_of_ticket(ticket):
        tickets_to_remove.append(ticket)


for t in tickets_to_remove:
    other_tickets.remove(t)


rules_with_rows = {}

for rule in rule_names:
    rows = []
    for row in range(20):
        total_sat = 0
        for ticket in other_tickets:
            if ticket[row] in rules[rule]:
                total_sat += 1
        if total_sat == len(other_tickets):
            rows.append(row)
    rules_with_rows[rule] = rows

map_of_rules = {}


def remove_value_from_others(val: int, rwr:dict ) -> dict:
    for r in rwr.keys():
        if val in rwr[r]:
            rwr[r].remove(val)
    return rwr


def deduct(rwr: dict) -> dict:
    global map_of_rules
    print(rwr)
    vals_to_remove = []
    list_of_rules = list(rwr.keys())
    for _rule in list_of_rules:
        if len(rwr[_rule]) == 1:
            map_of_rules[_rule] = rwr[_rule][0]
            vals_to_remove.append(rwr[_rule][0])
            del rwr[_rule]
    for val in vals_to_remove:
        rwr = remove_value_from_others(val, rwr.copy())

    return rwr


while len(map_of_rules.keys()) < 20:
    rules_with_rows = deduct(rules_with_rows.copy())

print(map_of_rules)

print(my_ticket[1] * my_ticket[8] * my_ticket[19] * my_ticket[10] * my_ticket[3] * my_ticket[6] )


