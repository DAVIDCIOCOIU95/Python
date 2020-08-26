# it is possible to have a list of tuples
albums = [("John Lennon", 1990),("Kimbra", 2006)]

for album in albums:
    print("Album: {}, Year: {}".format(album[0], album[1]))

# or
for name, year in albums:
    print("Album: {}, Year: {}".format(name, year))