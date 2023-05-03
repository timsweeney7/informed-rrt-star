import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np

def rotated_ellipse(center_x, center_y, point1, point2, semi_major_axis, semi_minor_axis):
    # Calculate the semi-major and semi-minor axes of the ellipse
    distance = np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

    # Calculate the angle of rotation of the ellipse
    angle = np.arctan2(point2[1] - point1[1], point2[0] - point1[0])

    # Generate coordinates of the rotated ellipse
    theta = np.linspace(0, 2*np.pi, 1000)
    x_rotated = center_x + semi_major_axis * np.cos(theta) * np.cos(angle) - semi_minor_axis * np.sin(theta) * np.sin(angle)
    y_rotated = center_y + semi_major_axis * np.cos(theta) * np.sin(angle) + semi_minor_axis * np.sin(theta) * np.cos(angle)

    return x_rotated, y_rotated

# Define the ellipse parameters
point1 = [125, 125]
point2 = [135, 125]
center_x = (point1[0] + point2[0]) / 2
center_y = (point1[1] + point2[1]) / 2
semi_major_axis = 50
semi_minor_axis = 25

# Generate the ellipse
x, y = rotated_ellipse(center_x, center_y, point1, point2, semi_major_axis, semi_minor_axis)

# Create a Path object for the ellipse
ellipse_path = mpath.Path(np.column_stack((x, y)))

# Generate random points within the ellipse
n_points = 100
points = []
while len(points) < n_points:
    # Generate random x and y coordinates within the range of the ellipse
    x_rand = np.random.uniform(center_x - semi_major_axis, center_x + semi_major_axis)
    y_rand = np.random.uniform(center_y - semi_minor_axis, center_y + semi_minor_axis)
    
    # Check if the point is inside the ellipse
    if ellipse_path.contains_point([x_rand, y_rand]):
        points.append([x_rand, y_rand])

# Plot the ellipse and the random points
fig, ax = plt.subplots()
ax.plot(x, y)
ax.scatter(np.array(points)[:, 0], np.array(points)[:, 1])
ax.axis('equal')
plt.show()
