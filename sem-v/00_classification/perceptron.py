"""
The Perceptron update rule:

1. Compute the score (margin): m = w⋅x
2. Predict: y_hat = sign(m)
3. If prediction is wrong (y_hat != true_y), then update: w ← w + yx
"""

x = [1, 1]
y = -1
w = [0, 0]


# Compute margin
def score(x, w):
    return sum(xi * wi for xi, wi in zip(x, w))


# Predict y_hat
def predict(x, w):
    return 1 if score(x, w) >= 0 else -1


# Perceptron update
max_iters = 10
for _ in range(max_iters):
    y_hat_val = predict(x, w)
    if y_hat_val == y:
        print("correct prediction")
        break
    else:
        # update weights
        for i in range(len(w)):
            w[i] += y * x[i]
        print(f"Updated weights: {w}")
