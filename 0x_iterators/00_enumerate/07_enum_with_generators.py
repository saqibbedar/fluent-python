# Enumerator with Generators: in python generators are special type of iterators that produce one value at a time, on demand, instead of generating and storing all values in memory at once.

# They are useful when working with large datasets, streams of data, or sequences that could be infinite.

def square():
    for i in range(5):
        yield i*i

for idx, value in enumerate(square()):
    print(idx, value)

"""
0 0
1 1
2 4
3 9
4 16
"""

# No extra memory is used to store all values.