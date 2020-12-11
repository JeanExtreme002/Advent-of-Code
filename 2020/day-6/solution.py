def get_chars(from_ = "a", to = "z"):

    """
    Return a list of characters.
    """

    return [chr(i) for i in range(ord(from_), ord(to) + 1)]

def get_answers_count(group):

    """
    Return the number of answers for each question (a-z).
    """

    answers_count = []

    for char in get_chars():

        # Get the number of times the character appears in the string.
        answers_count.append(group.count(char))

    # Return answers count.
    return answers_count

def get_people_count(group):

    """
    Return the number of people in a group.
    """

    # Separate people from the group.
    people = group.split("\n")
    if "" in people: people.remove("")

    # Return people count.
    return len(people)

def get_questions_count(group):

    """
    Return the number of questions answered.
    """

    questions_count = 0

    for char in get_chars():

        # Check whether the character is in the string.
        if char in group: questions_count += 1

    # Return questions count.
    return questions_count

# Get data from file.
with open("input.txt") as file:
    data = file.read().split("\n\n")

first_part_count = 0
second_part_count = 0

# Get questions count from each group.
for group in data:

    # Get answers count for each question.
    answers_count = get_answers_count(group)

    # Get people count.
    people_count = get_people_count(group)

    # Compute the number of questions answered.
    first_part_count += get_questions_count(group)

    # Compute the number of questions that everyone answered.
    for number in answers_count:
        if number == people_count: second_part_count += 1

# Show the results.
print("First Part: The sum of questions answered is {}.".format(first_part_count))
print("Second Part: The sum of questions that everyone answered is {}.".format(second_part_count))
