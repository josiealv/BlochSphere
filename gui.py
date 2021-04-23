from tkinter import *
from PIL import Image
import time
import os

gif = Image.open('bloch_anim.gif', 'r')
frames = []

try:
    while 1:
        frames.append(gif.copy())
        gif.seek(len(frames))
except EOFError:
    pass

root = Tk()
root.title("Bloch Sphere")
frameCnt = len(frames)
frames = [PhotoImage(file='bloch_anim.gif', format='gif -index %i' %(i)) for i in range(frameCnt)]


def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)


label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()


