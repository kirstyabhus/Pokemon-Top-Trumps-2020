def calculate_vat(amount):
    return amount * 1.2

# our function is expected to output something
# without the return statement, the function will return an object 'None'
# therefore, a return statement is added above to return a value

total = calculate_vat(100)
print(total)