import argparse
from cmath import pi, sin, cos

import imageio
from pylab import *
from qutip import *

# to test: run "./command_line.py -i alpha -n time -n spacing
def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument("-i", "--input", help="Your input file.")
    parser.add_argument("-o", "--output", help="Your destination output file.")
    parser.add_argument("-n", "--num0", type=int, help="A number.")
    parser.add_argument("-n", "--num1", type=int, help="A number.")
    parser.add_argument("-v", "--verbose", dest='verbose', action='store_true', help="Verbose mode.")
    opts = parser.parse_args(args)

    return opts

options = getOptions(sys.argv[1:])

alpha = options.input
beta = options.output
spacing = options.num0
time = options.num1

items = [alpha, beta, spacing, time]

def animate_bloch(states, duration=0.1, save_all=False):
    #call get_input from parse
    #extract input from list and then put into respective variables
    for x in items:
        alpha = x[0]

    b = Bloch3d()
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
    #b.point_marker = ['o']
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


states = []
thetas = linspace(0, pi, 21)
for theta in thetas:
    states.append((cos(theta / 2) * basis(2, 0) + sin(theta / 2) * basis(2, 1)).unit())

animate_bloch(states, duration=0.1, save_all=False)
