nums = [2, 6, 45, 54, 765, 123, 876, 8, 8]

nums_sorted = sorted(nums)  # stores the sorted list in a variable

print(max(nums))  # prints biggest integer
print("")
print(min(nums))  # prints smallest integer
print("")
print(len(nums))  # prints the length of the list
print("")
print(sorted(nums))  # sorts the list from smallest to biggest
print("")
print(list(reversed(nums_sorted)))  # reverses the order of the list stored in the 'nums_sorted' variable
print("")
print(list(reversed(nums)))  # reverses the order of the list (without changing the order)

nums.append(6)  # 'append' adds a new value to the END of the list
print("")
print(nums)

nums.insert(4, 10)  # 'insert' inserts a value into a given position in a list
# first part of bracket is the position you want to insert a item
# second part of bracket is the item you want to insert into the given position

print(nums)

print("")
print("")

print(nums.index(6))  # 'index' prints the position of the item in the list

print(nums.count(8))  # 'count' prints the number of times an item occurs in a list

nums.remove(2)  # 'remove' removes the item from the list
print(nums)

print("")
print("methods learnt: max, min, len, sorted, list reversed, append, insert, index, count, remove")