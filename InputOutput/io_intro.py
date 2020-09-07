# jabber = open("C:\\Users\david\\Desktop\\sample.txt", "r")
jabber = open("sample.txt", "r")
print(id(jabber))

for line in jabber:
    if "jabberwock" in line.lower():
        print(line,
              end="")  # we printing empty at the end as each line ends with \n and print will print a \n (so double \n)
    # print(line)

jabber.close()

with open("sample.txt", "r") as jabber:
    print(id(jabber))
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end="")

with open("sample.txt", "r") as jabber:
    line = jabber.readline()
    # enters the while loop if there is something on the line being read
    print("line: " + line)
    while line:
        print(line, end="")
        line = jabber.readline()

with open("sample.txt", "r") as jabber:
    lines = jabber.readlines()
    print(lines)
    for line in lines:
        print(line, end="")

with open("sample.txt", "r") as jabber:
    # read all the file as a string
    lines = jabber.read()
    print(lines, end="")



