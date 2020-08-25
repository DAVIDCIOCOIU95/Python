even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print(even)
# we need to sort even now, the sort is done in place
even.sort()
print("Even")
print(even)

another_even = even
print("Another Even")
print(another_even)

# See below how the other list bound to the firs list changes as well when we change the first list
even.sort(reverse=True)
print("After reverse")
print("Even")
print(even)
print(id(even))
print("Another Even")
print(another_even)
print(id(another_even))
if id(even) == id(another_even):
    print("The two lists have the same id.")


