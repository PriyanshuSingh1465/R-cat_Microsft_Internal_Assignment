import numpy as np

class GradientDescent:
    def __init__(self, rate=0.01, max=1000, tol=1e-6):
        self.rate = rate
        self.max = max
        self.tol = tol

    def minimize(self, f, grad_f, x_init):
        x = np.copy(x_init)
        for _ in range(self.max):
            grad = grad_f(x)
            x_new = x - self.rate * grad
            if np.linalg.norm(x_new - x) < self.tol:
                break
            x = x_new
        return x


if __name__ == "__main__":
    def f(x):
        return x[0]**2 + x[1]**2

    def grad_f(x):
        return np.array([2 * x[0], 2 * x[1]])

    x_init = np.array([3.0, 4.0])
    gd = GradientDescent(rate=0.1, max=1000, tol=1e-6)
    min_x = gd.minimize(f, grad_f, x_init)

    print("Minimum point:", min_x)
    print("Minimum value:", f(min_x))


# output :
