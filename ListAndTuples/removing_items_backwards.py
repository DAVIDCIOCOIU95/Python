# the size of the sequence can be changed without creating a problem when iterating backwards
data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

# the data is not sorted here
for index in range(len(data) - 1, -1, -1):
    if data[index] < min_valid or data[index] > max_valid:
        print(index)
        del data[index]

# what happens above is that the list shuffles down from the right hand, although we continue into the left hand side
# this means that the data we are working on won't be affected

# reversed function: used to iterate backwards
print("Using reversed\n")
data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        # note how we get the original index in order to remove from the original data list
        del data[top_index - index]

# using enumerate is faster than using index lookup with the first method, but only with big data
# obviously if an item is deleted an item needs to be shuffled down, so it will take longer
# deleting a range in one go is more efficient, but you need to know if the data is sorted or not.