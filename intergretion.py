import scipy.integrate as spi

# Define the function
def f(x):
    return x**4 - x - 2

# Perform numerical integration from 0 to 2
integral, error = spi.quad(f, 0, 2)

print(f"The integral of f(x) from 0 to 2 is approximately {integral} with an error of {error}")
