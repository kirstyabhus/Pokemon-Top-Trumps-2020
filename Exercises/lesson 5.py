new_item = input("Enter a to-do item: ")  # asks the user for an input

with open("todo.txt", 'r') as todo_file:  # 'r' to read the txt file bc it has already been made
    list = todo_file.read()  # reads the contents of the file

list = list + new_item + "\n"  # adds new_item to list with a new line

with open("todo.txt", "w+") as todo_file:  # opens the file with the intention to write
    todo_file.write(list)  # adds the 'list' to the file
