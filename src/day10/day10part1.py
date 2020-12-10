# Day 10 part 1

# these are not strictly charges in the list already but are needed as part of the gap numbers.
chargers = [0, 158]

f = open("day10input.txt", "r")
for file_line in f:
    chargers.append(int(file_line.rstrip()))
f.close()

# dictionary to store the number of gaps of each size
dict_of_gaps = {'1': 0, '2': 0, '3': 0}

# sort the list
sorted_chargers = sorted(chargers)

# add gaps to the list
for i in range(len(sorted_chargers)-1):
    dict_of_gaps[str(sorted_chargers[i+1]-sorted_chargers[i])] += 1

print('# gaps of one * # gaps of 3: ' + str(dict_of_gaps['1']*dict_of_gaps['3']))