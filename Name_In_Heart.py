import matplotlib.pyplot as plt
from Plot_Anim import Plot
from Alphabets import AlphabetsGraphics
import numpy as np
from PIL import Image  # Import Image module from Pillow

def Plot_Name(Name, Name2 = None, xshift = 0.9, yshift= 1.2, xshift2 = 1.2, yshift2=0.1, OuterHeartScale=1, heart=False):
    fig, ax = plt.subplots()

    X = np.linspace(-2, 2, 100000)
    Alpha_X = np.linspace(0, 1, 50)

    f = lambda x, a: abs(x)**(2/3) + ((np.e/3) * ((np.pi - x**2)**0.5) * np.sin(a*np.pi*abs(x))) * abs(x)/x

    shift = 4
    heartScale = lambda x : 3*x*OuterHeartScale
    graphs = []

    graphs.append(Plot(fig, ax, X, "black", f, Transform=lambda x : 1.05*heartScale(x), xshift = shift, intervals=100, frames = 70))
    graphs.append(Plot(fig, ax, X, "red", f, Transform=heartScale, xshift = shift, intervals=20, frames = 70))
    graphs.append(Plot(fig, ax, X, "blue", f, Transform=lambda x : 0.96*heartScale(x), xshift = shift, intervals=20, frames = 70))
    graphs.append(Plot(fig, ax, X, "white", f, Transform=lambda x : 0.93*heartScale(x), xshift = shift, intervals=20, frames = 70))

    colors = ["black", "green", "red", "orange", "blue"]
    colors2 = ["green", "blue", "orange", "red", "black"]
    alp = AlphabetsGraphics()
    delay = 50
    delay_h = 70
    for i in range(len(Name)):
        graphs.append(Plot(fig, ax, Alpha_X, colors[i%len(colors)], alp.get(Name[i]), True, frames= 70, intervals=20, x_update=True, y_update=False, xshift=xshift, yshift=yshift, delay = delay))
        xshift += 1.1
    if Name2 != None:
        if heart:
            graphs.append(Plot(fig, ax, X, "black", f, Transform=lambda x: 0.55*x, xshift = shift, yshift=1.5, intervals=120, frames = 100, delay=delay_h))
            graphs.append(Plot(fig, ax, X, "#F00000", f, Transform=lambda x: 0.51*x, xshift = shift, yshift=1.5, intervals=120, frames = 100, delay=delay_h))
        for i in range(len(Name2)):
            graphs.append(Plot(fig, ax, Alpha_X, colors2[-i%len(colors)-1], alp.get(Name2[i]), True, frames= 70, intervals=20, x_update=True, y_update=False, xshift=xshift2, yshift=yshift2, delay = delay))
            xshift2 += 1.1
    
# Save the animations as frames
    frames = []
    for i in range(100):
        for ele in graphs:
            ele[1](i)
        fig.canvas.draw()
        img = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
        img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        frames.append(Image.fromarray(img))  # Convert numpy array to Image object

    # Create a GIF from the frames using Pillow
    gif_filename = 'animations.gif'
    frames[0].save(gif_filename, save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)
    # plt.show()