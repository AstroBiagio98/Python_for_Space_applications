'''
Problem Statement
----------------------
- We want to track the orbit of the earth around the Sun for a period of 1 year 
- Use Euler and Runge Kutta method of 4th order for this task
- Find the distance from Earth to Sun at the Apogee using Euler and RK4 methods and compare with the known distance

Equations
----------------------
Acceleration of Earth due to Gravity of the Sun
--> a = - (G*M/|r|^3)*r_vect (with r_vect = relative position of the Earth with reagrd to the Sun)

ODE for Position 
--> dr/dt = v

ODE for velocity 
--> dv/dt = a

Initial Condition
------------------------
Earth is at its Perihelion
'''


import matplotlib.pyplot as plt
import numpy as np

