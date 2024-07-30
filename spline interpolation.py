import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# Generate some data points
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Perform spline interpolation
spl = UnivariateSpline(x, y)

# Generate dense x values for a smooth curve
x_dense = np.linspace(0, 10, 1000)
y_dense = spl(x_dense)

# Plot the data points and the interpolated curve
plt.scatter(x, y, label='Data')
plt.plot(x_dense, y_dense, label='Spline interpolation', color='red')
plt.legend()
plt.show()
