cats = 10
cans_each_day = 3

total_cans = cats * cans_each_day
days = 7

total_for_amount_of_days = days * total_cans

print("To feed {} cats {} cans each day, you will need a total of {} cans.".format(cats, cans_each_day, total_cans))
print("The total number of cans for {} days is {}".format(days, total_for_amount_of_days))
print("\n")

print(f"{cats} cats eat {cans_each_day} cans each day, making a total of {total_cans}")

print("To feed " + str(cats) + " cats" + str(cans_each_day) + " cans each day, you will need a total of" + str(total_cans) + " cans")