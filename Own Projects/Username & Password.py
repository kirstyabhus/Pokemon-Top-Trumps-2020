user = input("Username: ")
password = input("Password: ")

if len(user) < 6:
    print("invalid username.")
    print("username is too short.")

if len(user) > 15:
    print("invalid username.")
    print("username is too long.")