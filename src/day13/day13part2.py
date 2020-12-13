"""
Day 13 Part 2

This part is basically chinese remainder theorem.

All service numbers are prime and thus coprime
"""

file_contents = []

f = open("day13input.txt", "r")
for file_line in f:
    file_contents.append(file_line.rstrip())
f.close()

# Only care about service numbers this time
list_of_services = file_contents[1].split(',')
list_of_running_services = []
list_of_mods = []

for i in range(len(list_of_services)):
    if list_of_services[i].isnumeric():
        list_of_running_services.append(int(list_of_services[i]))
        list_of_mods.append(i % int(list_of_services[i]))

services = list_of_running_services

print(services)

list_of_coeffs = []

for service in services:
    l = services.copy()
    l.remove(service)
    coeff_tot = 1
    for s in l:
        coeff_tot *= s
    list_of_coeffs.append(coeff_tot)

print(list_of_coeffs)


def find_lowest_sat_mod(xmody: int, coeff: int, y: int) -> int:
    print('finding lowest mult of: ' + str(coeff) + ' s.t. it = ' + str(xmody) + ' mod ' + str(y))
    i = 1
    coeff_mod_y = coeff % y
    original_coeff = coeff
    a = 0
    while True:
        a = coeff % y
        if a == xmody:
            break
        i += 1
        coeff = (i % y) * coeff_mod_y

    print('found')
    print(original_coeff * i)
    return original_coeff * i


out = 0

for i in range(len(services)):
    out += find_lowest_sat_mod(list_of_mods[i], list_of_coeffs[i], services[i])

print(' out = ' + str(out))

x = 1
divisor = 1
for i in range(len(services)):
    divisor *= list_of_running_services[i]


print(divisor-(out % divisor))
