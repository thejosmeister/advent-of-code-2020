# Day 4 part 2
import re

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


# Long ass method, probably not the cleanest
def validate_passport(passport: dict) -> int:
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if field not in passport.keys():
            return 0

    #byr
    if not passport['byr'].isnumeric():
        return 0
    if 1920 > int(passport['byr']) or 2002 < int(passport['byr']):
        return 0

    # iyr
    if not passport['iyr'].isnumeric():
        return 0
    if 2010 > int(passport['iyr']) or 2020 < int(passport['iyr']):
        return 0

    # eyr
    if not passport['eyr'].isnumeric():
        return 0
    if 2020 > int(passport['eyr']) or 2030 < int(passport['eyr']):
        return 0

    # hgt
    if re.search('1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in', passport['hgt']) is None:
        return 0

    # hcl
    if re.search('#[a-f0-9]{6}', passport['hcl']) is None:
        return 0

    # ecl
    colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if not passport['ecl'] in colours:
        return 0

    #pid
    if not passport['pid'].isnumeric():
        return 0
    if len(passport['pid']) != 9:
        return 0

    return 1


no_of_valid_passports = 0

# Counting up valid passports
for passport in list_of_passports:
    no_of_valid_passports += validate_passport(passport)

print('no of valid: ' + str(no_of_valid_passports))
