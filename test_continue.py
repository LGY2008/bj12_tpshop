# row = 1
# while row <= 5:
#     print("*" * row)
#     row += 1

# print("*", end="")
# print("*")

row = 1
while row <= 9:
    col = 1
    while col <= row:
        # print("*", end="")
        print("%d * %d = %d" % (col, row, row * col), end="\t")
        col += 1
    print("")
    row += 1
