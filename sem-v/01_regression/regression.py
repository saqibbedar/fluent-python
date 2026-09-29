"""
y_hat is prediction done by our algorithm, it is defined as:

    y_hat = (w.phi(x))
"""

x = [3, 4]
w = [0.5, -1.5]

true_y = int(input("What's true_y? "))  # get y input


# find margin/score w.phi(x) where phi(x) = array of x or feature vectors
def score(feature_vectors, weights):
    result = 0
    for x, w in zip(feature_vectors, weights):
        result += x * w

    return result


y_hat = score(x, w)

print("Prediction: ", y_hat)
