# There is only a list. A list contains objects. If one of those objects happens to be another list, apply the exact same indexing rule to that list. Repeat as many times as necessary.

# x = [[0] * 3] * 3

# print(id(x[0]))
# print(id(x[1]))
# print(id(x[2]))

x = [1, 2, 3, 4, 5]

x[0] = 10

x = [[[1, 2], [3, 4]], ["h", "o"]]

print(x[0][0][0])