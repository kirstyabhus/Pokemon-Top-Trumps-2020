friends = []  # an empty list

f1 = input('name a friend: ')
f2 = input('name a friend: ')
f3 = input('name a friend: ')
f4 = input('name a friend: ')

friends.append(f1)  # adds to list
friends.append(f2)
friends.append(f3)
friends.append(f4)

print("")
print(friends)
print("")

no_like = input('which friend from the list do you like the least: ')
friends.remove(no_like)
print(friends)
