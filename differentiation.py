import sympy as sp

# Define the variable and the function
x = sp.symbols('x')
f = x**3 - x - 2

# Compute the derivative
f_prime = sp.diff(f, x)

print(f"The derivative of {f} is {f_prime}")
