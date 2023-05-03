import matplotlib.pyplot as plt
import numpy as np

def rotated_ellipse(center_x, center_y, point1, point2, semi_major_axis, semi_minor_axis, angle):
    # Rotate the points
    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)
    rot_matrix = np.array([[cos_angle, -sin_angle], [sin_angle, cos_angle]])
    point1 = np.dot(rot_matrix, point1)
    point2 = np.dot(rot_matrix, point2)

    # Calculate the semi-major and semi-minor axes of the ellipse
    distance = np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

    # Generate coordinates of the rotated ellipse
    theta = np.linspace(0, 2*np.pi, 1000)
    x_rotated = center_x + semi_major_axis * np.cos(theta) * np.cos(angle) - semi_minor_axis * np.sin(theta) * np.sin(angle)
    y_rotated = center_y + semi_major_axis * np.cos(theta) * np.sin(angle) + semi_minor_axis * np.sin(theta) * np.cos(angle)


    # Calculate the coordinates of the foci
    c = np.sqrt(semi_major_axis**2 - semi_minor_axis**2)
    focus1 = np.array([center_x + c * np.cos(angle), center_y + c * np.sin(angle)])
    focus2 = np.array([center_x - c * np.cos(angle), center_y - c * np.sin(angle)])

    return x_rotated, y_rotated, focus1, focus2

# Example usage
point1 = np.array([105, 105])
point2 = np.array([155, 155])
center_x = (point1[0] + point2[0]) / 2
center_y = (point1[1] + point2[1]) / 2
semi_major_axis = 35.4
distance = np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
semi_minor_axis = np.sqrt(semi_major_axis**2 - distance**2 / 4)
angle = np.arctan2(point2[1] - point1[1], point2[0] - point1[0])

x, y, focus1, focus2 = rotated_ellipse(center_x, center_y, point1, point2, semi_major_axis, semi_minor_axis, angle)

# Plot the ellipse
fig, ax = plt.subplots()
ax.plot(x, y)
ax.axis('equal')

# Generate random points within the rotated ellipse
num_points = 1000
theta = 2 * np.pi * np.random.rand(num_points)
radius = np.sqrt(np.random.rand(num_points))
# Define the rotation matrix for the ellipse
cos_angle = np.cos(angle)
sin_angle = np.sin(angle)
rot_matrix = np.array([[cos_angle, -sin_angle], [sin_angle, cos_angle]])
# Rotate the random points using the same rotation matrix
rand_points = np.dot(rot_matrix, np.array([semi_major_axis * radius * np.cos(theta), semi_minor_axis * radius * np.sin(theta)]))
x_points = rand_points[0] + center_x
y_points = rand_points[1] + center_y

ax.plot(focus1[0], focus1[1], 'bo')
ax.plot(focus2[0], focus2[1], 'bo')

print("Focus 1:  " + str(focus1))
print("Focus 2:  " + str(focus2))


# Plot the random points
ax.scatter(x_points, y_points, s=5, color='red')
plt.show()
