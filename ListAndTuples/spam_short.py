# notice below how formatting is recommended for lists
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
]

# print only lists which don't contain spam
for meal in menu:
    if "spam" not in meal:
        print(meal)
    else:
        print("{0} has a spam score of {1}".format(meal, meal.count("spam")))
