"""
1. f_w(x) = sign(w.phi(x)) where w.phi(x) are called score or margin and phi(x) is feature vector or in simple terms array of data and w represents weights

Overall, f_w(x) is called y_hat.

1. We will be given inputs as x(phi(x) or feature vectors) in an array or any data structure.
2. secondly weight vectors also in an array
3. Also true_y which is given or sometimes we are asked to find, its a true labeled value which we compare with predicted or y_hat.
"""

import math

x = [3, 2, -9]
weights = [0.1, -0.5, 1]

# Input true_y
true_y = int(input("enter true_y value[-1 or +1]: "))


# score/margin: measure model prediction score
def score(x, w):
    sc = 0
    # Iterate over x and weights to get score sc = w.phi(x)
    for xi, wi in zip(x, w):
        sc += wi * xi

    return sc


# predicted output
sc = score(x, weights)

# convert to [-1,+1]
# y_hat = fw_(x) = sin(w.phi(x))
y_hat = 1 if math.sin(sc) >= 0 else -1

if y_hat == true_y:
    print("correct")
else:
    print("wrong")
