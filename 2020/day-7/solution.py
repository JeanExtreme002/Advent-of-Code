def get_outermost_bag_colors(rules, content_colors, found = set()):

    """
    Return the available outermost bag colors for the given bag colors.
    """

    bag_colors = set()

    for content_color in content_colors:

        # Check each bag color rule and divide it (color | content).
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

# Get data from file.
with open("input.txt") as file:
    data = file.readlines()

search = ["shiny gold"]

# Get bag colors.
bag_colors = get_outermost_bag_colors(data, search)

# Show the results.
print("First Part: {} bag colors are available.".format(len(bag_colors)))
