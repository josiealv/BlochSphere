from bloch import animate_bloch_states, animate_multiple_bloch_states, plot_state_vectors
import sys
from qutip.states import basis

def get_single_plotanim_input():
    plot_type = input("Animation or Image? Enter 'anim' for animation or 'img' for image: ")
    arr_norm = []
    value = input("Enter complex numbers for alpha and beta (e.g. '1+2j' where '2j' represents the imaginary part) \n" + 
    "Type 'd' and 'enter' when you're done inputting your alpha(s) and beta(s): \n")
    while (value!='d'): # d for done
        arr_norm.append(value)
        value = input()
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
        filename = input("type in filename (without extension) e.g. 'test_file': ")
    else:
        print("Each state vector must have an alpha and a beta")
        return
    if(plot_type == 'anim'):
        file_type = input("type in file type (gif or mp4) e.g. 'gif': ")
        filename += '.' + file_type
        animate_bloch_states(complex_array, filename, file_type, duration=0.1, save_all=False)
    elif(plot_type == 'img'):
        plot_state_vectors(complex_array, filename)
    else:
        print("Please specify if plot is animation or image with: 'anim' or 'img', respectively\n")

def get_multiple_anim_input():
    numAnim = int(input ("Enter the number of animations you would like: \n"))
    arr_norm = []
    for i in range(numAnim):
        curr_arr_norm = []
        value = input("Enter complex numbers, alpha and beta, for animation " + str(i) + "\n" +
        "(e.g. '1+2j' where '2j' represents the imaginary part) \n" + 
        "Type 'd' and 'enter' when you're done inputting your alpha(s) and beta(s): \n")
        while (value!='d'): # d for done
            curr_arr_norm.append(value)
            value = input()
        arr_norm.append(curr_arr_norm)

    for j in range(numAnim): #check if any animations don't have sufficient alphas & betas
        if(len(arr_norm[j])%2!=0):
            print("Each state vector must have an alpha and a beta")
            return 
    complex_array = []
    for k in range(numAnim):
        curr_complex_array = []
        for l in range (0, len(arr_norm[k]), 2):
            curr_complex_array.append((complex(arr_norm[k][l]) * basis(2, 0) + complex(arr_norm[k][l + 1]) * basis(2, 1)))
        complex_array.append(curr_complex_array)
    filename = input("type in filename (without extension) e.g. 'test_file': ")
    file_type = input("type in file type (gif or mp4) e.g. 'gif': ")
    filename += '.' + file_type
    animate_multiple_bloch_states(complex_array, filename, file_type, numAnim)

def main():
     #                                      argv[0]  argv[1] 
     # to run command looks like >> Python3 main.py   s/m     
    if sys.argv[0] != "main.py":
        pass
    else:
        num_args = len(sys.argv)
        if num_args < 2:
            print("Not enough command line arguments.")
            return
        elif num_args > 2:
            print("Too many command line arguments.")
            return
        if (sys.argv[1] == 's'):
            get_single_plotanim_input()
        elif(sys.argv[1] == 'm'):
            get_multiple_anim_input()
        else:
            print("Invalid input: Please specify if you want a single animation/plot or multiple\n")
            print("Enter 's' for single or 'm' for multiple\n")
            return
main()