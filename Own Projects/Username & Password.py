# try making "invalid ... " not print more than once
import re

user = input("Username: ")
password = input("Password: ")
print(" ")

# DONE username must be between 6-15 characters

if len(user) < 6:
    print("invalid username.")
    print("username must be between 6-15 characters")
    print(" ")
elif len(user) > 15:
    print("invalid username.")
    print("username must be between 6-15 characters")
    print(" ")

# NOT DONE username must start with uppercase english alphabet letter

user_first_letter = user[0]  # stores the first character of the username ([0] means first character)
is_ufl_upper = user_first_letter.isupper()  # 'isupper()' checks if value stored in 'user_first_letter' is uppercase

# checks if first character of username contains the english alphabet [a-zA-Z]
EN_alpha = re.search('[a-zA-Z]', user_first_letter)

if not is_ufl_upper or not EN_alpha:  # meaning if first character of user is not uppercase and english alphabet char
    print("invalid username.")
    print("username must start with uppercase english alphabet letter")
    print(" ")

# DONE password must be between 8-256 characters

if len(password) < 8:
    print("invalid password.")
    print("password must be between 6-15 characters")
    print(" ")
elif len(user) > 256:
    print("invalid password.")
    print("password must be between 6-15 characters")
    print(" ")

# DONE password and username can not have any types of parentheses or white spaces.
# putting a bracket around all the 'or' is very important here

if " " in user:
    print("invalid username.")
    print("Username must not contain whitespaces.")
    print(" ")

if " " in password:
    print("invalid password.")
    print("Password must not contain whitespaces.")
    print(" ")

if ("(" or ")" or "{" or "}" or "]" or "[") in user:
    print("invalid username.")
    print("Username must not contain parentheses.")
    print(" ")

if ("(" or ")" or "{" or "}" or "]" or "[") in password:
    print("invalid password.")
    print("Password must not contain parentheses.")
    print(" ")

# DONE password cannot contain or be the same as the username

if user in password:
    print("invalid password")
    print("password cannot contain or be the same as the username.")
    print(" ")
