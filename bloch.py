import sys
from cmath import pi, sin, cos
from math import atan2

import matplotlib as mpl
import imageio
from matplotlib import cm
import cv2
import numpy as np
from qutip import Bloch3d, basis, Bloch
import gui_gif
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
    # normalize colors to the length of data ##
    nrm = mpl.colors.Normalize(0, length)
    colors = cm.cool(nrm(range(length)))  # options: cool, summer, winter, autumn etc.
    # customize sphere properties ##
    b.point_color = list(colors)  # options: 'r', 'g', 'b' etc.
    b.point_marker = ['o']
    b.point_size = [30]
    b.add_states(states)
    b.save(save_file)

def animate_bloch_states(states, save_file, file_type, duration=0.1, save_all=False):
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

    if(file_type=='mp4'):
        imageio.mimsave(save_file, images, **kargs) # save images into mp4
        w, h, layers = images[0].shape # get dimensions of images
        fps = 0.5 # frames per second
        out = cv2.VideoWriter(save_file, -1, fps, (w, h)) # start creating the mp4
        for i in images:
            out.write(i) # 'writing' the images into the mp4
        cv2.destroyAllWindows() 
        out.release()
        # calling gui_mp4.py file -> passing in the mp4
        gui_mp4.main(save_file) 
    else:
        # saves list of images into a gif
        imageio.mimsave(save_file, images, duration=duration)
        # calling gui_gif.py file -> passing in the gif
        gui_gif.main(save_file)

def animate_multiple_bloch_states(vect_complex_arr, save_file, file_type, numV, duration=0.1, save_all=False):
    azimuthal = -40  # can customize to chang view of gif
    elevation = 20  # can customize to chang view of gif
    b = Bloch()
    b.view = [-40, 30]
    try:
        length = 0
        for i in range(numV): # number of frames will be max length of vectors amongst all animations 
            if (len(vect_complex_arr[i]) >= length):
                length = len(vect_complex_arr[i])
    except:
        length = 1
        states = [states]
    
    images = [None] * length  # setting length of images array to help decrease time gif/mp4 is created
    # normalize colors to the length of data ##
    nrm = mpl.colors.Normalize(0, length)
    b.point_marker = ['o']
    b.point_size = [30]
    for j in range(length):
        b.clear()
        curr_vect_complex_arr = [] #get all vectors for this frame
        for k in range (numV): 
            curr_vect_len = len(vect_complex_arr[k])
            if (j <= (curr_vect_len-1)):
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
            b.save(dirc='tmp')  # saving frames to tmp directory
            filename = "tmp/bloch_%01d.png" % j
        else:
            filename = 'temp_file.png'
            b.save(filename)
        images[j] = (imageio.imread(filename))  # combines all the images into one gif (one image)

    if(file_type=='mp4'):
        imageio.mimsave(save_file, images, **kargs) # save images into mp4
        w, h, layers = images[0].shape # get dimensions of images
        fps = 0.5 # frames per second
        out = cv2.VideoWriter(save_file, -1, fps, (w, h)) # start creating the mp4
        for i in images:
            out.write(i) # 'writing' the images into the mp4
        cv2.destroyAllWindows() 
        out.release()
        # calling gui_mp4.py file -> passing in the mp4
        gui_mp4.main(save_file) 
    else:
        # saves list of images into a gif
        imageio.mimsave(save_file, images, duration=duration)
        # calling gui_gif.py file -> passing in the gif
        gui_gif.main(save_file)

#creates the complex vector states for multiple animations
def external_animate_bloch_multiple(numV, alpha_reals, alpha_imags, beta_reals, beta_imags, filename, file_type):
    if(len(alpha_reals)!= numV): 
        print ("Number of state vectors does not equal amount inputted")
        return 
    if(len(alpha_reals)==len(beta_reals) and 
    len(alpha_imags)==len(beta_imags)):
        for i in range (0, len(alpha_reals)): # check if reals match
            if(len(alpha_reals[i])!=len(beta_reals[i])):
                print("Alphas and Betas do not match")
                return
        for j in range (0, len(alpha_imags)): # check if imaginaries match
            if(len(alpha_imags[j])!=len(beta_imags[j])):
                print("Alphas and Betas do not match")
                return
        # adding file extension (gif or mp4) to the filename 
        if(file_type=='gif' or file_type=='mp4'):
            filename += "." + file_type
        else:
            print("Invalid file type. Please specify 'gif' or 'mp4'")
            return

        vect_complex_arr = [] #2d vector to hold all vector animations      
        for j in range (0, numV):
            complex_arr = []
            for k in range (0, len(alpha_reals[j])):
                alpha = complex(alpha_reals[j][k], alpha_imags[j][k])
                beta = complex(beta_reals[j][k], beta_imags[j][k])
                # appending alpha and beta to complex_arr array
                complex_arr.append((alpha * basis(2, 0) + beta * basis(2, 1)))
            vect_complex_arr.append(complex_arr)
        animate_multiple_bloch_states (vect_complex_arr, filename, file_type, numV)
    else:
        print("Alphas and Betas do not match") 

# creates the complex vector states for a single animation
def external_animate_bloch(alpha_reals, alpha_imags, beta_reals, beta_imags, filename, file_type):
    if filename == "":
        print("Need to have a filename")
        return
    # checking that parameters are > 0
    if (len(alpha_reals) == len(beta_reals) and 
    len(alpha_imags) == len(beta_imags)) :
         # adding file extension (gif or mp4) to the filename 
        if(file_type=='gif' or file_type=='mp4'):
            filename += "." + file_type
        else:
            print("Invalid file type. Please specify 'gif' or 'mp4'")
            return
        complex_arr = []    # creating array that we will fill with alpha and beta
        for k in range(0, len(alpha_reals)):
            # converting alpha nad beta inputs to complex #s
            alpha = complex(alpha_reals[k], alpha_imags[k])
            beta = complex(beta_reals[k], beta_imags[k])
            # appending alpha and beta to complex_arr array
            complex_arr.append((alpha * basis(2, 0) + beta * basis(2, 1)))
        # calling function to create the bloch sphere gif
        animate_bloch_states(complex_arr, filename, file_type, duration=0.1, save_all=False)
    else:
        print("Alphas and Betas length do not match")
