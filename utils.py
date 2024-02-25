from qutip.states import basis
import imageio
import cv2
import gui_gif
import gui_mp4

kargs = {'macro_block_size': None }
def create_open_mp4(images, save_file):
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

def create_open_gif(images, save_file, duration):
    # saves list of images into a gif
    imageio.mimsave(save_file, images, duration=duration)
    # calling gui_gif.py file -> passing in the gif
    gui_gif.main(save_file)

#   for each vector input:
#   1)  converting alpha/beta to complex and calculating the xy points for the bloch sphere
#   2)  appending to array
def getQuantumStates(numQuantumStates):
    complex_array = []
    for i in range (0, numQuantumStates):
        print(f"Inputs for Quantum State #{i+1}:\n")
        alpha = 0
        beta = 0
        complexAlpha = input("Is alpha a complex number? Enter 'y' or 'n' \n")
        if (complexAlpha == 'y'):
            alphaR = int(input("Enter real part of alpha: \n"))
            alphaI = int(input("Enter imaginary part of alpha \n"))
            alpha = complex(alphaR, alphaI)
        else:
            alphaR = int(input("Enter a real number for alpha (i.e. an int): \n"))
            alpha = complex(alphaR)

        complexBeta = input("Is beta a complex number? Enter 'y' or 'n' \n")
        if (complexBeta == 'y'):
            betaR = int(input("Enter real part of beta: \n"))
            betaI = int(input ("Enter imaginary part of beta \n"))
            beta = complex(betaR, betaI)
        else:
            betaR = int(input("Enter a real number for beta (i.e. an int): \n"))
            beta = complex(betaR)
        complex_array.append(alpha * basis(2, 0) + beta * basis(2, 1))
    return complex_array
        