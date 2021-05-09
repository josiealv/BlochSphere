from bloch import external_animate_bloch
import numpy as np

# length = 200  # uncomment if you also want to animate rabi oscillations with exponential decay example
length = 100    # uncomment if you want a single example aniamted (double check the bounds of the for loops)
betasR = [None] * length
alphasR = [None] * length
alphasI = [None] * length
betasI = [None] * length
omega = .05  # customize omega here
gamma = .01  # customize gamma here

# ---------------
#   For the file name, provide the absolute path and then the name of what you want it to be saved without an extension
#   Ex: /users/name/Desktop/{name_you_want}
#   Reminder: DO NOT ADD AN EXTENSION TO THE NAME (ie. {...}.gif)
#   If no relative path is provided, it will save to the directory in which the program is running in.
# ---------------
filename_no_extension = "test"
file_type = 'mp4'
phi = (np.pi * 3) / 4

# example 1 (exponential decay)
for i in range(0, 100):
    alphasR[i] = (np.cos(omega * i) * np.exp(-i * gamma))
    alphasI[i] = 0
    betasR[i] = (np.sin(omega * i) * np.exp(-i * gamma) * np.cos(phi))
    betasI[i] = (np.sin(omega * i) * np.exp(-i * gamma) * np.sin(phi))

# # # example 2 (Rabi oscillations)
# for i in range(100, 200):
#     alphasR[i] = (np.cos(omega * i))
#     alphasI[i] = 0
#     betasR[i] = (np.sin(omega * i))
#     betasI[i] = 0
external_animate_bloch(alphasR, alphasI, betasR, betasI, filename_no_extension, file_type)

