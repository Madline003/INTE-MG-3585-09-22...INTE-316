
import numpy as np

def lagrange_coefficients(x, y):
    def L(k, x_val):
        L_k = 1
        for j in range(len(x)):
            if j != k:
                L_k *= (x_val - x[j]) / (x[k] - x[j])
        return L_k
    
    def Lagrange_polynomial(x_val):
        return sum(y[k] * L(k, x_val) for k in range(len(x)))
    
    coeffs = np.polyfit(x, [Lagrange_polynomial(xi) for xi in x], len(x) - 1)
    return coeffs

x_points = [1, 2, 3, 4]
y_points = [1, 4, 9, 16]
coeffs = lagrange_coefficients(x_points, y_points)
print("Lagrange Polynomial Coefficients:",coeffs)


def newton_coefficients(x, y):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:,0] = y

    for j in range(1, n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])

    return coef[0, :]

x_points = [1, 2, 3, 4]
y_points = [1, 4, 9, 16]
coeffs = newton_coefficients(x_points, y_points)
print("Newton's Divided Difference Coefficients:",coeffs)


