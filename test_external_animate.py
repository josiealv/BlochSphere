from bloch import external_animate_bloch
import numpy as np

length = 200
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
file_no_extension = "test"
phi = (np.pi * 3) / 4

# example 1 (exponential decay)
for i in range(0, 100):
    alphasR[i] = (np.cos(omega * i) * np.exp(-i * gamma))
    alphasI[i] = 0
    betasR[i] = (np.sin(omega * i) * np.exp(-i * gamma) * np.cos(phi))
    betasI[i] = (np.sin(omega * i) * np.exp(-i * gamma) * np.sin(phi))

# # # example 2 (Rabi oscillations)
for i in range(100, 200):
    alphasR[i] = (np.cos(omega * i))
    alphasI[i] = 0
    betasR[i] = (np.sin(omega * i))
    betasI[i] = 0
external_animate_bloch(alphasR, alphasI, betasR, betasI, file_no_extension)

