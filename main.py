from bloch import animate_bloch_states, animate_multiple_bloch_states, plot_state_vectors
import sys
from qutip.states import basis
from utils import getQuantumStates

def get_single_plotanim_input():
    numQuantumStates = int(input("Enter number of Quantum States being plotted: \n"))
    complex_array = getQuantumStates(numQuantumStates)

    if complex_array:
        # Getting filename 
        filename = input("type in filename (without extension) e.g. 'test_file': ")
    else:
        raise Exception("A problem occurred when generating Quantum State vectors! Ending program...")
    
    plot_type = input("Animation or Image? Enter 'anim' for animation or 'img' for image: ")

    # Get file type and generate name of file before calling plotting function
    if(plot_type == 'anim'):
        file_type = input("type in file type (gif or mp4) e.g. 'gif': ")
        filename += '.' + file_type
        animate_bloch_states(complex_array, filename, file_type)
    elif(plot_type == 'img'):
        plot_state_vectors(complex_array, filename)
    else:
        raise Exception("Plot type must be specified to continue. Ending program... \n")

def get_multiple_anim_input():
    numAnim = int(input ("Enter the number of animations you would like: \n"))
    arr_norm = []
    for i in range(numAnim):
        curr_arr_norm = []
        value = input("Enter coefficents: alpha and beta (where alpha and beta are real numbers), for animation " + str(i) + "\n" +
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