from numpy import sin, cos, pi, array
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

# Equations of motion for the double pendulum
# Constants
g = 9.81
m_1 = 2
m_2 = 2
theta_1 = pi
theta_2 = 0
l_1 = 1
l_2 = 1
omega_1 = 1
omega_2 = 1


omega_prime_1_top = -g*(2*m_1 + m_2)*sin(theta_1) - m_2*g*sin(theta_1 - 2*theta_2) - 2*sin(theta_1 - theta_2)*m_2 * \
                    (omega_2**2 * l_2 + omega_1**2 * l_1 * cos(theta_1 - theta_2))

omega_prime_1_bottom = l_1 * (2*m_1 + m_2 - m_2*cos(2*theta_1-2*theta_2))

omega_prime_1 = omega_prime_1_top / omega_prime_1_bottom

omega_prime_2_top = 2*sin(theta_1 - theta_2) * ( omega_1**2 * l_1 * (m_1 + m_2) + g*(m_1 + m_2) * cos(theta_1) +
                                                 omega_2**2 * l_2 * m_2 * cos(theta_1 - theta_2))

omega_prime_2_bottom = l_2 * (2*m_1 + m_2 - m_2*cos(2*theta_1 - 2*theta_2))

omega_prime_2 = omega_prime_2_top / omega_prime_2_bottom
