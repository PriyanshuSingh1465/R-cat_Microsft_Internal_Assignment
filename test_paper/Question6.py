import numpy as np

def test(z):
    return 1 / (1 + np.exp(-z))

def cost_fun(theta, X, y):
    m = len(y)  
    h = test(np.dot(X, theta))
    ep = 1e-5  
    cost = -(1/m) * (np.dot(y, np.log(h + ep)) + np.dot((1 - y), np.log(1 - h + ep)))
    return cost

if __name__ == "__main__":
    
    X = np.array([[1, 2], [1, 3], [1, 4], [1, 5]])  
    y = np.array([0, 0, 1, 1])
    theta = np.array([0.1, 0.2])  
    cost = cost_fun(theta, X, y)
    print(f"Cost: {cost}")

# output :
# Cost: 0.6764170536896302