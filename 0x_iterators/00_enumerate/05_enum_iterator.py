# Enumerate object is an iterator

e = enumerate(["a", "b", "c"])

print(next(e))
print(next(e))
print(next(e))

"""
Output:
(0, 'a')
(1, 'b')
(2, 'c')
"""

# print(next(e))        # Error: raises StopIteration