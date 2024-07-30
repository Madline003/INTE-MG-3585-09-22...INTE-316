import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define the function to fit
def func(x, a, b, c):
    return a * x**3 + b * x + c

# Generate some data points
x_data = np.linspace(1, 4, 50)
y_data = func(x_data, 1, -1, -2) + 0.5 * np.random.normal(size=len(x_data))

# Fit the curve
popt, pcov = curve_fit(func, x_data, y_data)

# Plot the data and the fitted curve
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, func(x_data, *popt), label='Fitted curve', color='yellow')
plt.legend()
plt.show()

print(f"Fitted parameters: a={popt[0]}, b={popt[1]}, c={popt[2]}")

