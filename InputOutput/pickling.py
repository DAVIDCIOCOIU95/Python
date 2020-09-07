import pickle

imelda = ("More Mayehm",
          "IMelda May",
          "2011",
          ((1, "Pulling the rug"),
           (2, "psycho"),
           (3, "Mayhem"),
           (4, "Kenthish Town Waltz")))

# # write
# with open("imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda, pickle_file)
#

# read
# with open("imelda.pickle", "rb") as imelda_pickled:
#     imelda2 = pickle.load(imelda_pickled)
#
# print(imelda2)
# album, artist, year, track_list = imelda2
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)

# once u open a file u can keep writing to it
imelda = ("More Mayehm",
          "IMelda May",
          "2011",
          ((1, "Pulling the rug"),
           (2, "psycho"),
           (3, "Mayhem"),
           (4, "Kenthish Town Waltz")))
even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))
with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)
    pickle.dump(299282, pickle_file)

with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)

print(imelda2)
album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

print("=" * 40)
for i in even_list:
    print(i)
print("=" * 40)

for i in odd_list:
    print(i)
print("=" * 40)

print(x)
