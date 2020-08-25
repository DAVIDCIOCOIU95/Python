# the sorted function is used to sort things other than lists
# you can sort any iterable object
# it produces a list

# use the below pangram which contains all the latter of the alphabet at least once
pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
# this will be case insensitive
# letters = sorted(pangram, key=str.casefold)
print(letters)

# it is also possible to sort numbers
# here you will get a different list back, note that sort takes the list as argument
# whereas sort is called upon a list: it won't return anything
numbers = [2.3, 5.6, 3.5, 6.2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)


# case insensitive sorting
names = ["Graham", "John", "terry", "eric"]
# be careful not to call the function but just to pass it as an argument to the method
names.sort(key=str.casefold)
print(numbers)