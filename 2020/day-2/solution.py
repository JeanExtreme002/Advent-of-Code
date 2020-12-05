import re

pattern = "(\d+)-(\d+) (\w+): (\w+)"

first_part_count = 0
second_part_count = 0

with open("input.txt") as file:
    data = file.readlines()

for line in data:

    n1, n2, letter, password = re.split(pattern, line.strip())[1: -1]
    n1, n2 = int(n1), int(n2)

    if n1 <= password.count(letter) <= n2:
        first_part_count += 1

    if password[n1 - 1] == letter and password[n2 - 1] == letter: continue
    elif password[n1 - 1] != letter and password[n2 - 1] != letter: continue
    else: second_part_count += 1

print("First Part: {} correct passwords found!".format(first_part_count))
print("Second Part: {} correct passwords found!".format(second_part_count))
