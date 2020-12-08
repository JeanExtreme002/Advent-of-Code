def get_outermost_bag_colors(rules, content_colors, found = set()):

    """
    Return the colors of bags available for content in the given colors.
    """

    bag_colors = set()

    for content_color in content_colors:

        # Check each bag color rule.
        for rule in rules:
            color, content = rule.split("contain")

            # Check whether the bag can contain a bag in the given color.
            if content_color in content and not color in found:
                bag_colors.add(color.replace("bags", "").strip())

    # If there are more results, the function will be called again, passing the results as an argument.
    if bag_colors.difference(found):
        found.update(bag_colors)
        return bag_colors.union(get_outermost_bag_colors(rules, bag_colors, found))

    # Return an empty Set if there are no more results.
    else: return set()

def get_bag_content_count(rules, bag_colors):

    bags = []

    for bag_color in bag_colors:

        # Check each bag color rule.
        for rule in rules:
            color, content = rule.replace(".", "").split("contain")

            # If the bag color is the same, the contents it can contain
            # will be unpacked in a list of bags.
            if bag_color in color:
                content = unpack_content(content)
                bags.extend(content)

    # If there were results, the function will be called again, passing the results as an argument.
    return [] if not bags else bags + get_bag_content_count(rules, bags)

def unpack_content(content):

    """
    Unpack the content into a list of bags.
    """

    bags = []

    # Separate each item into a list.
    content = content.replace("bags", "").split(",")
    content = list(map(lambda s: s.strip().split(maxsplit = 1), content))

    # Unpack the items.
    for bag in content:
        if not "no" in bag[0]: bags += [bag[1].replace("bags", "")] * int(bag[0])

    # Return list of bags.
    return bags

# Get data from file.
with open("input.txt") as file:
    data = file.readlines()

search = ["shiny gold"]

# Get the number of outermost bag colors and individual bags that can be inside the main bag.
first_part_count = len(get_outermost_bag_colors(data, search))
second_part_count = len(get_bag_content_count(data, search))

# Show the results.
print("First Part: {} bag colors are available.".format(first_part_count))
print("Second Part: {} bags can be inside the main bag.".format(second_part_count))
