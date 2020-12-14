"""
Day 14 Part 1

Able to use python libraries to do most of the leg work in this part.
"""

file_contents = []

f = open("day14input.txt", "r")
for file_line in f:
    file_contents.append(file_line.rstrip())
f.close()

memory = {}
bitmask = ['']


# Applies bitmask to entry before insertion into memory
def apply_bitmask(inp: str) -> str:
    out = ''
    i = 0
    for char in bitmask:
        if char == 'X':
            out += inp[i]
        else:
            out += char
        i += 1
    return out


# Inserts a 36 bit binary string into memory after applying the bitmask.
def change_mem_address(_line: str):
    mem_address = int(_line.split(']')[0].split('[')[1])
    memory[mem_address] = apply_bitmask(format(int(_line.split(' = ')[1]), '036b'))


# Iterate through file making the appropriate changes for each line.
for line in file_contents:
    if line[:4] == 'mask':
        bitmask = list(line.split(' = ')[1])
    else:
        change_mem_address(line)

# Sum entries in memory.
sum_of_memory = 0
for entry in memory.keys():
    sum_of_memory += int(memory[entry], 2)

print('Sum of all values in memory: ' + str(sum_of_memory))
