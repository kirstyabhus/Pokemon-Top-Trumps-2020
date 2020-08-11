import csv

with open("trees.csv", "r") as trees_file:
    spreadsheet = csv.DictReader(trees_file)

    heights = []

    for row in spreadsheet:
        tree_height = row["height"]
        heights.append(tree_height)

shortest_height = min(heights)
print(shortest_height)
