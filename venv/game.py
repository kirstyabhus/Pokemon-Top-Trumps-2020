import random
#random_integer = random.randint(1, 100)
#print(random_integer)

# rolls a die sing number of sides given
#sides = int(input("How many sides does the die have?"))
#random_integer = random.randint(1, sides)
#print("You rolled a {}".format(random_integer))

def flip_coin():
    random_number = random.randint(1,2)

    if random_number == 1:
        side = "heads"
    elif random_number == 2:
        side = "tails"
    return side

def flip():
    choice = input("Heads or tails:")

    flip_coin()
    result = flip_coin()

    if choice != "heads" or "tails":
        print("Please choose either heads or tails. \n")
        flip()
    elif choice == result:
        print("The coin has landed on {}".format(result))
        print("You win!")
    elif choice != result and choice == "heads" or "tails":
        print("The coin has landed on {}".format(result))
        print("You lose!")


flip()