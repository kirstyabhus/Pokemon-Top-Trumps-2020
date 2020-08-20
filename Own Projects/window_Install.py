# asks user for dimensions of window
width = float(input("What is the width of the window: \n"))
height = float(input("What is the height of the window: \n"))

area = width * height
perimeter = width + width + height + height

if width < 0.5 or width > 3.5:
    print("Window width must be between 0.5m and 3.5m")

if height < 0.5 or height > 2.0:
    print("Window height must be between 0.5m and 2.0m")

feet = perimeter * 3.25  # converts the meters of wood into feet

# conversion of decimal feet to feet and inches
feet_first = int(feet)  # takes the numbers before the decimal point of the feet calulated before

inch_fraction = feet - feet_first  # finds the numbers after the decimal point

inches = int(12 * inch_fraction)  # converts the numbers after decimal point into inches

# decimal feet to feet and inches test
# print(feet)
# print(inches)


# changes float to 2 decimal places
# "{:12.2f}".format(x)

# calculates whole number figure of glass needed
# glass_amount = int(area)
# if area > int(area):
# glass_amount = glass_amount + 1

if inches != 0:
    print("You will need {} meters squared of glass and {} feet {} inches of wood.".format(area, feet_first, inches))

if inches == 0:
    print("You will need {} meters squared of glass and {} feet of wood.".format(area, feet_first))




