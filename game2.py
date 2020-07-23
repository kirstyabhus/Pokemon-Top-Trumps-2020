import random


def flip_coin():
    random_number = random.randint(1, 2)

    if random_number == 1:
        side = "heads"
    elif random_number == 2:
        side = "tails"
    return side


def flip():
    choice = input("Heads or tails:")

    flip_coin()
    result = flip_coin()
    error1 = "heads" or "tails"

    if choice == result:
        print("The coin has landed on {}".format(result))
        print("You win!")
    elif choice != result and choice == error1:
        print("The coin has landed on {}".format(result))
        print("You lose!")
    elif choice != error1:
        print("Please choose either heads or tails.")
        print("\n")
        flip()


flip()
