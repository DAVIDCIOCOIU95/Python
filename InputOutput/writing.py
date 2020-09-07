cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sidney"]

# with open("cities.txt", "w") as city_file:
#     for city in cities:
#         print(city, file=city_file)  # file indicates we want to write the content to a txt file
#

# we are reading back the data
# with open("cities.txt", "r") as city_file:
#     for city in city_file:
#         cities.append(city.strip("\n"))  # remove the trailing char newline otherwise appended to the word in the list
#
# print(cities)
# for city in cities:
#     print(city)

#use eval
# imelda = "More Mayhem", "Imelda MAy", "2011", ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# with open("imelda3.txt", "w") as imelda_file:
#     print(imelda, file=imelda_file)

with open("imelda3.txt", "r") as imelda_file:
    contents = imelda_file.readline()
imelda = eval(contents)
print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)