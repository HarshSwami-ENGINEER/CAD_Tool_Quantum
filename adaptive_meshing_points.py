import numpy as np
import matplotlib.pyplot as plt


class QuadTreeNode:
    def __init__(self, center, length):
        self.center = center
        self.length = length
        self.children = [
            None,
            None,
            None,
            None,
        ]  # Children nodes in the order NW, NE, SW, SE
        self.is_leaf = True


def refine_tree(node, points, max_depth, depth=0):
    if depth >= max_depth:
        return

    for i in range(4):
        sub_length = node.length / 2
        x_offset = sub_length * (i % 2) - sub_length / 2
        y_offset = sub_length * (i // 2) - sub_length / 2
        child_center = (node.center[0] + x_offset, node.center[1] + y_offset)
        child = QuadTreeNode(child_center, sub_length)
        node.children[i] = child

        # Check if this child contains any user-defined points
        points_in_child = [p for p in points if is_inside(p, child_center, sub_length)]
        if points_in_child:
            refine_tree(child, points_in_child, max_depth, depth + 1)

    node.is_leaf = False


def is_inside(point, center, length):
    return (
        abs(point[0] - center[0]) <= length / 2
        and abs(point[1] - center[1]) <= length / 2
    )


def get_user_points():
    user_points = []
    num_points = int(input("Enter the number of points: "))
    for i in range(num_points):
        x = float(input(f"Enter x-coordinate for point {i+1}: "))
        y = float(input(f"Enter y-coordinate for point {i+1}: "))
        user_points.append((x, y))
    return user_points


def plot_quadtree(node, ax):
    if node.is_leaf:
        ax.add_patch(
            plt.Rectangle(
                (node.center[0] - node.length / 2, node.center[1] - node.length / 2),
                node.length,
                node.length,
                fill=False,
                edgecolor="black",
            )
        )
    else:
        for child in node.children:
            plot_quadtree(child, ax)


def main():
    # User-defined parameters
    square_length = 100
    max_depth = 24
    user_points = get_user_points()  # Get user-defined points

    # Constructing the initial root node
    root = QuadTreeNode((square_length / 2, square_length / 2), square_length)

    # Refine the quadtree based on user-defined points
    refine_tree(root, user_points, max_depth)

    # Plotting
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    plot_quadtree(root, ax)
    for point in user_points:
        ax.plot(point[0], point[1], "ro")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Adaptive Mesh Refinement with Quadtree")
    plt.show()


if __name__ == "__main__":
    main()
