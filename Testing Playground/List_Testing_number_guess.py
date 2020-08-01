
numbers = [1, 2, 3, 4, 5, 6, 7]
guess = int(input('what number do you think is in the list?\n'))

if guess in numbers:
    print("You are right!")
else:
    print("You are wrong!")

print(guess in numbers)