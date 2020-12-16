"""
Day 16 Part 1

Made this a lot harder than it needed to be as I was originally finding tickets where all the values didn't match up.
Should have read the question more carefully.
"""
from day16.day16common import set_up, check_validity_of_ticket

set_up_values = set_up()

rules = set_up_values[0]
my_ticket = set_up_values[3]
other_tickets = set_up_values[2]

error = 0
# Add all the error together.
for ticket in other_tickets:
    error += check_validity_of_ticket(ticket, rules)

print('Sum of error ' + str(error))
