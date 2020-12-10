# Day 10 part 2

chargers = [0, 158]

f = open("day10input.txt", "r")
for file_line in f:
    chargers.append(int(file_line.rstrip()))
f.close()

# We want out sorted list of chargers again
sorted_chargers = sorted(chargers)

# To get the total permutations of chargers it centres around the fact that we only have gaps of 1 or 3 in the sorted
# list. Where there is a gap of 3 we must include that in every permutation. The permutations arise from then sequential
# gaps of 1. The permutation numbers for sequential gaps of 1 are outlined below.

# First we want to work out where the gaps of one are.
sequence_of_ones = 0
sequence_list = []
for i in range(len(sorted_chargers)-1):

    if sorted_chargers[i+1]-sorted_chargers[i] == 1:
        sequence_of_ones += 1
    else:
        sequence_list.append(sequence_of_ones)
        sequence_of_ones = 0

# Now we have a list of the gaps with sequential ones. If there are 2 gaps of 1 then there are two ways (1,1) and (2).
# 3 gaps has 4 ways (1,1,1), (2,1), (1,2) and (3)
# 4 gaps has 7 ways (1,1,1,1), (1,1,2), (1,2,1), (2,1,1), (2,2), (3,1) and (1,3)
# Fortunately there were no more than 4 in a row.
# To get the total number of permutations we just multiply all these permutation numbers together for each sequence.
out = 1
for num in sequence_list:
    if num == 3:
        out *= 4
    if num == 4:
        out *= 7
    if num == 2 or num == 1:
        out *= num

print('Total # ways to arrange chargers: ' + str(out))
