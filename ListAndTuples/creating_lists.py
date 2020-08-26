empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# list concatenation
numbers = even + odd
print(numbers)

# return a list form a function
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# see how sorted will sort the sequence of chars, this will return a list of chars
digits = sorted("4346534")
print(digits)

# use a class initializer: this will create a list from any iterable
# this is used if you want to copy a list (remember that a list is a mutable type)
other_digits = list("54242345")
print(other_digits)
more_numbers = list(other_digits)
print(more_numbers)
# see how the lists are different
print(other_digits is more_numbers)

# see how the lists are the same
dublicate_digits = other_digits
print(dublicate_digits is other_digits)

# slice can also be used to duplicate lists
list_slice = numbers[:]
print(list_slice)

# use the copy method
list_slice = numbers.copy()
print(list_slice)

# is checks if two variables refer to the same list
# == equality checks if the lists contain the same values in the same order
