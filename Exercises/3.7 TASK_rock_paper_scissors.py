
import random


def random_choice():
    choice_number = random.randint(1, 3)

    if choice_number == 1:
        choice = "rock"
    elif choice_number == 2:
        choice = "paper"
    else:
        choice = "scissors"

    return choice


def game():

    my_choice = input("Choose rock, paper or scissors: ")
    opponent_choice = random_choice()

    if my_choice == "rock" and opponent_choice == "scissors":
        print("Your opponent chose {}".format(opponent_choice))
        print("You win!")
    elif my_choice == "rock" and opponent_choice == "paper":
        print("Your opponent chose {}".format(opponent_choice))
        print("You lose!")
    elif my_choice == "scissors" and opponent_choice == "rock":
        print("Your opponent chose {}".format(opponent_choice))
        print("You lose!")
    elif my_choice == "scissors" and opponent_choice == "paper":
        print("Your opponent chose {}".format(opponent_choice))
        print("You win!")
    elif my_choice == "paper" and opponent_choice == "scissors":
        print("Your opponent chose {}".format(opponent_choice))
        print("You lose!")
    elif my_choice == "paper" and opponent_choice == "rock":
        print("Your opponent chose {}".format(opponent_choice))
        print("You win!")
    elif my_choice == "rock" and opponent_choice == "rock":
        print("Your opponent chose {}".format(opponent_choice))
        print("It's a tie.\n")
        game()
    elif my_choice == "paper" and opponent_choice == "paper":
        print("Your opponent chose {}".format(opponent_choice))
        print("It's a tie.\n")
        game()
    elif my_choice == "scissors" and opponent_choice == "scissors":
        print("Your opponent chose {}".format(opponent_choice))
        print("It's a tie.\n")
        game()
    elif my_choice != "scissors" and my_choice != "paper" and my_choice != "rock":
        print("Please input a choice that is either rock, paper, or scissors.\n")
        game()


game()

