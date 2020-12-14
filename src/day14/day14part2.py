"""
Day 14 Part 2

Slightly more tricky having to iterate through the combinations of turning X into 1 or 0.
"""

file_contents = []

f = open("day14input.txt", "r")
for file_line in f:
    file_contents.append(file_line.rstrip())
f.close()

memory = {}
address_decoder = ''


# Recursive function that will call itself with the first X in the input now a 1 or a 0.
def change_1st_x(inp: str) -> list:
    parts = inp.split('X')

    # No X in input so just return input
    if len(parts[0]) == len(inp):
        return [inp]

    out = []
    for add in change_1st_x(parts[0] + '0' + inp[len(parts[0]) + 1:]):
        out.append(add)
    for add in change_1st_x(parts[0] + '1' + inp[len(parts[0]) + 1:]):
        out.append(add)

    return out


# Returns the list of memory addresses created by applying the address decoder.
def apply_address_decoder(inp: str) -> list:
    out = ''
    i = 0
    for char in address_decoder:
        if char == '0':
            out += inp[i]
        else:
            out += char
        i += 1

    # Then want permutations of decoded address.
    return change_1st_x(out)


# Changes values for all decoded memory addresses to the value specified in the instruction.
def change_value_for_mem_addresses(_line: str):
    mem_address = format(int(_line.split(']')[0].split('[')[1]), '036b')
    list_of_addresses_to_change = apply_address_decoder(mem_address)

    for address in list_of_addresses_to_change:
        memory[int(address, 2)] = int(_line.split(' = ')[1])


# Iterate through file making the appropriate changes for each line.
for line in file_contents:
    if line[:4] == 'mask':
        address_decoder = line.split(' = ')[1]
    else:
        change_value_for_mem_addresses(line)

# Sum entries in memory.
sum_of_memory = 0
for entry in memory.keys():
    sum_of_memory += memory[entry]

print('Sum of all values in memory: ' + str(sum_of_memory))
