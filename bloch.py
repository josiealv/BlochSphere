import sys
from cmath import pi, sin, cos
from math import atan2

import matplotlib as mpl
import imageio
from matplotlib import cm
import numpy
from qutip import Bloch3d, basis, Bloch

num_args = len(sys.argv)
comp_input = 0

if "-v" in sys.argv:
    vectors = sys.argv[3]  # to run command looks like >> Python3 bloch.py -v [list of vectors]
if "-c" in sys.argv:        # to run command looks like >> Python3 bloch.py -c alpha+betaj
    comp_input = complex(sys.argv[3])

def animate_bloch(states, duration=0.1, save_all=False):
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

    for i in range(length):
        b.clear()
        b.add_states(states[i])
        b.add_states(states[:(i + 1)], 'point')
        if save_all:
            b.save(dirc='tmp')  # saving images to tmp directory
            filename = "tmp/bloch_%01d.png" % i
        else:
            filename = 'temp_file.png'
            b.save(filename)
        images.append(imageio.imread(filename))
    imageio.mimsave('bloch_anim.gif', images, duration=duration)

#   state vectors
if comp_input == 0:
    states = []
    thetas = numpy.linspace(0, pi, 21)
    for theta in thetas:
        states.append((cos(theta / 2) * basis(2, 0) + sin(theta / 2) * basis(2, 1)).unit())

    animate_bloch(states, duration=0.1, save_all=False)

else: #  use alpha and beta to get thetas -> plug in range for states vectors
    alpha = comp_input.real
    beta = comp_input.imag
    r = numpy.sqrt(abs(alpha)*abs(alpha) + abs(beta)*abs(beta))
    theta = numpy.arccos2(alpha)
    phi = numpy.arctan2(beta / alpha) #need to get imaginary of beta

    states = []
    # thetas = numpy.linspace(0, pi, 21)
    # for theta in thetas:
    states.append((cos(theta / 2) * basis(2, 0) + sin(theta / 2) * basis(2, 1)).unit())

    animate_bloch(states, duration=0.1, save_all=False)