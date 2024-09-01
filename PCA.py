import numpy as np

class PCA:
    def __init__(self, k):
        self.k = k
    
    def Standardization(self, X):
        mean = np.mean(X, axis=0)
        std_dev = np.std(X, axis=0)
        return (X - mean) / std_dev

    def CovarianceMatrix(self, X):
        n = len(X)
        Z = self.Standardization(X)
        C = np.dot(Z.T, Z) / (n - 1)
        return C

    def SortedEigenvalues(self, X): 
        eigenvalues, eigenvectors = np.linalg.eig(X)
        idx = np.argsort(eigenvalues)[::-1]  # Sort in descending order
        sorted_eigenvalues = eigenvalues[idx]
        sorted_eigenvectors = eigenvectors[:, idx]
        return sorted_eigenvalues, sorted_eigenvectors

    def select_top_k_components(self, sorted_eigenvectors):
        return sorted_eigenvectors[:, :self.k]

    def components(self, X):
        Z = self.Standardization(X)
        C = self.CovarianceMatrix(Z)
        _, sorted_eigenvectors = self.SortedEigenvalues(C)
        T = self.select_top_k_components(sorted_eigenvectors)
        return np.dot(Z, T)

# Example Usage
if __name__ == "__main__":
    # Example dataset: 5 samples, 3 features
    X = np.array([[2.5, 2.4, 2.7],
                  [0.5, 0.7, 1.0],
                  [2.2, 2.9, 2.4],
                  [1.9, 2.2, 1.9],
                  [3.1, 3.0, 3.1]])

    # Create a PCA instance with k=2
    pca = PCA(k=2)

    # Compute the principal components
    X_transformed = pca.components(X)

    print("Components(X):")
    print(X)
    print("Original shape:", X.shape)
    print("Components (X_transformed):")
    print(X_transformed)
    print("Transformed shape:", X_transformed.shape)
