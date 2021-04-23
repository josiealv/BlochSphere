import sys
from cmath import pi, sin, cos
from math import atan2

import matplotlib as mpl
import imageio
from matplotlib import cm
import numpy as np
from qutip import Bloch3d, basis, Bloch

num_args = len(sys.argv)
comp_input = 0

def animate_bloch_states(states, duration=0.1, save_all=False):
    b = Bloch()
    b.vector_color = ['r']
    b.view = [-40, 30]
    images = []
    try:
        length = len(states)
    except:
        length = 1
        states = [states]
    # normalize colors to the length of data ##
    nrm = mpl.colors.Normalize(0, length)
    colors = cm.cool(nrm(range(length)))  # options: cool, summer, winter, autumn etc.

    # customize sphere properties ##
    b.point_color = list(colors)  # options: 'r', 'g', 'b' etc.
    b.point_marker = ['o']
    b.point_size = [30]

    for j in range(length):
        b.clear()
        b.add_states(states[j])
        b.add_states(states[:(j+1)], 'point')
        if save_all:
            b.save(dirc='tmp')  # saving images to tmp directory
            filename = "tmp/bloch_%01d.png" % j
        else:
            filename = 'temp_file.png'
            b.save(filename)
        images.append(imageio.imread(filename))
    imageio.mimsave('bloch_anim.gif', images, duration=duration)

def external_animate_bloch(alphas, betas, duration=0.1, save_all=False):
    if(len(alphas)==len(betas)):
        complex_arr=[]
        for i in range(0, len(alphas)):
           complex_arr.append((complex(alphas[i])*basis(2, 0) + complex(betas[i]) * basis(2, 1)).unit())
        animate_bloch_states(complex_arr, duration=0.1, save_all=False)
    else:
        print("Alphas and Betas length do not match")

if "-s" in sys.argv:
    arr_norm = sys.argv[2].split(",")  # to run command looks like >> Python3 bloch.py -v [list of vectors]
    if len(arr_norm)%2==0: 
        complex_arr=[]
        for i in range(0, len(arr_norm), 2):
            complex_arr.append((complex(arr_norm[i])*basis(2, 0) + complex(arr_norm[i+1]) * basis(2, 1)).unit())
        animate_bloch_states(complex_arr, duration=0.1, save_all=False)
    else:
        print("Each state vector must have an alpha and a beta")
elif "-c" in sys.argv:        # to run command looks like >> Python3 bloch.py -c alpha+betaj
    comp_input = complex(sys.argv[2])
    animate_bloch_states(comp_input, duration=0.1, save_all=False)

# #   state vectors
# if comp_input == 0:
#     states = []
#     thetas = np.linspace(0, pi, 21)
#     for theta in thetas:
#         states.append((cos(theta / 2) * basis(2, 0) + sin(theta / 2) * basis(2, 1)).unit())
#
#     animate_bloch(states, duration=0.1, save_all=False)
#
# else: #  use alpha and beta to get thetas -> plug in range for states vectors
#     alpha = comp_input.real
#     print(alpha)
#     beta = comp_input.imag
#     print(beta)
#     r = np.sqrt(abs(alpha)*abs(alpha) + abs(beta)*abs(beta))
#    # theta = np.linspace(0, np.arccos(2*(alpha), 21))
#     # phi = numpy.arctan(2(beta.imag / alpha)) #need to get imaginary of beta
#
#     states = []
#     print(np.arccos(2(alpha)))
#     theta = np.radians(np.arccos(2(alpha)))
#     # for theta in thetas:
#     states.append((np.cos(theta / 2) * basis(2, 0) + np.sin(theta / 2) * basis(2, 1)).unit())
#
#     animate_bloch(states, duration=0.1, save_all=False)