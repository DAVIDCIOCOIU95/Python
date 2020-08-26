from ListAndTuples.final_challenge.nested_data_challenge import albums

# convention for constants is to capitalize the var name note that the compiler doesn't spot this difference,
# hence you can reassign a const value as there is no const concept in python
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1  # note that 0 is the number and 1 is the title
while True:
    print("Choose your album:")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {} "
              .format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]  # get the songs list inside the tuple
    else:
        continue

    print("Please choose your song: ")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))
    song_choice = int(input())
    if 1 <= choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))
    else:
        continue

    print("="*40)