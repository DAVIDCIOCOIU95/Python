import random

highest = 10
answer = random.randint(1, highest)
print(answer)
guess = 0

while guess != answer:
    guess = int(input())

    if guess == answer:
        print("You got it.")
        break
    else:
        print("Guess again.")

# -----------------------------------------
# i = 0
# while i < 10:
#     print("i is now: {}".format(i))
#     i += 1

# -----------------------------------------
# directions = ["north", "south", "east", "west"]
# chosen_exit = ""
# while chosen_exit not in directions:
#     chosen_exit = input("Please choose a direction: ").casefold()
#     if chosen_exit == "quit":
#         print("Game Over")
#         break
#
# print("You've exit with direction: {}".format(chosen_exit))
# -----------------------------------------
