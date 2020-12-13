"""
Day 13 Part 2

This part is basically chinese remainder theorem.

All service numbers are prime and thus coprime so we can apply CRT.

To preform this I will have an eqn in the form

a*x + time = b0*x0 + ... + bn*xn where:
a, b0,...,bn >0 , x = all service numbers mult toegther, xi = x/ith service no.,
time = the time of arrival of the first bus where we then get the sequential arrivals

We will be able to find 'a*x + time' by computing the RHS using the fact that 'xi mod service no.[j] = 0 for all i != j'
We can then find time using the fact a is a natural number.
"""

file_contents = []

f = open("day13input.txt", "r")
for file_line in f:
    file_contents.append(file_line.rstrip())
f.close()

# Only care about service numbers this time
list_of_services = file_contents[1].split(',')
# Each service number x minutes past the time for the 1st service so will be 'time = x mod service no.'
# We have to take into account x > service number by using the fact that the service will just arrive n times before
# our x so 'x = n * service no. + y' with y < service no.
list_of_running_services = []
list_of_mods = []
for i in range(len(list_of_services)):
    if list_of_services[i].isnumeric():
        list_of_running_services.append(int(list_of_services[i]))
        # find y from above ( y = x for service no. > x )
        list_of_mods.append(i % int(list_of_services[i]))

# Now we want to find our initial coefficients for the CRT eqn (the xi stated at the top)
list_of_coeffs = []
for service in list_of_running_services:
    l = list_of_running_services.copy()
    l.remove(service)
    coeff_tot = 1
    for s in l:
        coeff_tot *= s
    list_of_coeffs.append(coeff_tot)

print(list_of_coeffs)


# I had to fettle this method a bit by taking mods throughout the calculation as if i simply kept multiplying the coefficient xi by
def find_lowest_mult_of_coeff_that_satisfies_mod_condition(mod_conditon: int, coeff: int, service_no: int) -> int:
    print('finding lowest mult of: ' + str(coeff) + ' s.t. it = ' + str(mod_conditon) + ' mod ' + str(service_no))
    j = 1
    coeff_mod_y = coeff % service_no
    original_coeff = coeff
    while True:
        a = coeff % service_no
        if a == mod_conditon:
            break
        j += 1
        coeff = (j % service_no) * coeff_mod_y

    print('found')
    print(original_coeff * j)
    return original_coeff * j


out = 0

for i in range(len(list_of_running_services)):
    out += find_lowest_mult_of_coeff_that_satisfies_mod_condition(list_of_mods[i], list_of_coeffs[i], list_of_running_services[i])

print(' out = ' + str(out))

x = 1
divisor = 1
for i in range(len(list_of_running_services)):
    divisor *= list_of_running_services[i]


print(divisor-(out % divisor))
