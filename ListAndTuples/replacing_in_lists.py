computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

print(computer_parts)

# replacing by index
computer_parts[3] = "trackball"
print(computer_parts)

# slice and replace with an iterable
computer_parts[1:3] = computer_parts
print(computer_parts)

# beware when replacing by slicing with a string, the string is an iterable
# this will add each letter to the computer parts, it's not really what we'd like to achieve, use an index for that
computer_parts[5:] = "trackball"
print(computer_parts)
