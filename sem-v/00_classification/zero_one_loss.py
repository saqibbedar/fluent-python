"""
1. y_hat = fw_(x) = sin(w.phi(x))
01Loss = 1[(y_hat)*true_y <= 0] = 1[(w.phi(x)) * y <= 0]
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


# prediction_score
prediction_score = score(x, weights)


# zero_one_loss = (w-x)*y
def zero_one_loss(prediction_score, true_y):
    # convert to [-1,+1]
    # y_hat = fw_(x) = sin(w.phi(x))
    y_hat = 1 if math.sin(prediction_score) >= 0 else -1
    loss = y_hat * true_y

    # if positive means no loss return 0 else return 1
    return 0 if loss > 0 else 1


print("score:", prediction_score)
print("y_hat:", 1 if prediction_score >= 0 else -1)
print("zero-one loss:", zero_one_loss(prediction_score, true_y))
