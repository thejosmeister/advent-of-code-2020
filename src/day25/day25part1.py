"""
Day 25 Part 1

Pretty quick and dirty brute force of Diffie-Hellman
Just count up powers of the subject number modulo the base till we get both of the input numbers.
Answer is then subject number to the power of the multiple of the two powers (modulo base).
"""
# Timing my efforts.
import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

numbers = []
subject_number = 7
base = 20201227

f = open("day25input.txt", "r")
for file_line in f:
    numbers.append(int(file_line.rstrip()))
f.close()

the_powers = [0, 0]

i = 2
num = 7
while True:
    calc = (num * subject_number) % base

    for j in [0, 1]:
        if calc == numbers[j] and the_powers[j] == 0:
            the_powers[j] = i
            print(str(numbers[j]) + ' is equal to ' + str(subject_number) + ' to the power of: ' + str(i))

    if the_powers[0] != 0 and the_powers[1] != 0:
        break
    num = calc
    i += 1

a_b = the_powers[0] * the_powers[1]
print('The common secret key is: ' + str(pow(subject_number, a_b, base)))

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
