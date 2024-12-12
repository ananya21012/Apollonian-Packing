#integer appolonian packing

import matplotlib.pyplot as plt
import numpy as np
import math

# Function to plot a circle
def plot_circle(ax, center, radius, **kwargs):
    circle = plt.Circle(center, radius, **kwargs)
    ax.add_artist(circle)

# Function to calculate the new curvature using Descartes' Circle Theorem
def new_curvature_inner(k1, k2, k3):
    return k1 + k2 + k3 + 2 * np.sqrt(k1 * k2 + k2 * k3 + k3 * k1)

def new_curvature_outer(k1, k2, k3):
    return k1 + k2 + k3 - 2 * np.sqrt(k1 * k2 + k2 * k3 + k3 * k1)
   

# Initialize plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Initial circle centers and curvatures (3 mutually tangent circles)
centers = [[0, 0], [1, 0], [0.5, 2/3]]

radius=[]
curvatures=[2, 2,3]


# # Plot the initial circles
for center, curvature in zip(centers, curvatures):
    radius = 1 / curvature
    plot_circle(ax, center, radius, fill=False, color='black')

curvatures.append(new_curvature_inner(curvatures[0],curvatures[1],curvatures[2]))
curvatures.append(new_curvature_outer(curvatures[0],curvatures[1],curvatures[2]))
centers.append([0.5,4/15])
centers.append([0.5,0])

plot_circle(ax,centers[3],1/curvatures[3],fill=False,color='black')
plot_circle(ax,centers[4],1/curvatures[4],fill=False,color='black')
plot_circle(ax,[0.5,-2/3],1/3,fill=False,color='black')


# Display the plot
plt.show()




     


