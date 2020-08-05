chocolates = {'white': 1.50, 'milk': 1.20, 'dark': 1.80, 'vegan': 2.00,}

buy = input("What item would you like to buy?")
print(" ")

price = chocolates[buy]

print(" ")
print("The price is £{}".format(price))