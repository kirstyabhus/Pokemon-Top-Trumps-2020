import random

picked = []  # empty list for the users' 7 inputs

for x in range(7):  # asks the user for a number 7 times and adds the numbers to the 'picked' list
    number = int(input("Number: "))
    picked.append(number)

lottery = []  # empty list for the 7 random numbers, that will be picked from 'numbers' list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ]

for y in range(7):  # picks 7 random numbers from 'numbers' list then adds into 'lottery' list
    random_num = random.choice(numbers)
    if random_num in lottery:
        random_num = random.choice(numbers)

    lottery.append(random_num)  # adds randomly picked number into lottery list

match = 0  # will be used to count the number of matches in picked and lottery list

for z in range(7):
    if picked[z] in lottery:
        match = match + 1

print("\nLottery numbers: {} \nYour numbers: {}\n".format(lottery, picked))

if match == 3:
    print("3 matches! \nPrize = £20")
elif match == 4:
    print("4 matches! \nPrize = £40")
elif match == 5:
    print("5 matches! \nPrize = £100")
elif match == 6:
    print("6 matches! \nPrize = £10000")
elif match == 7:
    print("7 matches! \nPrize = £1000000")
