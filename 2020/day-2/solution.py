import re

# Pattern to find the password policy and password.
pattern = "(\d+)-(\d+) (\w+): (\w+)"

first_part_count = 0
second_part_count = 0

# Get data from file.
with open("input.txt") as file:
    data = file.readlines()

# Check each password in the list of passwords.
for line in data:

    # Separate the data from the string with regular expression.
    n1, n2, letter, password = re.findall(pattern, line)[0]
    n1, n2 = int(n1), int(n2)

    # Check the number of times the letter appears in the password.
    if n1 <= password.count(letter) <= n2:
        first_part_count += 1

    # Check whether the letter appears only in one of the given positions.
    if password[n1 - 1] == letter and password[n2 - 1] == letter: continue
    elif password[n1 - 1] != letter and password[n2 - 1] != letter: continue
    else: second_part_count += 1

# Show the results.
print("First Part: {} correct passwords found!".format(first_part_count))
print("Second Part: {} correct passwords found!".format(second_part_count))
