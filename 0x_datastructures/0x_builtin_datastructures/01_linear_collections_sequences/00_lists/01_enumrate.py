numList = [10, 20, 30]

print(f"{" Tuples ".center(36, "=")}")
for num in enumerate(numList):
    print(num)

# output: tuple
"""
============== Tuples ==============
(0, 10)
(1, 20)
(2, 30)
"""

# accessing values separate, index, and actual entry at index
print(f" Debug ".center(36, "="))
for i, num in enumerate(numList):
    print(f"{i=}, {num=}")

"""
=============== Debug ===============
i=0, num=10
i=1, num=20
i=2, num=30
"""