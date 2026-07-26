# Consumed Iterator Behavior

e = enumerate(["a", "b", "c"])


print(list(e))          # output: [(0, 'a'), (1, 'b'), (2, 'c')]
print(list(e))          # []: Because the iterator is already exhausted.