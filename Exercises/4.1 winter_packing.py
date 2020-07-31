clothes = ["shorts", "shoes", "t-shirt"]

print(clothes[0])

if clothes[0] == "shorts":
    clothes[0] = "warm coat" # changes the value of position 0 in list
    print(clothes)  # prints whole list


# separate to exercise
numbers = [5, 3, 7, 2, 11, 1]

print(len(numbers))  # prints length of list
print(max(numbers))  # prints biggest value in list
print(min(numbers))  # prints smallest value in list

print(sorted(numbers))
print(list(reversed(numbers)))
