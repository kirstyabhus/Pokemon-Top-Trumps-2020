book_year = int(input("What year was the book written in?\n"))

if book_year == 1800:
    century = "Eighteenth Century"
elif 1900 >= book_year >= 1801:
    century = "Nineteenth Century"
elif 1900 < book_year <= 1950:
    century = "Twentieth Century"

if book_year < 190


print("{},{}".format(century, decade))