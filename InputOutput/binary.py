# with open("binary", "bw") as bin_file:
#     # for i in range(17):
#     #     bin_file.write(bytes([i]))
#
#     # actual implementation
#     bin_file.write(bytes(range(17)))
#
#
# with open("binary", "br") as binFile:
#     for b in binFile:
#         print(b)


a = 65534  # FF FE
b = 65535
c = 65536
x = 2998302

# built in int methods for bin conversion
with open("binary2", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, "big"))
    bin_file.write(b.to_bytes(2, "big"))
    bin_file.write(c.to_bytes(4, "big")) # as we increase the number we need more bytes to store the number
    bin_file.write(x.to_bytes(4, "big"))
    bin_file.write(x.to_bytes(4, "little"))

with open("binary2", "br") as bin_file:
    e = int.from_bytes(bin_file.read(2), "big")
    print(e)
    f = int.from_bytes(bin_file.read(2), "big")
    print(f)
    g = int.from_bytes(bin_file.read(4), "big")
    print(g)
    h = int.from_bytes(bin_file.read(4), "big")
    print(h)
    i = int.from_bytes(bin_file.read(4), "big") # this will return something else (the bites will be in reverse order)
    print(i)