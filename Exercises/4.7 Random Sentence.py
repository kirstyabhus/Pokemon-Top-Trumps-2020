import random

first_name = ["Kirsty", "Chantel", "Jade", "Jordan"]
last_name = ["Fernandez", "Malik", "Scott", "Smith"]

verb = ["plays", "breaks", "eats"]

noun = ["piano", "saxophone", "basketball"]

chosen_first = random.choice(first_name)
chosen_last = random.choice(last_name)
cverb = random.choice(verb)
cnoun = random.choice(noun)

print("{} {} {} the {}".format(chosen_first, chosen_last, cverb, cnoun))