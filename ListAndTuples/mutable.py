shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

# mutate the list:note that the ids remain unchanged
shopping_list += ["cookies"]
print(shopping_list)
print("Added a new object to original list")
print(id(shopping_list))
print(id(another_list))

# how many lists are there in the program? There is only One list.
