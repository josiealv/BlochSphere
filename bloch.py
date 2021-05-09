import sys
from cmath import pi, sin, cos
from math import atan2

import matplotlib as mpl
import imageio
from matplotlib import cm
import cv2
import numpy as np
from qutip import Bloch3d, basis, Bloch
import gui
import gui_mp4

kargs = {'macro_block_size': None }

def plot_state_vectors (states, save_file): #no animation, just show an image of multiple state vectors on the bloch sphere
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

def animate_bloch_states(states, save_file, duration=0.1, save_all=False):
    azimuthal = -40  # can customize to change view of gif
    elevation = 20  # can customize to change view of gif
    print("file name: %s" % save_file)  # printing out inputted file name in the terminal
    b = Bloch()  # creating bloch object
    b.vector_color = ['r']
    b.view = [azimuthal, elevation]  # setting view of vector in sphere
    try:
        length = len(states)  # getting length of vectors
    except:
        length = 1  # sets length of vector to 1 if not a valid length
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
    imageio.mimsave(save_file, images, **kargs)
    # calling gui.py file -> passing in the gif
    # gui.main(save_file)
    w, h, layers = images[0].shape
    fps = 0.5
    out = cv2.VideoWriter(save_file, -1, fps, (w, h))

    for i in images:
        out.write(i)
    cv2.destroyAllWindows()
    out.release()
    gui_mp4.main(save_file)

    # saves list of images into a gif
    # imageio.mimsave(save_file, images, duration=duration)

    # convert gif to mp4
    # clip = mp.VideoFileClip(save_file)
    # clip.write_videofile(save_file + ".mp4")

def animate_multiple_states(vect_complex_arr, save_file, numV, duration=0.1, save_all=False):
    azimuthal = -40  # can customize to chang view of gif
    elevation = 20  # can customize to chang view of gif
    b = Bloch()
    b.view = [-40, 30]
    try:
        length = 0
        for i in range(len(vect_complex_arr)): # number of frames are gonna be max length of vectors amongst all animations 
            if (len(vect_complex_arr[i]) >= length):
                length = len(vect_complex_arr[i])
    except:
        length = 1
        states = [states]
    
    images = [None] * length  # setting length of images array to help decrease time gif is created
    # normalize colors to the length of data ##
    nrm = mpl.colors.Normalize(0, length)
    # colors = cm.cool(nrm(range(length)))  # options: cool, summer, winter, autumn etc.
    # customize sphere properties ##
    # b.point_color = list(colors)  # options: 'r', 'g', 'b' etc.
    b.point_marker = ['o']
    b.point_size = [30]

    for j in range(length):
        b.clear()
        curr_vect_complex_arr = [] #get all vectors for this frame
        for k in range (numV): 
            curr_vect_len = len(vect_complex_arr[k])
            if (j < curr_vect_len):
                curr_vect_complex_arr.append(vect_complex_arr[k][j])
            else:
                curr_vect_complex_arr.append(vect_complex_arr[k][curr_vect_len-1]) #animation for current vector done, make it static
        b.add_states(curr_vect_complex_arr) #add all state vectors to bloch animation
        
        for l in range (numV): #add points for each state vector
            curr_vect_len = len(vect_complex_arr[l])
            temp_point_arr = []
            if (j < curr_vect_len):
                temp_point_arr.append(vect_complex_arr[l][:(j + 1)])
            else:
                temp_point_arr.append(vect_complex_arr[l][:((curr_vect_len-1)+1)])
            b.add_states(temp_point_arr, 'point')
        
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

def external_animate_bloch_multiple(numV, alpha_reals, alpha_imags, beta_reals, beta_imags, filename):
    if(len(alpha_reals)!= numV):
        print ("Number of state vectors does not equal amount inputted")
        return 
    if(len(alpha_reals)==len(beta_reals)):
        for i in range (0, len(alpha_reals)):
            if(len(alpha_reals[i])!=len(beta_reals[i])):
                print("Alphas and Betas do not match")
                return
        filename += ".gif"
        vect_complex_arr = [] #2d vector to hold all vector animations      
        for j in range (0, numV):
            complex_arr = []
            for k in range (0, len(alpha_reals[j])):
                alpha = complex(alpha_reals[j][k], alpha_imags[j][k])
                beta = complex(beta_reals[j][k], beta_imags[j][k])
                # appending alpha and beta to complex_arr array
                complex_arr.append((alpha * basis(2, 0) + beta * basis(2, 1)))
            vect_complex_arr.append(complex_arr)
        animate_multiple_states (vect_complex_arr, filename, numV)
    else:
        print("Alphas and Betas do not match") 

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
        filename += ".mp4"
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
                filename = input("type in filename (without extension) e.g. 'test_file' ") + ".gif"
                animate_bloch_states(complex_array, filename, duration=0.1, save_all=False)
            else:
                print("Each state vector must have an alpha and a beta")

main()
