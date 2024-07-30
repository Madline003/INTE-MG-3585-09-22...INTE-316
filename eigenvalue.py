
import numpy as np

def power_iteration(A, num_simulations: int):
    b_k = np.random.rand(A.shape[1])
    
    for _ in range(num_simulations):
        b_k1 = np.dot(A, b_k)
        b_k1_norm = np.linalg.norm(b_k1)
        b_k = b_k1 / b_k1_norm
    
    eigenvalue = np.dot(b_k.T, np.dot(A, b_k))
    eigenvector = b_k
    return eigenvalue, eigenvector

A = np.array([[4, 1, 1], [1, 3, -1], [1, -1, 2]])
eigenvalue, eigenvector = power_iteration(A, 100)
print("Eigenvalue:", eigenvalue)
print("Eigenvector:",eigenvector)

def qr_algorithm(A, num_iterations):
    A_k = np.copy(A)
    for _ in range(num_iterations):
        Q, R = np.linalg.qr(A_k)
        A_k = np.dot(R, Q)
    
    eigenvalues = np.diag(A_k)
    eigenvectors = Q
    return eigenvalues, eigenvectors

A = np.array([[4, 1, 1], [1, 3, -1], [1, -1, 2]])
eigenvalues, eigenvectors = qr_algorithm(A, 100)
print("Eigenvalues:",eigenvalues)
print("Eigenvectors:",eigenvectors)
