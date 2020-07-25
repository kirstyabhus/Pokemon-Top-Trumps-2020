# 'my_money' should be converted to integer so that it can be compared to boat_cost
my_money = int(input("How much money do you have?"))

# 'boat cost' is one variable and variables can not have spaces
# therefore it should be 'boat_cost' with an underscore
boat_cost = 20 + 5

# first if statement line should be my_money > boat_cost not my_money < boat_cost
# because to buy something you must have more than the amount needed not less
if my_money > boat_cost:
    print("You can afford the boat hire")
else:
    print("You cannot afford the boat hire")