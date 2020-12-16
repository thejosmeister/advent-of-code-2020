"""
Day 16 Part 2

Was held up by the fact that I was modifying an array I was iterating through, oops.
"""
from day16.day16common import set_up, check_validity_of_ticket

set_up_values = set_up()

rules = set_up_values[0]
my_ticket = set_up_values[3]
other_tickets = set_up_values[2]


# remove non valid tickets
tickets_to_remove = []
for ticket in other_tickets:
    if check_validity_of_ticket(ticket, rules) > 0:
        tickets_to_remove.append(ticket)

for t in tickets_to_remove:
    other_tickets.remove(t)


# Look through list of tickets and add rows where, for all tickets, the row adheres to the rule.
rules_with_rows = {}

for rule in rules.keys():
    rows = []
    for row in range(20):
        total_sat = 0
        for ticket in other_tickets:
            if ticket[row] in rules[rule]:
                total_sat += 1
        if total_sat == len(other_tickets):
            rows.append(row)
    rules_with_rows[rule] = rows

# Now we want to reduce the map rules_with_rows by taking out the rows that can be assigned to a rule
# i.e. where a rule only has 1 viable row
# We can then remove this row from any other lists of rows for rules. This will (hopefully) mean another rule will only
# have one row now.
# Eventually, we should be able to deduct the row for all the rules.

# The map that we will populate with the row for each rule.
map_of_rules = {}


# Removes a rule name key from rules_with_rows
def remove_value_from_others(val: int, rwr: dict) -> dict:
    for r in rwr.keys():
        if val in rwr[r]:
            rwr[r].remove(val)
    return rwr


# Looks for rules with only one row number then takes the row number(s) away from the other row lists.
def deduct(rwr: dict) -> dict:
    global map_of_rules
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


# Apply the above till we have a complete map.
while len(map_of_rules.keys()) < 20:
    rules_with_rows = deduct(rules_with_rows.copy())

# Filter out the row numbers for row names with departure in.
indices = [map_of_rules[name] for name in list(filter(lambda x: ('departure' in x), list(map_of_rules.keys())))]

mult_together = 1
for index in indices:
    mult_together *= my_ticket[index]
print('Answer: ' + str(mult_together))
