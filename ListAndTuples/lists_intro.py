# computer_parts = ["computer",
#                   "monitor",
#                   "keyboard",
#                   "mouse",
#                   "mouse mat"
#                   ]
#
# for part in computer_parts:
#     print(part)
#
# # access the list by index
# print(computer_parts[2])
#
# # we can slice a list
# print(computer_parts[0:3])
# print(computer_parts[-1])

# strings are immutable objects: see why
myString1 = "hello"
myCopyString = myString1

print(myString1)
print(id(myString1))
print(myCopyString)
print(id(myCopyString))

myString1 += " world"
print("After change")
print(myString1)
print(id(myString1))
print(myCopyString)
print(id(myCopyString))

