import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_rule(f, a, b, n):
    """
    Approximate the integral of f(x) from a to b using the trapezoidal rule with n subdivisions.

    Parameters:
    f: function to integrate
    a: lower limit of integration
    b: upper limit of integration
    n: number of subdivisions

    Returns:
    float: Approximation of the integral
    """
    x = np.linspace(a, b, n+1)  # n+1 points make n subintervals
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral

# Example function to integrate
def f(x):
    return np.sin(x)

# Integration parameters
a = 0  # lower limit
b = np.pi  # upper limit
n = 100  # number of subdivisions

# Calculate the integral using the trapezoidal rule
result = trapezoidal_rule(f, a, b, n)

# Output the result
print(f"The approximate integral of sin(x) from {a} to {b} using {n} subdivisions is {result}")

# Plotting the function and the trapezoids
x = np.linspace(a, b, 1000)
y = f(x)
x_trap = np.linspace(a, b, n+1)
y_trap = f(x_trap)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b', label='sin(x)')
plt.fill_between(x_trap, 0, y_trap, color='skyblue', alpha=0.4, label='Trapezoids')
plt.plot(x_trap, y_trap, 'ro')  # trapezoid points
plt.title('Trapezoidal Rule Integration of sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid()
plt.show()
