import sys
from cmath import pi, sin, cos
from math import atan2

import matplotlib as mpl
import imageio
from matplotlib import cm
import numpy as np
from qutip import Bloch3d, basis, Bloch
import gui

def animate_bloch_states(states, save_file, duration=0.1, save_all=False):
    b = Bloch()
    b.vector_color = ['r']
    b.view = [-40, 30]
    try:
        length = len(states)
    except:
        length = 1
        states = [states]
    
    images = [None] * length  # setting length of images array to help decrease time gif is created
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
        images[j] = (imageio.imread(filename))  # combines all the images into one gif (one image)
    imageio.mimsave(save_file, images, duration=duration)
    # calling gui.py file -> passing in the gif
    gui.main(save_file)

def plot_state_vectors (states, save_file):
    save_file += '.png'
    b = Bloch()
    b.view = [-40, 30]
    try:
        length = len(states)
    except:
        length = 1
        states = [states]
    
    images = [None] * length  # setting length of images array to help decrease time gif is created
    # normalize colors to the length of data ##
    nrm = mpl.colors.Normalize(0, length)
    colors = cm.cool(nrm(range(length)))  # options: cool, summer, winter, autumn etc.
    # customize sphere properties ##
    b.point_color = list(colors)  # options: 'r', 'g', 'b' etc.
    b.point_marker = ['o']
    b.point_size = [30]
    b.add_states(states)
    b.save(save_file)

def animate_multiple_states(vect_complex_arr, save_file, numV, duration=0.1, save_all=False):
    azimuthal = -40  # can customize to chang view of gif
    elevation = 20  # can customize to chang view of gif
    bloch_obj = []
    for i in range(0, numV):
        bloch_obj[i] = Bloch()
    

    # customize sphere properties ##
    # b.point_color = list(colors)  # options: 'r', 'g', 'b' etc.
    # b.point_marker = ['o']
    # b.point_size = [30]

def external_animate_bloch_multiple(numV, alpha_reals, alpha_imags, beta_reals, beta_imags, filename):
    if(len(alpha_reals)!= numV):
        print ("Number of state vectors does not equal amount inputted")
        return 
    if(len(alpha_reals)==len(beta_reals)):
        for i in range (0, len(alpha_reals)):
            if(len(alpha_reals[i])!=len(beta_reals[i])):
                print("Alphas and Betas length do not match")
                return
        filename += ".gif"
        vect_complex_arr = []      
        for j in range (0, numV):
            complex_arr = []
            for k in range (0, len(alpha_reals[j])):
                alpha = complex(alpha_reals[j][k], alpha_imags[j][k])
                beta = complex(beta_reals[j][k], beta_imags[j][k])
                # appending alpha and beta to complex_arr array
                complex_arr.append((alpha * basis(2, 0) + beta * basis(2, 1)))
            vect_complex_arr.append(complex_arr)
        animate_multiple_states (filename, numV, vect_complex_arr)
    else:
        print("Alphas and Betas length do not match")

def external_animate_bloch(alpha_reals, alpha_imags, beta_reals, beta_imags, filename):
    if filename == "":
        print("Need to have a filename")
        return
    # checking that parameters are > 0
    if (len(alpha_reals) == len(beta_reals)) and len(alpha_imags) == len(beta_imags):
        complex_arr = []    # creating array that we will fill with alpha and beta
        for k in range(0, len(alpha_reals)):
            # converting alpha nad beta inputs to complex #s
            alpha = complex(alpha_reals[k], alpha_imags[k])
            beta = complex(beta_reals[k], beta_imags[k])
            # appending alpha and beta to complex_arr array
            complex_arr.append((alpha * basis(2, 0) + beta * basis(2, 1)))
        # adding file extension to the filename
        filename += ".gif"
        # calling function to create the bloch sphere gif
        animate_bloch_states(complex_arr, filename, duration=0.1, save_all=False)
    else:
        print("Alphas and Betas length do not match")

def main():
    # if else statements are checking command line arguments are valid
    if sys.argv[0] != "bloch.py":
        pass
    else:
        num_args = len(sys.argv)
        if num_args < 2:
            print("Not enough command line arguments.")
        elif num_args > 2:
            print("Too many command line arguments.")
        else:
            #                                       argv[0]    argv[1]
            # to run command looks like >> Python3 bloch.py [list of vectors]
            # splitting each vector by the ","
            arr_norm = sys.argv[1].split(",")
            # making sure there are an alpha and a beta per vector inputs (so length of array needs to be divisible
            # by 2)
            if len(arr_norm) % 2 == 0:
                complex_array = []
                #   for each vector input:
                #   1)  converting alpha/beta to complex and calculating the xy points for the bloch sphere
                #   2)  appending to array
                #   3)  calling function to create the bloch sphere gif
                for i in range(0, len(arr_norm), 2):
                    complex_array.append((complex(arr_norm[i]) * basis(2, 0) + complex(arr_norm[i + 1]) * basis(2, 1)))
                filename = input("type in filename (without extension) e.g. 'test_file' ") # + ".gif"
                #animate_bloch_states(complex_array, filename, duration=0.1, save_all=False)
                # plot_state_vectors(complex_array, filename)
            else:
                print("Each state vector must have an alpha and a beta")

main()
