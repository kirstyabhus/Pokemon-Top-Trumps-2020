for i in range(1, 4):
    with open('rounds.txt', 'a') as rounds_file:
        rounds_file.write('Round {}\n'.format(i))  # reads the contents of the file
