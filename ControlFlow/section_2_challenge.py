# options = ["1-Learn Python", "2-Revise Python", "3-Exercise", "4-Chill-out", "5-Sleep", "0-Quit"]
#
# while True:
#     for choice in options:
#         print(choice)
#     command = int(input("Enter your choice number: "))
#     if not (command >= 1 and command <= (len(options) - 2)):
#         print("Invalid option")
#     elif command == 0:
#         print("Exiting...")
#     else:
#         print("You made a valid choice choosing: {}".format(command))

choice = "-"
while choice != "0":
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below")
        print("1")
        print("2")
        print("3")
        print("4")
        print("5")
        print("0: exit")
    choice = input()