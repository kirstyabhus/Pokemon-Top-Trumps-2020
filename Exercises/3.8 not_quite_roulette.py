import random


# colour_picker() picks randomly between red and black
def colour_picker():
    random_number_colour = random.randint(1, 2)

    if random_number_colour == 1:
        colour = "red"
    else:
        colour = "black"

    return colour


# generates random number between 1 and 100
random_number = random.randint(1, 100)
# stores random colour (either black or red) from random colour picker
random_colour = colour_picker()

bet_amount = float(input("How much do you want to bet: £"))
chosen_colour = input("Choose a colour (red/black): ")
chosen_number = int(input("Choose a number between 1 and 100: "))
print("")

print("Random number = {}   Random colour = {}\n".format(random_number, random_colour))

total_amount = 0

# if both match, user wins 100 times the bet amount. their winning amount & total amount are output
if random_colour == chosen_colour and random_number == chosen_number:
    both = bet_amount * 100
    total_amount = total_amount + both
    print("The colour and number matches. \nYou have won £{}. You total is £{}\n".format(both, total_amount))


# if colour match, user keeps the amount that was bet. their winning amount & total amount are output
if random_colour == chosen_colour:
    colour_match = bet_amount
    total_amount = total_amount + colour_match
    print("The colour matches.\nYou keep the £{} that was bet. Your total is £{}\n".format(colour_match, total_amount))

# if number match, the user wins double the amount that was bet. their winning amount & total amount are output
if random_number == chosen_number:
    number_match = bet_amount * 2
    total_amount = total_amount + number_match
    print("The number matches. \nYou have won £{}. Your total is £{}\n".format(number_match, total_amount))

# if neither colour or number match the user wins 0. their winning amount of 0 is
if total_amount == 0:
    total_amount = total_amount + 0
    print("There were no matches. \nYou have won £0")
