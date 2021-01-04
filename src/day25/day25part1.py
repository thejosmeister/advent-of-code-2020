"""
Day 25 Part 1

Pretty quick and dirty brute force of Diffie-Hellman
"""

numbers = []
subject_number = 7
base = 20201227

f = open("day25input.txt", "r")
for file_line in f:
    numbers.append(int(file_line.rstrip()))
f.close()

the_powers = []

for number in numbers:
    i = 2
    while True:
        if pow(subject_number, i, base) == number:
            break
        i += 1
    print(str(number) + ' is equal to' + str(subject_number) + ' to the power of: ' + str(i))
    the_powers.append(i)

a_b = the_powers[0] * the_powers[1]
print('The common secret key is: ' + str(pow(subject_number, a_b, base)))
