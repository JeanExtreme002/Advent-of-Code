import re

def has_fields(passport):

    for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if not field in passport: return False

    return True

def has_only(string, chars):

    for char in string:
        if not char in chars: return False

    return True

def parse(string):

    passport = {}

    for field in re.findall("(\w{3}:[#\w]+)+", string):
        key, value = field.split(":")
        passport[key] = value

    return passport

def validate_fields(passport):

    if not 1920 <= int(passport["byr"]) <= 2002: return False
    if not 2010 <= int(passport["iyr"]) <= 2020: return False
    if not 2020 <= int(passport["eyr"]) <= 2030: return False

    if passport["hgt"].endswith("cm"):
        if not 150 <= int(passport["hgt"].replace("cm","")) <= 193: return False

    elif passport["hgt"].endswith("in"):
        if not 59 <= int(passport["hgt"].replace("in","")) <= 76: return False

    else:
        return False

    hcl_allowed_chars = [chr(i) for i in range(ord("a"), ord("z") + 1)]
    hcl_allowed_chars.extend([str(n) for n in range(10)])

    if not passport["hcl"].startswith("#"): return False
    if len(passport["hcl"][1:]) != 6 or not has_only(passport["hcl"][1:], hcl_allowed_chars): return False

    if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: return False

    if not len(passport["pid"]) == 9 or not passport["pid"].isnumeric(): return False
    return True

with open("input.txt") as file:
    data = file.read().split("\n\n")

first_part_count = 0
second_part_count = 0

for passport in data:

    if has_fields(passport):
        first_part_count += 1
        passport = parse(passport)
        if validate_fields(passport): second_part_count += 1

print("First Part: {} passports are valid.".format(first_part_count))
print("Second Part: {} passports are valid.".format(second_part_count))
