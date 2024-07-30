
def gradient_descent(func, grad, x0, learning_rate, num_iterations):
    x = np.array(x0, dtype=float)
    for _ in range(num_iterations):
        grad_x = grad(x)
        x = x - learning_rate * grad_x
    return x

def func(x):
    return -x[0]*2 - x[1]*2 - x[0]*x[1] + 2*x[0] + x[1] - 1

def grad(x):
    dfdx = -2*x[0] - x[1] + 2
    dfdy = -2*x[1] - x[0] + 1
    return np.array([dfdx, dfdy])

x0 = [0, 0]
learning_rate = 0.1
num_iterations = 100
min_point = gradient_descent(func, grad, x0, learning_rate, num_iterations)
print("Minimum point:",min_point)
