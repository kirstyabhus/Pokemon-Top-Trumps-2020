book_year = int(input("What year was the book written in?\n"))

if book_year == 1800:
    print("Eighteenth Century")

if 1900 >= book_year >= 1801:
    print("Nineteenth Century")

if 1900 < book_year <= 1950:
    print("Twentieth Century")

if book_year