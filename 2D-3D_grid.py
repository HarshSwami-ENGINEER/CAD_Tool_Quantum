import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class DiscretizeShape:
    def __init__(self, shape_type, size, grid_size):
        self.shape_type = shape_type  # '2D' or '3D'
        self.size = size  # Overall size of the shape (tuple)
        self.grid_size = grid_size  # Grid size for discretization
        self.grid = None  # Discretized grid
        self.create_grid()

    def create_grid(self):
        if self.shape_type == '2D':
            x = np.arange(0, self.size[0], self.grid_size)
            y = np.arange(0, self.size[1], self.grid_size)
            self.grid = np.array(np.meshgrid(x, y)).T.reshape(-1, 2)  # 2D coordinates

        elif self.shape_type == '3D':
            x = np.arange(0, self.size[0], self.grid_size)
            y = np.arange(0, self.size[1], self.grid_size)
            z = np.arange(0, self.size[2], self.grid_size)
            self.grid = np.array(np.meshgrid(x, y, z)).T.reshape(-1, 3)  # 3D coordinates

    def get_subgrid(self, region, subgrid_size):
        if self.shape_type == '2D':
            x = np.arange(region[0][0], region[1][0], subgrid_size)
            y = np.arange(region[0][1], region[1][1], subgrid_size)
            subgrid = np.array(np.meshgrid(x, y)).T.reshape(-1, 2)  # 2D coordinates
        
        elif self.shape_type == '3D':
            x = np.arange(region[0][0], region[1][0], subgrid_size)
            y = np.arange(region[0][1], region[1][1], subgrid_size)
            z = np.arange(region[0][2], region[1][2], subgrid_size)
            subgrid = np.array(np.meshgrid(x, y, z)).T.reshape(-1, 3)  # 3D coordinates
        
        return subgrid

    def plot(self, subgrid=None):
        if self.shape_type == '2D':
            x = np.unique(self.grid[:, 0])
            y = np.unique(self.grid[:, 1])
            plt.figure()
            for xi in x:
                plt.plot([xi, xi], [min(y), max(y)], 'b-', alpha=0.7, linewidth=1)  # vertical lines
            for yi in y:
                plt.plot([min(x), max(x)], [yi, yi], 'b-', alpha=0.7, linewidth=1)  # horizontal lines
            
            if subgrid is not None:
                x_sub = np.unique(subgrid[:, 0])
                y_sub = np.unique(subgrid[:, 1])
                for xi in x_sub:
                    plt.plot([xi, xi], [min(y_sub), max(y_sub)], 'r-', alpha=0.7, linewidth=1.5)  # vertical lines
                for yi in y_sub:
                    plt.plot([min(x_sub), max(x_sub)], [yi, yi], 'r-', alpha=0.7, linewidth=1.5)  # horizontal lines

            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('2D Discretization with Lines')
            plt.grid(True)
            plt.show()

        elif self.shape_type == '3D':
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            # Plotting lines along X, Y, and Z axes to form a wireframe
            # Horizontal lines in the XY plane
            for z in np.unique(self.grid[:, 2]):
                x_vals = np.unique(self.grid[:, 0])
                y_vals = np.unique(self.grid[:, 1])
                for y in y_vals:
                    ax.plot([min(x_vals), max(x_vals)], [y, y], [z, z], 'b-', alpha=0.7, linewidth=1)
                for x in x_vals:
                    ax.plot([x, x], [min(y_vals), max(y_vals)], [z, z], 'b-', alpha=0.7, linewidth=1)

            # Vertical lines along the Z axis
            for xi in np.unique(self.grid[:, 0]):
                for yi in np.unique(self.grid[:, 1]):
                    ax.plot([xi, xi], [yi, yi], [min(self.grid[:, 2]), max(self.grid[:, 2])], 'b-', alpha=0.7, linewidth=1)

            # Plotting subgrid if provided
            if subgrid is not None:
                x_sub = np.unique(subgrid[:, 0])
                y_sub = np.unique(subgrid[:, 1])
                z_sub = np.unique(subgrid[:, 2])

                for z in z_sub:
                    for y in y_sub:
                        ax.plot([min(x_sub), max(x_sub)], [y, y], [z, z], 'r-', alpha=0.7, linewidth=1.5)
                    for x in x_sub:
                        ax.plot([x, x], [min(y_sub), max(y_sub)], [z, z], 'r-', alpha=0.7, linewidth=1.5)

                for xi in x_sub:
                    for yi in y_sub:
                        ax.plot([xi, xi], [yi, yi], [min(z_sub), max(z_sub)], 'r-', alpha=0.7, linewidth=1.5)

            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.set_title('3D Discretization with Lines')
            plt.show()

# Example 1: Discretize and plot 2D shapes with lines
discretizer_2D = DiscretizeShape('2D', (10, 10), 2)
subgrid_2D = discretizer_2D.get_subgrid(((2, 2), (8, 8)), 1)
discretizer_2D.plot(subgrid_2D)  # Plotting the 2D grid and subgrid with lines

# Example 2: Discretize and plot 3D shapes with lines
discretizer_3D = DiscretizeShape('3D', (10, 10, 10), 2)
subgrid_3D = discretizer_3D.get_subgrid(((2, 2, 2), (8, 8, 8)), 1)
discretizer_3D.plot(subgrid_3D)  # Plotting the 3D grid and subgrid with wireframe lines
