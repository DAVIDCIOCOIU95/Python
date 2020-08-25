computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

del computer_parts[0:2]
print(computer_parts)

data = [4, 6, 7, 2, 54, 76, 324, 76, 23, 7]
print(data)
del data[4]
print(data)

min_valid = 100
max_valid = 200
# note how this does not produce the desired output
for index, value in enumerate(data):
    if (value < min_valid) or (value > max_valid):
        del data[index]
print(data)

# to achieve what we want to do then you could create an extra array and push to it
# keep in mind that you can't decrease the index, it won't work with enumerate


# deleting from a sorted list (assume we don't have memory to copy the list)
data = [4, 6, 7, 2, 54, 76, 324, 76, 23, 7,100,25,5432,543, 46, 130, 180, 184, 200]
data.sort()
print(data)
# process the low values
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop) # for debugging
del data[:stop] # note that we sorted the list first

# delete upper bound
start = 0
# work backwards from end to 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break
print(start) # for debugging
del data[start:]
print(data)
