# d means decimal integer. Display this value as a base-10 integer.

n = 42

print(f"{n:d}")             # Output: 42        -- Usually you don't need d by itself because Python already knows it's an integer.


n = 7
f"{n:03d}"                  # Output: 007
"""
0  -> pad with zeros
3  -> total width = 3
d  -> decimal integer
"""