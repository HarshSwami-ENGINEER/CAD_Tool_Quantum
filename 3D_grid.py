import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def discretize_cube(cube_size, grid_size):
    num_points = int(cube_size / grid_size) + 1
    x = np.linspace(0, cube_size, num_points)
    y = np.linspace(0, cube_size, num_points)
    z = np.linspace(0, cube_size, num_points)
    return np.meshgrid(x, y, z)


def discretize_region_3d(region_size, grid_size, region_center):
    half_size = region_size / 2
    num_points = int(region_size / grid_size) + 1
    x = np.linspace(
        region_center[0] - half_size, region_center[0] + half_size, num_points
    )
    y = np.linspace(
        region_center[1] - half_size, region_center[1] + half_size, num_points
    )
    z = np.linspace(
        region_center[2] - half_size, region_center[2] + half_size, num_points
    )
    return np.meshgrid(x, y, z)


# Get user input
cube_size = float(input("Enter the size of the cube: "))
initial_grid_size = float(input("Enter the initial grid size: "))
region_size = float(input("Enter the size of the region to be refined: "))
region_center = tuple(
    map(float, input("Enter the coordinates of the region center (x y z): ").split())
)
refined_grid_size = float(input("Enter the refined grid size for the region: "))

# Discretize the cube
X, Y, Z = discretize_cube(cube_size, initial_grid_size)

# Discretize the specified region within the cube
region_X, region_Y, region_Z = discretize_region_3d(
    region_size, initial_grid_size, region_center
)

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# Plot the cube with discretization
ax.scatter(X, Y, Z, color="black")

# Plot the specified region with discretization
ax.scatter(region_X, region_Y, region_Z, color="red")

ax.set_title("Discretization of Cube, Specified Region")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
