import sys
from cmath import pi, sin, cos
from math import atan2

import matplotlib as mpl
import imageio
from matplotlib import cm
import numpy as np
from qutip import Bloch3d, basis, Bloch
import gui

num_args = len(sys.argv)
comp_input = 0


def animate_bloch_states(states, save_file, duration=0.1, save_all=False):
    print("file name: %s" % save_file)
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
        b.add_states(states[:(j + 1)], 'point')
        if save_all:
            b.save(dirc='tmp')  # saving images to tmp directory
            filename = "tmp/bloch_%01d.png" % j
        else:
            filename = 'temp_file.png'
            b.save(filename)
        images.append(imageio.imread(filename))
    imageio.mimsave(save_file, images, duration=duration)

    gui.main(save_file)


def external_animate_bloch(alpha_reals, alpha_imags, beta_reals, beta_imags, filename):
    if filename == "":
        print("Need to have a filename")
        return
    if (len(alpha_reals) == len(beta_reals)) and len(alpha_imags) == len(beta_imags):
        complex_arr = []
        for k in range(0, len(alpha_reals)):
            alpha = complex(alpha_reals[k], alpha_imags[k])
            beta = complex(beta_reals[k], beta_imags[k])
            complex_arr.append((alpha * basis(2, 0) + beta * basis(2, 1)))
        filename += ".gif"
        animate_bloch_states(complex_arr, filename, duration=0.1, save_all=False)
    else:
        print("Alphas and Betas length do not match")


if "-s" in sys.argv:
    arr_norm = sys.argv[2].split(",")  # to run command looks like >> Python3 bloch.py -v [list of vectors]
    if len(arr_norm) % 2 == 0:
        complex_array = []
        for i in range(0, len(arr_norm), 2):
            complex_array.append((complex(arr_norm[i]) * basis(2, 0) + complex(arr_norm[i + 1]) * basis(2, 1)))
        animate_bloch_states(complex_array, duration=0.1, save_all=False)
    else:
        print("Each state vector must have an alpha and a beta")

# elif "-c" in sys.argv:  # to run command looks like >> Python3 bloch.py -c alpha+betaj
#     comp_input = complex(sys.argv[2])
#     animate_bloch_states(comp_input, duration=0.1, save_all=False)
