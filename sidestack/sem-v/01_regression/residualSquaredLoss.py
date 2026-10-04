"""
y_hat is prediction done by our algorithm, it is defined as:

    y_hat = (w.phi(x))

# Losses: Measures how wrong predictor predicts
    In our course, we took Residual but in ML approach they call it as error (i.e., in prediction)

    Residual = (y_hat - true_y) # statistical
    Error = (true_y - y_hat) # ML approach

    SquaredLoss: Used in linear regression to flip the sings and there are other advantages too

    SquaredLoss = (Residual)^2 or (y_hat - true_y)^2
"""

x = [3, 4]
w = [0.5, -1.5]

true_y = int(input("What's true_y? "))  # get y input


# find margin/score w.phi(x) where phi(x) = array of x or feature vectors
def score(feature_vectors, weights):
    result = 0
    for xi, wi in zip(feature_vectors, weights):
        result += xi * wi

    return result


y_hat = score(x, w)


# Find residual
def residual(y_hat, true_y):
    return y_hat - true_y


# Find Squared Loss
def squared_loss(residual):
    return (residual) ** 2


# loss computation
r = residual(y_hat, true_y)
sqLoss = squared_loss(r)

print(f"Prediction: {y_hat}")
print(f"Residual: {r}")
print(f"SquaredLoss: {sqLoss}")
