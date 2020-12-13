"""
Day 13 Part 1

The fact this was easy meant I was already gearing up for a hard part 2.
"""

file_contents = []

f = open("day13input.txt", "r")
for file_line in f:
    file_contents.append(file_line.rstrip())
f.close()

# The time I can make my earliest departure
earliest_departure = int(file_contents[0])


list_of_services = file_contents[1].split(',')
list_of_running_services = []

# filter out services that are running
for service in list_of_services:
    if service.isnumeric():
        list_of_running_services.append(int(service))

# Test to see which service arrives first after the earliest time.
time = earliest_departure - 1
a = True
winning_service = 0
departure_time = 0
while a:
    time += 1
    for service in list_of_running_services:
        if time % service == 0:
            winning_service = service
            departure_time = time
            a = False
            break

print('Service taken: ' + str(winning_service))
print('time of departure: ' + str(departure_time-earliest_departure))
print('Time waiting * service number: ' + str((departure_time - earliest_departure) * winning_service))
