import matplotlib as mpl
from pylab import *
from qutip import *
from matplotlib import cm
import imageio
from tkinter import Canvas, PhotoImage, Tk, mainloop
from math import cos, sin, pi
from PIL.Image import Image

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
    displayGif()

def displayGif():
    #gif_info = Image.open("bloch_anim.gif")   , format="gif -index %i",
    #frames = gif_info.n_frames
    window = Tk()
    window.title('Bloch Sphere')
    canvas = Canvas(window, width = 500, height = 500)
    canvas.pack()
    bloch_gif = PhotoImage(file = 'bloch_anim.gif', master=window)
    canvas.create_image(0, 0, image=bloch_gif, anchor = 'nw')
    window.mainloop()

states = []
thetas = linspace(0, pi, 21)
for theta in thetas:
    states.append((cos(theta / 2) * basis(2, 0) + sin(theta / 2) * basis(2, 1)).unit())
animate_bloch(states, duration=0.1, save_all=False)