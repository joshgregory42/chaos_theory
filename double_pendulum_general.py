from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

'''
Source: https://matplotlib.org/2.0.2/examples/animation/double_pendulum_animated.html
'''

g = 9.80665

L1 = 1.0  # length of pendulum 1 in meters
L2 = 1.0  # length of pendulum 2 in meters

M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg


def deriv(state, t):
    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    del_ = state[2] - state[0]
    den1 = (M1 + M2) * L1 - M2 * L1 * cos(del_) * cos(del_)
    dydx[1] = (M2 * L1 * state[1] * state[1] * sin(del_) * cos(del_) +
               M2 * g * sin(state[2]) * cos(del_) +
               M2 * L2 * state[3] * state[3] * sin(del_) -
               (M1 + M2) * g * sin(state[0])) / den1

    dydx[2] = state[3]

    den2 = (L2 / L1) * den1
    dydx[3] = (-M2 * L2 * state[3] * state[3] * sin(del_) * cos(del_) +
               (M1 + M2) * g * sin(state[0]) * cos(del_) -
               (M1 + M2) * L1 * state[1] * state[1] * sin(del_) -
               (M1 + M2) * g * sin(state[2])) / den2
    return dydx


# Creating time array from 0 to 0.1 sampled at 0.05 second steps
a = 0.0
b = 20
dt = 0.05
t = np.arange(a, b, dt)

# theta_1, theta_2 are the initial angles in degrees
# omega_1 and omega_2 are the initial angular velocities (degrees per second)

theta_1 = 120.0
omega_1 = 0.0
theta_2 = -10.0
omega_2 = 0.0

# Defining the initial state
state = np.radians([theta_1, omega_1, theta_2, omega_2])

# Solving the ODE using scipy.integrate
y = integrate.odeint(deriv, state, t)

x1 = L1 * sin(y[:, 0])
y1 = -L1 * cos(y[:, 0])

x2 = L2 * sin(y[:, 2]) + x1
y2 = -L2 * cos(y[:, 2]) + y1

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    this_x = [0, x1[i], x2[i]]
    this_y = [0, y1[i], y2[i]]

    line.set_data(this_x, this_y)
    time_text.set_text(time_template % (i * dt))
    return line, time_text


sim = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
                              interval=25, blit=True, init_func=init)

sim.save('double_pendulum_general.mp4', fps=15)
plt.show()
