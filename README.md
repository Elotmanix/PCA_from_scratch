
# Principal Component Analysis (PCA) Implementation

This repository contains an implementation of Principal Component Analysis (PCA) in Python using NumPy. PCA is a dimensionality reduction technique used to reduce the number of variables in a dataset while retaining the most important information.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Class Methods](#class-methods)
- [Example](#example)
- [Contributing](#contributing)

## Features

- Standardizes the dataset before performing PCA.
- Computes the covariance matrix of the standardized data.
- Extracts and sorts eigenvalues and eigenvectors to identify principal components.
- Reduces the dimensionality of the dataset by selecting the top `k` principal components.

## Installation

To use this code, ensure that you have Python installed along with the NumPy library. You can install NumPy using pip if it is not already installed:

```bash
pip install numpy
```

## Usage

You can use this PCA implementation by creating an instance of the `PCA` class and calling the `components` method to compute the principal components.

### Basic Workflow

1. **Standardization:** Standardize the dataset to have a mean of 0 and a standard deviation of 1.
2. **Covariance Matrix Calculation:** Compute the covariance matrix of the standardized data.
3. **Eigenvalue Decomposition:** Perform eigenvalue decomposition on the covariance matrix to obtain eigenvalues and eigenvectors.
4. **Sort Eigenvalues and Eigenvectors:** Sort the eigenvalues and corresponding eigenvectors in descending order.
5. **Select Top `k` Components:** Select the top `k` eigenvectors as the principal components.
6. **Transform Data:** Project the standardized data onto the selected principal components.

## Class Methods

### `__init__(self, k)`
- Initializes the PCA instance with the number of principal components `k` to retain.

### `Standardization(self, X)`
- Standardizes the dataset `X` to have zero mean and unit variance.

### `CovarianceMatrix(self, X)`
- Computes the covariance matrix of the standardized dataset `X`.

### `SortedEigenvalues(self, X)`
- Performs eigenvalue decomposition on the covariance matrix and returns sorted eigenvalues and corresponding eigenvectors.

### `select_top_k_components(self, sorted_eigenvectors)`
- Selects the top `k` eigenvectors to use as principal components.

### `components(self, X)`
- Transforms the dataset `X` to a lower-dimensional space using the top `k` principal components.

## Example

An example of how to use this PCA implementation is included in the code. To run the example:

```bash
python pca.py
```

This example demonstrates how to reduce a dataset with 3 features to 2 principal components.

Example Output:

```bash
Components(X):
[[2.5 2.4 2.7]
 [0.5 0.7 1.0]
 [2.2 2.9 2.4]
 [1.9 2.2 1.9]
 [3.1 3.0 3.1]]
Original shape: (5, 3)
Components (X_transformed):
[[-0.82861743 -0.57735027]
 [ 1.58701371  0.57735027]
 [-1.35640226 -0.57735027]
 [-0.2772244   0.57735027]
 [ 0.87523037  0.57735027]]
Transformed shape: (5, 2)
```

## Contributing

If you want to contribute to this project, feel free to open an issue or submit a pull request.
