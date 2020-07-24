import random


def colour():
    random_number = random.randint(1, 2)

    if random_number == 1:
        colour = "red"
    else:
        colour = "black"

    return colour


random_number = random.randint(1, 100)
random_colour = colour()

bet_amount = float(input("How much do you want to bet: "))
chosen_colour = input("Choose a colour (red/black): ")
chosen_number = input("Choose a number between 1 and 100: ")

total_amount = bet_amount

if random_colour == chosen_colour:
    total_amount = total_amount
    print(total_amount)

if random_number == chosen_number:
    total_amount == total_amount * 2
    print(total_amount)

if random_colour == chosen_colour and random_number == chosen_number:
    total_amount = total_amount * 100
    print(total_amount)

print(total_amount)
