empty_lists = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
# this will produce a list of lists
numbers = [even , odd]
print(numbers)

# printing contents of the inner lists
for number_list in numbers:
    print(number_list)
    for value in number_list:
        print(value)