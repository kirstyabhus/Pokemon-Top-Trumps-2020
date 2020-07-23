#price = float(input("What is the price of a burger?"))

#if price <= 10.00:
#    print("Burger is within budget: True")

price = input("What is the price of a burger?")

within_budget = float((price)) <= 10.00

vegetarian = input("is there a vegetarian option? (y/n)")

is_vegetarian = vegetarian == "y"

if within_budget and is_vegetarian == True:
#print("Burger is within budget: {}\nRestaurant is vegetarian: {}".format(within_budget, is_vegetarian))
    print("This restaurant is a good choice.")

if not within_budget and not is_vegetarian:
    print("This restaurant is not a good choice.")

meal_price = float(input("How much did the meal cost?"))

discount_choice = input("Do you have a discount? y/n")
discount_applicable = discount_choice == "y"

if discount_applicable and meal_price >= 20.00:
    meal_price = meal_price * 0.9
    print("Discount applied.")
else:
    print("No discount applied.")

print("Total cost: {}".format(meal_price))