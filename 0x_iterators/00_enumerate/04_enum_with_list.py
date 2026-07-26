# Note: You can start with any index, either negative or positive. If positive, indexes will grow orderly and decrease same.

# Positive: starting index is 5.
for i, val in enumerate(["apple", "banana", "carrot"], start=5):
    print(i, val)

"""
5 apple
6 banana
7 carrot
"""


# Positive: starting index is 5.
for i, val in enumerate(["apple", "banana", "carrot"], start=-5):
    print(i, val)

"""
-5 apple
-4 banana
-3 carrot
"""