import numpy as np
import matplotlib.pyplot as plt

def laplace_jacobi(u, tol=1e-6, max_iter=1000):
    rows, cols = u.shape
    u_new = u.copy()
    iteration = 0
    while iteration < max_iter:
        u = u_new.copy()
        for i in range(1, rows-1):
            for j in range(1, cols-1):
                u_new[i, j] = 0.25 * (u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1])

        # Apply boundary conditions
        u_new[:, 0] = T_left  # Left boundary
        u_new[:, -1] = T_right  # Right boundary

        residual = np.max(np.abs(u_new - u))
        if residual < tol:
            break

        iteration += 1

    return u_new, iteration

# Set up the grid and parameters
L = 1.0  # Dimensions of the plate
Nx, Ny = 50, 50  # Number of grid points
T_left, T_right = 200.0, 200.0  # Temperature boundary conditions

# Initialize temperature distribution
T = np.zeros((Nx, Ny))

# Solve Laplace's equation using Jacobi method
solution, iterations = laplace_jacobi(T)

# Plot the solution
x = np.linspace(-L/2, L/2, Nx)
y = np.linspace(-L/2, L/2, Ny)
X, Y = np.meshgrid(x, y)

plt.contourf(X, Y, solution, cmap='hot', levels=50)
plt.colorbar(label='Temperature')
plt.title(f'Temperature Distribution on a Metal Plate\nIterations: {iterations}')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
