import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate some random data in Cartesian coordinates
num_points = 100
x = np.random.uniform(-1, 1, num_points)
y = np.random.uniform(-1, 1, num_points)
z = np.random.uniform(0, 360, num_points)

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='r', marker='o')  # Scatter plot of points

# Plotting angle arms from the origin to each point
origin = [0], [0], [0]
for i in range(num_points):
    ax.plot([origin[0][0], x[i]], [origin[1][0], y[i]], [origin[2][0], z[i]], c='b')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z (Angle in degrees)')
ax.set_title('3D Scatter Plot with Angle Arms')

# Show the plot
plt.show()
