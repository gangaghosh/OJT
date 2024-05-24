import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
g = 9.81  # gravity (m/s^2)
e = 0.8   # coefficient of restitution (elasticity)
dt = 0.01 # time step (s)
ground_level = 0

# Ball properties
ball_radius = 0.1
initial_height = 5
initial_velocity = 0

# Ball state
y = initial_height
v = initial_velocity
t = 0

# Flag to check if ball has started rolling
rolling = False
t_start_rolling = 0
horizontal_speed = 2  # horizontal speed when rolling

# Figure setup
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-1, 6)
ball, = ax.plot([], [], 'o', markersize=20)

# Update function
def update(frame):
    global y, v, t, rolling, t_start_rolling
    t += dt
    
    if not rolling:
        v += -g * dt
        y += v * dt
        
        # Check for collision with the ground
        if y <= ground_level + ball_radius:
            y = ground_level + ball_radius
            v = -v * e  # reverse velocity with elasticity
        
        # Update ball position
        ball.set_data([5], [y])
        
        # If the ball is rolling on the ground, move it horizontally
        if y == ground_level + ball_radius and abs(v) < 0.1:
            rolling = True
            t_start_rolling = t
    else:
        x = 5 + (t - t_start_rolling) * horizontal_speed
        ball.set_data([x], [ground_level + ball_radius])
    
    return ball,

# Initialization function
def init():
    ball.set_data([5], [initial_height])
    return ball,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 500), init_func=init, blit=True, interval=dt*1000)

# Show the animation
plt.show()
