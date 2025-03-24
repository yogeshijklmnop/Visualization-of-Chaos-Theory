import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Lorenz equation
def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot

# Define the initial conditions
x1, y1, z1 = (0, 1, 1.05)  # Initial coordinates of point 1
x2, y2, z2 = (1, 2, 2.05)  # Initial coordinates of point 2
x3, y3, z3 = (2,3,.05)


# Set the time step and total time
dt = 0.01
tmax = 30
nsteps = int(tmax / dt)

# Create the figure and axes objects
fig = plt.figure(facecolor='black')
#ax = fig.add_subplot(111, projection='3d')
plt.xlabel('X', color='black')
plt.ylabel('Y', color='black')
#plt.zlabel('Z', color='white')
plt.title('Lorenz Attractor')
#ax.set_facecolor('black')

"""
# Set the grid color to white and make it thinner
ax.xaxis.pane.set_edgecolor('white')
ax.yaxis.pane.set_edgecolor('white')
ax.zaxis.pane.set_edgecolor('white')
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.grid(True, linewidth=0.5, color='white')

# Set the tick color to white
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.tick_params(axis='z', colors='white')
"""
# Initialize the data arrays
x1s = np.empty(nsteps)
y1s = np.empty(nsteps)
z1s = np.empty(nsteps)
x2s = np.empty(nsteps)
y2s = np.empty(nsteps)
z2s = np.empty(nsteps)
x3s = np.empty(nsteps)
y3s = np.empty(nsteps)
z3s = np.empty(nsteps)

# Set the first values
x1s[0], y1s[0], z1s[0] = (x1, y1, z1)
x2s[0], y2s[0], z2s[0] = (x2, y2, z2)
x3s[0], y3s[0], z3s[0] = (x3, y3, z3)
"""
# Create the plot objects for point 1 and point 2
ln1, = ax.plot([], [], [], color='lime', lw=1)
ln2, = ax.plot([], [], [], color='yellow', lw=1)
ln3, = ax.plot([], [], [], color='lightblue', lw=1)
"""
# Set the axis limits
plt.xlim(-25, 25)
plt.ylim(-35, 35)
#ax.set_zlim(5, 55)

# Create the animation loop
for i in range(1, nsteps):
    # Update the data for point 1
    x1_dot, y1_dot, z1_dot = lorenz(x1s[i-1], y1s[i-1], z1s[i-1])
    x1s[i] = x1s[i-1] + x1_dot * dt
    y1s[i] = y1s[i-1] + y1_dot * dt
    z1s[i] = z1s[i-1] + z1_dot * dt
    
    # Update the data for point 2
    x2_dot, y2_dot, z2_dot = lorenz(x2s[i-1], y2s[i-1], z2s[i-1])
    x2s[i] = x2s[i-1] + x2_dot * dt
    y2s[i] = y2s[i-1] + y2_dot * dt
    z2s[i] = z2s[i-1] + z2_dot * dt

    # Update the data for point 3
    x3_dot, y3_dot, z3_dot = lorenz(x3s[i-1], y3s[i-1], z3s[i-1])
    x3s[i] = x3s[i-1] + x3_dot * dt
    y3s[i] = y3s[i-1] + y3_dot * dt
    z3s[i] = z3s[i-1] + z3_dot * dt

    # Update the plot for point 1 and point 2
    plt.plot(x1s[:i], y1s[:i], color="lime", lw=1)
    #ln1.set_3d_properties(z1s[:i])
    plt.plot(x2s[:i], y2s[:i], color="yellow", lw=1)
    #ln2.set_3d_properties(z2s[:i])
    plt.plot(x3s[:i], y3s[:i], color="lightblue", lw=1)
    #ln3.set_3d_properties(z3s[:i])
    plt.draw()
    plt.pause(0.01)

# Show the plot
plt.show()