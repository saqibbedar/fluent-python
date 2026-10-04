# lmf = loss minimization framework

"""
Previously, we were trying to find losses sample by sample.
Now, by using Loss Minimization Framework (LMF),
we generalize the idea from 1 sample to all training examples.

TrainLoss(w) = (1/N) ∑ Loss(xᵢ, yᵢ, w)

where:
    N               : number of training examples
    xᵢ, yᵢ          : ith sample and its true label/output
    w               : weight vector
    Loss(xᵢ, yᵢ, w) : Loss on single sample
    TrainLoss(w)    : average loss over the entire dataset

In our case (Linear Regression):

    Loss(xᵢ, yᵢ, w) = (y_hat - true_y)^2
    TrainLoss(w)    = (1/N) ∑ (y_hatᵢ - yᵢ)^2
"""

# ------------------------------ Dataset ------------------------------
# Each element = (xᵢ, yᵢ)
# xᵢ represents the feature vector, yᵢ is the true output
dataset = [([3, 4], 2), ([1, -1], -1), ([2, 3], 4)]

# Initial weights
w = [0.5, -1.5]


# ------------------------------ Step 1: Prediction ------------------------------
def score(feature_vectors, weights):
    """
    Computes: w · φ(x)
    where φ(x) = feature vector
    """
    result = 0
    for xi, wi in zip(feature_vectors, weights):
        result += xi * wi
    return result


# ------------------------------ Step 2: Per-sample Loss ------------------------------
def squared_loss(y_hat, true_y):
    """
    Squared Loss = (y_hat - true_y)^2
    Measures how far prediction deviates from actual value
    """
    residual = y_hat - true_y
    return residual**2


# ------------------------------ Step 3: Training Loss ------------------------------
def train_loss(dataset, weights):
    """
    TrainLoss(w) = (1/N) ∑ (y_hatᵢ - yᵢ)^2
    This generalizes loss to the whole training dataset.
    """
    N = len(dataset)
    total_loss = 0
    for x_i, y_i in dataset:
        y_hat = score(x_i, weights)
        loss_i = squared_loss(y_hat, y_i)
        total_loss += loss_i
        print(f"Sample: x={x_i}, y={y_i}, y_hat={y_hat:.3f}, Loss={loss_i:.3f}")

    avg_loss = total_loss / N
    return avg_loss


# ------------------------------ Step 4: Execute ------------------------------
train_loss_value = train_loss(dataset, w)
print(f"\nTrainLoss(w): {train_loss_value:.3f}")
