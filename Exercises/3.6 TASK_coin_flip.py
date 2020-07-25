import random


# flip_coin generates random number between 1 & 2, labelling them heads or tails
def flip_coin():
    random_number = random.randint(1, 2)

    if random_number == 1:
        side = "heads"
    elif random_number == 2:
        side = "tails"
    return side


def flip():

    choice = input("Heads or tails: ")

    flip_coin()
    result = flip_coin()

    if choice != result and choice != "tails" and choice != "heads":
        print("Please choose either heads or tails.")
        print("\n")
        flip()
    elif choice == result:
        print("The coin has landed on {}".format(result))
        print("You win!")
    elif choice != result:
        print("The coin has landed on {}".format(result))
        print("You lose!")


flip()
