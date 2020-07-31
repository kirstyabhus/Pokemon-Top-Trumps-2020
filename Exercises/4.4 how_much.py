costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost1 = 0

for cost in costs:  # for loop finds the total cost (sum)
    total_cost1 = total_cost1 + cost

print(total_cost1)

total_cost2 = sum(costs)  # total cost can easily be found using 'sum' function instead
print(total_cost2)
