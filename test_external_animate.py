import bloch as b
import numpy as np

betasR = []
alphasR = []
alphasI = []
betasI = []
omega = .05
gamma = .01
file_no_extension = "test"
phi = (np.pi * 3) / 4
for i in range(0, 100):
    alphasR.append((np.cos(omega*i)*np.exp(-i*gamma)))
    alphasI.append(0)
    betasR.append((np.sin(omega*i)*np.exp(-i*gamma)*np.cos(phi)))
    betasI.append((np.sin(omega*i)*np.exp(-i*gamma)*np.sin(phi)))
b.external_animate_bloch(alphasR, alphasI, betasR, betasI, file_no_extension)
