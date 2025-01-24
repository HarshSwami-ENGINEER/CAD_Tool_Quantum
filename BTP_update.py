import numpy as np
import matplotlib.pyplot as plt

def discretize_square(square_size, grid_size):
    num_points = square_size // grid_size
    x = np.linspace(0, square_size, num_points + 1)
    y = np.linspace(0, square_size, num_points + 1)
    return np.meshgrid(x, y)

def discretize_region(region_size, grid_size, region_center):
    half_size = region_size // 2
    num_points = region_size // grid_size
    x = np.linspace(region_center[0] - half_size, region_center[0] + half_size, num_points + 1)
    y = np.linspace(region_center[1] - half_size, region_center[1] + half_size, num_points + 1)
    return np.meshgrid(x, y)

# Get user input
square_size = int(input("Enter the size of the square: "))
initial_grid_size = int(input("Enter the initial grid size: "))
region_size = int(input("Enter the size of the region to be refined: "))
region_center = tuple(map(int, input("Enter the coordinates of the region center (x y): ").split()))
refined_grid_size = int(input("Enter the refined grid size for the region: "))

# Discretize the square
X, Y = discretize_square(square_size, initial_grid_size)

# Discretize the region
region_X, region_Y = discretize_region(region_size, refined_grid_size, region_center)

# Plotting
plt.figure(figsize=(8, 8))

# Plot original square with discretization
plt.plot(X, Y, 'k-')
plt.plot(X.T, Y.T, 'k-')

# Plot the refined region with discretization
plt.plot(region_X, region_Y, 'r-')
plt.plot(region_X.T, region_Y.T, 'r-')

plt.title('Discretization of Square and Refined Region')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.xlim(0, square_size)
plt.ylim(0, square_size)
plt.gca().set_aspect('equal', adjustable='box')

plt.show()
