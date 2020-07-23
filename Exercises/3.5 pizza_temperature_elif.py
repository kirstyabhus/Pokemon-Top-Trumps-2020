temperature = float(input("What is the temperature of the oven?"))

if temperature > 200:
    print("The oven is too hot")
elif temperature < 150:
    print("The oven is too cold")
elif temperature == 180:
    print("The oven is at the perfect temperature")
else:
    print("The temperature is close enough")