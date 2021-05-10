from bloch import external_animate_bloch_multiple
import numpy as np

num_animations = 2 #number of animations for the gif/mp4 to generate
betasR = []
betasI = []
alphasR = [] 
alphasI = [] 
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

# example 1 (exponential decay)
betas_r = []
betas_i = []
alphas_r = [] 
alphas_i = [] 
for i in range(0, 100):
    alphas_r.append(np.cos(omega * i) * np.exp(-i * gamma))
    alphas_i.append(0)
    betas_r.append(np.sin(omega * i) * np.exp(-i * gamma) * np.cos(phi))
    betas_i.append(np.sin(omega * i) * np.exp(-i * gamma) * np.sin(phi))
alphasR.append(alphas_r)
alphasI.append(alphas_i)
betasR.append(betas_r)
betasI.append(betas_i)
# # # example 2 (Rabi oscillations)
betas_r2 = []
betas_i2 = []
alphas_r2 = [] 
alphas_i2 = [] 
for i in range(0, 75):
    alphas_r2.append(np.cos(omega * i))
    alphas_i2.append(0)
    betas_r2.append(np.sin(omega * i))
    betas_i2.append(0)
alphasR.append(alphas_r2)
alphasI.append(alphas_i2)
betasR.append(betas_r2)
betasI.append(betas_i2)
external_animate_bloch_multiple(num_animations, alphasR, alphasI, betasR, betasI, filename_no_extension, file_type)