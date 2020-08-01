fruit = ['apple', 'orange', 'banana', 'peach']

print(fruit)

hate = input('\nWhat fruit do you hate in the above list? ')
prefer = input('What fruit do you prefer, that is not in the list? ')

if hate in fruit:
    hate_position = fruit.index(hate)  # 'index' stores the position of the 'hate' fruit in the 'fruit list
    fruit.insert(hate_position, prefer)  # 'insert' inserts the 'prefer' fruit into the position of the 'hate' fruit
    fruit.remove(hate)  # the 'hate' fruit is remove from the list
    print('\nHere\'s a better list!\n' + str(fruit))
