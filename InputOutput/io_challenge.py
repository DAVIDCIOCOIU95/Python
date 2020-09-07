with open("times.txt", "w") as sample_file:
    for x in range(2, 13):
        for y in range(1, 13):
            z = y*x
            print("{0:>2} times {1} is {2}".format(y, x, z), file=sample_file)
        print("\n", file=sample_file)

