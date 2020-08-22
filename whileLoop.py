i = 0
while i < 10:
    print("i is now: {}".format(i))
    i += 1

directions = ["north", "south", "east", "west"]
chosen_exit = ""
while chosen_exit not in directions:
    chosen_exit = input("Please choose a direction: ")

print("You've exit")