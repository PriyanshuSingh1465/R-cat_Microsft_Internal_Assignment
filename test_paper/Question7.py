import numpy as np

class KMeans:
    def __init__(self, n_cluster, max=300, tol=1e-4):
        self.n_cluster = n_cluster
        self.max = max
        self.tol = tol

    def fit(self, X):
        self.centroids = X[np.random.choice(X.shape[0], self.n_cluster, replace=False)]
        for _ in range(self.max):
            distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
            self.labels = np.argmin(distances, axis=1)
            new_centroids = np.array([X[self.labels == i].mean(axis=0) for i in range(self.n_cluster)])
            if np.all(np.abs(new_centroids - self.centroids) < self.tol):
                break
            self.centroids = new_centroids

    def predict(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)


if __name__ == "__main__":
    X = np.array([
        [1, 2], [1, 4], [1, 0],
        [10, 2], [10, 4], [10, 0]
    ])
    kmeans = KMeans(n_cluster=2)
    kmeans.fit(X)
    print("Centroids:")
    print(kmeans.centroids)
    print("Labels:")
    print(kmeans.labels)
    new_data = np.array([[0, 0], [12, 3]])
    predictions = kmeans.predict(new_data)
    print("Predictions for new data:")
    print(predictions)

# output :