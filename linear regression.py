 
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generate some data points
x = np.array([1, 3, 5, 7, 9]).reshape((-1, 1))
y = np.array([1, 3, 2, 5, 4])

# Create the model and fit it
model = LinearRegression().fit(x, y)

# Predict values
y_pred = model.predict(x)

# Plot the data and the regression line
plt.scatter(x, y, label='Data')
plt.plot(x, y_pred, label='Regression line', color='green')
plt.legend()
plt.show()

print(f"Intercept: {model.intercept_}")
print(f"Slope: {model.coef_[0]}")
