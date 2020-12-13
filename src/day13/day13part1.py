"""
Day 13 Part 1
"""

file_contents = []

f = open("day13input.txt", "r")
for file_line in f:
    file_contents.append(file_line.rstrip())
f.close()

earliest_departure = int(file_contents[0])

list_of_services = file_contents[1].split(',')
list_of_running_services = []

for service in list_of_services:
    if service.isnumeric():
        list_of_running_services.append(int(service))

time = earliest_departure - 1
a = True
winning_service = 0
departure_time = 0
while a:
    time += 1
    print('time: '+ str(time))
    for service in list_of_running_services:
        if time % service == 0:
            winning_service = service
            departure_time = time
            print(winning_service)
            print(departure_time-earliest_departure)
            a = False
            break

print((departure_time - earliest_departure) * winning_service)
