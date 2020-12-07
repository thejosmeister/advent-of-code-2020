# Day 7 part 1
from day7.day7common import create_list_of_instructions


list_of_instructions = create_list_of_instructions()


# Will return 1 if the bag colour contains a shiny gold bag
def bag_contains_shiny_gold(bag_colour: str) -> int:
    global list_of_instructions

    # No bags in this bag
    if list_of_instructions[bag_colour] == 0:
        return 0

    # Directly contains a shiny gold bag
    if 'shiny gold' in list_of_instructions[bag_colour].keys():
        return 1

    # If neither of the above hold then wee need to check all the bags inside
    out = 0

    for colour in list_of_instructions[bag_colour].keys():
        out += bag_contains_shiny_gold(colour)

    # I'm sure there must be a more succinct way for this.
    if out > 0:
        return 1
    return 0


bags_that_hold_shiny_ones = 0

for bag in list_of_instructions.keys():
    bags_that_hold_shiny_ones += bag_contains_shiny_gold(bag)

print('Number of bags containing shiny gold: ' + str(bags_that_hold_shiny_ones) )
