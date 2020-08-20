# with open("todo_list.txt", "w") as todo: "w" is write creates a new file/  overwrites the same file

with open("todo_list.txt", "a") as todo:  # "a" is append which means dding to whats been created
    new = input("What do you need to do today?: ")
    todo.write(new + "\n")
    todo.close()

with open("todo_list.txt", "r") as todo:  # "r" is read which opens a file
    print(todo.read())
    # OR
    # contents = todo.read()
    # print(contents)
