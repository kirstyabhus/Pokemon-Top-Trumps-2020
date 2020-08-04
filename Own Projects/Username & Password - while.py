import re

user = input("Username: ")
password = input("Password: ")
print(" ")

user_first_letter = user[0]  # stores the first character of the username ([0] means first character)
is_ufl_upper = user_first_letter.isupper()  # 'isupper()' checks if value stored in 'user_first_letter' is uppercase

# checks if first character of username contains the english alphabet [a-zA-Z]
EN_alpha = re.search('[a-zA-Z]', user_first_letter)

u1 = 0

# this 'while' checks & outputs whether the username is valid
while True:
    if len(user) < 6:  # min length must be 6
        u1 = -1
        break
    elif len(user) > 15:  # max length must be 15
        u1 = -1
        break
    elif not is_ufl_upper or not EN_alpha:  # first character must be upper case and english character
        u1 = -1
        break
    elif " " in user:  # no spaces
        u1 = -1
        break
    elif ("(" or ")" or "{" or "}" or "]" or "[") in user:  # no parentheses
        u1 = -1
        break
    else:
        u1 = 0
        print("Valid Username")
        break
if u1 == -1:
    print("Invalid Username")

u2 = 0

# this 'while' outputs the reason why the username is invalid
while True:
    if len(user) < 6:
        u2 = -1
        print("Username must be between 6-15 characters")
        break
    elif len(user) > 15:
        u2 = -1
        print("Username must be between 6-15 characters")
        break
    elif not is_ufl_upper or not EN_alpha:
        u2 = -1
        print("Username must start with uppercase english alphabet letter")
        break
    elif " " in user:
        u2 = -1
        print("Username must not contain whitespaces.")
        break
    elif ("(" or ")" or "{" or "}" or "]" or "[") in user:
        u2 = -1
        print("Username must not contain parentheses.")
        break
    else:
        u1 = 0
        break

print(" ")


p1 = 0

# this 'while' checks & outputs whether the password is valid
while True:
    if len(password) < 8:  # min length must be 8
        p1 = -1
        break
    elif len(password) > 256:  # max length must be 256
        p1 = -1
        break
    elif " " in password:  # no spaces
        p1 = -1
        break
    elif ("(" or ")" or "{" or "}" or "]" or "[") in password:  # no parentheses
        p1 = -1
        break
    elif user in password:
        p1 = -1
        break
    else:
        p1 = 0
        print("Valid Password")
        break
if p1 == -1:
    print("Invalid Password")


p2 = 0

# this 'while' outputs the reason why the password is invalid
while True:
    if len(password) < 8:  # min length must be 6
        p2 = -1
        print("Password must be between 8-256 characters")
        break
    elif len(password) > 256:  # max length must be 15
        p2 = -1
        print("Password must be between 8-256 characters")
        break
    elif " " in password:  # no spaces
        p2 = -1
        print("Password must not contain whitespaces.")
        break
    elif ("(" or ")" or "{" or "}" or "]" or "[") in password:  # no parentheses
        p2 = -1
        print("Username must not contain parentheses.")
        break
    elif user in password:
        p2 = -1
        print("password cannot contain or be the same as the username.")
        break
    else:
        p2 = 0
        break
