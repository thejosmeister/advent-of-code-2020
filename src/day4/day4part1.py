# Day 4 part 1

list_of_passports = []
set_of_creds = ''


# creates a dictionary of a passport from a space delimited list
def create_dict(line_of_creds: str) -> dict:
    out = {}
    parts = line_of_creds.split()
    for part in parts:
        out[part.split(':')[0]] = part.split(':')[1]

    return out


# creates a dictionary of a passport from a space delimited list
f = open("day4input.txt", "r")
for file_line in f:
    if file_line == '\n':
        list_of_passports.append(create_dict(set_of_creds))
        set_of_creds = ''
        continue
    # create space delimited list
    set_of_creds += file_line.rstrip() + ' '

f.close()


# check if all required fields are present
def validate_passport(passport: dict) -> int:
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if field not in passport.keys():
            return 0

    return 1


no_of_valid_passports = 0

# Counting up valid passports
for passport in list_of_passports:
    no_of_valid_passports += validate_passport(passport)

print('no of valid: ' + str(no_of_valid_passports))
