data = {
    "a": 100,
    "b": 200,
    "c": 300
}

for index, key in enumerate(data):
    print(index, key)

# Output:
# 0 a
# 1 b
# 2 c

print(f"{"Index":<10} | {"Key":<10} | {"Value"}")
for i, (k, v) in enumerate(data.items()):
    print(f"{i:<10} | {k:<10} | {v}")

"""
Index      | Key        | Value
0          | a          | 100
1          | b          | 200
2          | c          | 300
"""