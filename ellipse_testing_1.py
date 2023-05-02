import random
import math
import matplotlib.pyplot as plt
import numpy as np

def random_point_in_ellipse(a, b):
    # Generate random angle
    angle = random.uniform(0, 2*math.pi)
    # Generate random point inside unit circle
    r = math.sqrt(random.uniform(0, 1))
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    # Scale point to ellipse
    x *= a
    y *= b
    return (x, y)


def plot_ellipse(a, b):
    
    return ax


def plot_points(points):
    
    return

# Example usage
a = 3  # Semi-major axis
b = 2  # Semi-minor axis
points = []
for i in range(0,100):
    random_point = random_point_in_ellipse(a, b)
    points.append(random_point)

# Generate points on ellipse
t = np.linspace(0, 2*np.pi, 1000)
x = a * np.cos(t)
y = b * np.sin(t)
# Plot ellipse
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_aspect('equal', 'box')

x, y = zip(*points)
ax.plot(x, y)

plt.show()
