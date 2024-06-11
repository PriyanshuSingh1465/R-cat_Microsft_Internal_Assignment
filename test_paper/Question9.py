import numpy as np

class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None

    def fit(self, X):
        self.mean = np.mean(X, axis=0)
        X_center = X - self.mean
        cov_matrix = np.cov(X_center, rowvar=False)
        _, self.components = np.linalg.eigh(cov_matrix)
        self.components = self.components[:, ::-1][:, :self.n_components]

    def transform(self, X):
        X_center = X - self.mean
        return np.dot(X_center, self.components)

# Example usage
if __name__ == "__main__":
    X = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    pca = PCA(n_components=2)
    pca.fit(X)
    transformed = pca.transform(X)

    print("Original data:")
    print(X)
    print("Transformed data:")
    print(transformed)

# output :
# Original data:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# Transformed data:
# [[-5.19615242e+00  7.21644966e-16]
#  [ 0.00000000e+00  0.00000000e+00]
#  [ 5.19615242e+00 -7.21644966e-16]]