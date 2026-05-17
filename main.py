# ============================================
# ROCKET TRAJECTORY SIMULATOR
# ============================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------------------
# USER INPUTS
# -------------------------------

velocity = float(input("Enter launch velocity (m/s): "))
angle = float(input("Enter launch angle (degrees): "))

print("\nChoose Planet:")
print("1. Earth")
print("2. Moon")
print("3. Mars")

choice = input("Enter choice (1/2/3): ")

# Gravity values
if choice == "2":
    gravity = 1.62
    planet = "Moon"
elif choice == "3":
    gravity = 3.71
    planet = "Mars"
else:
    gravity = 9.81
    planet = "Earth"

# -------------------------------
# CONVERT ANGLE TO RADIANS
# -------------------------------

theta = np.radians(angle)

# Velocity components
vx = velocity * np.cos(theta)
vy = velocity * np.sin(theta)

# -------------------------------
# TIME OF FLIGHT
# -------------------------------

time_of_flight = (2 * vy) / gravity

# Time intervals
t = np.linspace(0, time_of_flight, 500)

# -------------------------------
# PROJECTILE MOTION EQUATIONS
# -------------------------------

x = vx * t
y = vy * t - 0.5 * gravity * t**2

# -------------------------------
# IMPORTANT VALUES
# -------------------------------

max_height = (vy**2) / (2 * gravity)
range_distance = vx * time_of_flight

# -------------------------------
# OUTPUT RESULTS
# -------------------------------

print("\n========== FLIGHT DATA ==========")
print(f"Planet: {planet}")
print(f"Gravity: {gravity} m/s²")
print(f"Time of Flight: {time_of_flight:.2f} seconds")
print(f"Maximum Height: {max_height:.2f} meters")
print(f"Horizontal Range: {range_distance:.2f} meters")

# -------------------------------
# PLOT GRAPH
# -------------------------------

# -------------------------------
# ANIMATED TRAJECTORY
# -------------------------------

fig, ax = plt.subplots(figsize=(10, 5))

# Axis limits
ax.set_xlim(0, max(x) + 10)
ax.set_ylim(0, max(y) + 10)

# Labels and title
ax.set_title(f"Rocket Trajectory on {planet}")
ax.set_xlabel("Horizontal Distance (m)")
ax.set_ylabel("Vertical Height (m)")

ax.grid(True)

# Rocket point
rocket, = ax.plot([], [], 'ro')

# Trajectory line
trajectory, = ax.plot([], [], 'b-')

# Initialization function
def init():
    rocket.set_data([], [])
    trajectory.set_data([], [])
    return rocket, trajectory

# Animation function
def update(frame):

    # Rocket position
    rocket.set_data([x[frame]], [y[frame]])

    # Path traveled so far
    trajectory.set_data(x[:frame], y[:frame])

    return rocket, trajectory

# Create animation
ani = FuncAnimation(
    fig,
    update,
    frames=len(t),
    init_func=init,
    interval=20,
    blit=True
)

plt.show()
