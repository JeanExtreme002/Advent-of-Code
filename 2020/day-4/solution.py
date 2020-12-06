import re

def has_fields(passport):

    # Check whether all required fields are in the passport.
    for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if not field in passport: return False
    return True

def has_only(string, chars):

    # Check whether the string contains only the specified characters.
    for char in string:
        if not char in chars: return False
    return True

def parse_passport(string):

    """
    Get the passport in string format and return the data in a dictionary.
    """

    passport = {}

    # Get each passport field with the regular expression.
    for field in re.findall("(\w{3}:[#\w]+)+", string):

        # Insert the key and value into the dictionary.
        key, value = field.split(":")
        passport[key] = value

    # Return the passport in a dictionary.
    return passport

def validate_fields(passport):
    """
    Validate the values ​​of each passport field.

    [byr] - Four digits; at least 1920 and at most 2002.
    [iry] - Four digits; at least 2010 and at most 2020.
    [ery] - Four digits; at least 2020 and at most 2030.
    [hgt] - A number followed by either "cm" or "in":
        - If "cm", the number must be at least 150 and at most 193.
        - If "in", the number must be at least 59 and at most 76.
    [hcl] - A "#" followed by exactly six characters 0-9 or a-f.
    [ecl] - Exactly one of: "amb", "blu", "brn", "gry", "grn", "hzl", "oth".
    [pid] - A nine-digit number, including leading zeroes.
    """

    # Validate fields with years.
    if not 1920 <= int(passport["byr"]) <= 2002: return False
    if not 2010 <= int(passport["iyr"]) <= 2020: return False
    if not 2020 <= int(passport["eyr"]) <= 2030: return False

    # Validate height field in "cm".
    if passport["hgt"].endswith("cm"):
        if not 150 <= int(passport["hgt"].replace("cm","")) <= 193: return False

    # Validate height field in "in".
    elif passport["hgt"].endswith("in"):
        if not 59 <= int(passport["hgt"].replace("in","")) <= 76: return False

    else: return False

    # Get all characters allowed in the "hcl" field.
    hcl_allowed_chars = [chr(i) for i in range(ord("a"), ord("z") + 1)]
    hcl_allowed_chars.extend([str(n) for n in range(10)])

    # Validate hair color field.
    if not passport["hcl"].startswith("#"): return False
    if len(passport["hcl"][1:]) != 6 or not has_only(passport["hcl"][1:], hcl_allowed_chars): return False

    # Validate eye color field.
    if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: return False

    # Validate passport ID field.
    if not len(passport["pid"]) == 9 or not passport["pid"].isnumeric(): return False
    return True

# Get data from file.
with open("input.txt") as file:
    data = file.read().split("\n\n")

first_part_count = 0
second_part_count = 0

# Validate each passport in the data list.
for passport in data:

    # First validation (has all required fields).
    if has_fields(passport):
        first_part_count += 1

        # Parse the passport and validate its data.
        passport = parse_passport(passport)
        if validate_fields(passport): second_part_count += 1

# Show the results.
print("First Part: {} passports are valid.".format(first_part_count))
print("Second Part: {} passports are valid.".format(second_part_count))
