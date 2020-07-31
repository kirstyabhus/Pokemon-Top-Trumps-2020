scores = [40, 15, 143, 200, 3, 76, 90, 176, 89, 25]

score_order = sorted(scores) # sorts the scores from smallest to biggest
score_order_reversed = list(reversed(score_order)) # reverses the order of the sorted list


print("Number of scores: {}".format(len(scores)))
print("Highest score: {}".format(max(scores)))
print("Lowest score: {}".format(min(scores)))

print("Scores in descending order: {}".format(score_order_reversed))

