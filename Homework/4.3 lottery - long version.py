import random

picked = []

p1 = int(input("First number: "))
p2 = int(input("Second number: "))
p3 = int(input("Third number: "))
p4 = int(input("Fourth number: "))
p5 = int(input("Fifth number: "))
p6 = int(input("Sixth number: "))
p7 = int(input("Seventh number: "))

picked.append(p1)
picked.append(p2)
picked.append(p3)
picked.append(p4)
picked.append(p5)
picked.append(p6)
picked.append(p7)

lottery = []

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ]

r1 = random.choice(numbers)
r2 = random.choice(numbers)
r3 = random.choice(numbers)
r4 = random.choice(numbers)
r5 = random.choice(numbers)
r6 = random.choice(numbers)
r7 = random.choice(numbers)

# can for loop be used instead???
lottery.append(r1)
lottery.append(r2)
lottery.append(r3)
lottery.append(r4)
lottery.append(r5)
lottery.append(r6)
lottery.append(r7)

match = 0

if picked[0] in lottery:
    match = match + 1

if picked[1] in lottery:
    match = match + 1

if picked[2] in lottery:
    match = match + 1

if picked[3] in lottery:
    match = match + 1

if picked[4] in lottery:
    match = match + 1

if picked[5] in lottery:
    match = match + 1

if picked[6] in lottery:
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
