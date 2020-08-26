t = "a", "b", "c"
print(t)

# or

y = ("l", "h", "m")
print(t, y, 2020, "Python")
# if you want to pass directly a tuple you have to use pars.
print((t, y, 2020, "Python"))

# you can index tuples of course
print(t[0])

# if you try to assign an item it will throw an error as tuples are immutable
print(id(t))
t = y
print(id(t))

# you can use tuple and list class constructors
list2 = list(t)

# unpacking
x, y, z = 1, 2, 3
print(x, y, z)

data_list = [1, 3, 5]
p, q, r = data_list
print(p, q, r)

# enumerate and unpacking
for t in enumerate("abfdass"):
    print(t)
# note that the above code will put index and value of each iteration in t which is tuple
# unpack
for t in enumerate("abfdass"):
    index, value = t
    print(index, value)