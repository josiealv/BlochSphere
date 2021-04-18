

# from PIL import Image
#
# canvas = Image.new("RGB", (500, 500), "white")
# gif = Image.open('bloch_anim.gif', 'r')
# frames = []
#
# try:
#     while 1:
#         frames.append(gif.copy())
#         gif.seek(len(frames))
# except EOFError:
#     pass
#
# for frame in frames:
#     canvas.paste(frame)
#     canvas.show()


import ffmpy
gif_input = 'bloch_anim.gif'

ff = ffmpy.FFmpeg(
    inputs={gif_input: None},
    outputs={'output.mp4': None}
)
ff.run()
