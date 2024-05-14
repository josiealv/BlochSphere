from bloch import external_animate_bloch_multiple
import numpy as np

from coefficients import Coefficients

num_animations = 2 #number of animations for the gif/mp4 to generate
omega = .05  # customize omega here
gamma = .01  # customize gamma here
phi = (np.pi * 3) / 4
# ---------------
#   For the file name, provide the absolute path and then the name of what you want it to be saved without an extension
#   Ex: /users/name/Desktop/{name_you_want}
#   Reminder: DO NOT ADD AN EXTENSION TO THE NAME (ie. {...}.gif)
#   If no relative path is provided, it will save to the directory in which the program is running in.
# ---------------
filename_no_extension = "test_multiple"
file_type = 'mp4'
animations_arr = []

# example 1 (exponential decay)
coefficients_arr1 = []
for i in range(0, 100):
    alpha = complex((np.cos(omega * i) * np.exp(-i * gamma)), 0)
    beta = complex((np.sin(omega * i) * np.exp(-i * gamma) * np.cos(phi)), 
                                                  (np.sin(omega * i) * np.exp(-i * gamma) * np.sin(phi)))
    coefficients_arr1.append(Coefficients(alpha, beta))
animations_arr.append(coefficients_arr1)

# example 2 (rabbi oscillation)
coefficients_arr2 = []
for i in range(0, 75):
    coefficients_arr2.append(Coefficients(complex((np.cos(omega * i)), 0), complex((np.sin(omega * i)), 0)))

animations_arr.append(coefficients_arr2)

external_animate_bloch_multiple(num_animations, animations_arr, filename_no_extension, file_type)