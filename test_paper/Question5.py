import numpy as np

class SimpleLinearRegression:
    def __init__(self):
        self.m = 0
        self.b = 0

    def fit(self, X, y):
        X_mean = np.mean(X)
        y_mean = np.mean(y)
        num = np.sum((X - X_mean) * (y - y_mean))
        den = np.sum((X - X_mean) ** 2)

        self.m = num / den
        self.b = y_mean - (self.m * X_mean)

    def pred(self, X):
        return self.m * X + self.b

    def coeff(self):
        return self.m, self.b

if __name__ == "__main__":
    
    X = np.array([1, 2, 3, 4, 5])
    y = np.array([3, 4, 2, 5, 6])

    model = SimpleLinearRegression()
    model.fit(X, y)
    
    m, b = model.coeff()
    print(f"Slope (m): {m}")
    print(f"Intercept (b): {b}")

    X_new = np.array([6, 7, 8])
    y_pred = model.pred(X_new)
    print(f"Predicted values: {y_pred}")

# output :
# Slope (m): 0.7
# Intercept (b): 1.9000000000000004
# Predicted values: [6.1 6.8 7.5]