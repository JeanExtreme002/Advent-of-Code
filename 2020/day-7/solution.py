def get_bag_colors_count(rules, content_colors, all_found = []):

    """
    Return the number of bag colors available for contents in the given colors.
    """

    found = []

    for content_color in content_colors:

        # Check each bag color rule.
        for rule in rules:
            color, content = split_rule(rule)

            # Check whether the bag can contain a bag in the given color.
            if content_color in content and not color in all_found + found:

                # Add color to the list.
                found.append(color)
                all_found.append(color)

    # If there were results, the function will be called again, passing the results as an argument.
    return len(found) + (get_bag_colors_count(rules, found, all_found) if found else 0)

def get_individual_bag_count(rules, bag_color):

    """
    Return the number of individual bags inside a bag.
    """

    bags = []

    # Check each bag color rule.
    for rule in rules:
        color, content = split_rule(rule)

        # Check if the color is correct and get the contents of the bag.
        if bag_color in color:
            bags += split_content(content)
            break

    # Multiply the amount of content by the number of bags of a type of color and return the sum of all bags.
    # Calculation: For each bag found -> n(bag) + n(bag) * n(content).
    return sum([bag[0] + bag[0] * get_individual_bag_count(rules, bag[1]) for bag in bags]) if bags else 0

def split_content(content):

    """
    Split the rule into a list of bags.
    """

    bags = []

    # Return an empty list if there is no content.
    if "no other" in content: return bags

    # Separate each type of bag.
    for bag in content.replace("bags", "").replace("bag", "").split(","):

        # Separate the number of bags and the color.
        n, color = bag.strip().split(maxsplit = 1)
        bags.append([int(n), color])

    return bags

def split_rule(rule):

    """
    Split a rule in color and content.
    """

    color, content = rule.replace(".", "").split("contain")
    color = color.replace("bags", "").replace("bag", "").strip()

    return color, content

# Get data from file.
with open("input.txt") as file:
    data = file.readlines()

search = "shiny gold"

# Get the number of outermost bag colors and individual bags that can be inside the main bag.
first_part_count = get_bag_colors_count(data, [search])
second_part_count = get_individual_bag_count(data, search)

# Show the results.
print("First Part: {} bag colors are available.".format(first_part_count))
print("Second Part: {} bags can be inside the main bag.".format(second_part_count))
