import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt

def Plot(fig, ax, X, color, func, coordinates=False, x_update=False, y_update=True, frames=100, intervals=20, alphaFunc=lambda x: x/20, Transform=None, xshift=0, yshift=0, delay=0, test=False):
    # Initialize the lines (empty for now)
    line1, = ax.plot([], [], color=color)
    alpha = 0
    # Function to update the first pattern
    plt.xticks([])
    plt.yticks([])
    for spine in plt.gca().spines.values():
        spine.set_visible(False)
    def update1(frame):
        nonlocal alpha
        if x_update:
            tempFramesx = frames-delay
            Framex = max(0, (frame + 1-delay)*100//tempFramesx)
            x_data = X[:int(len(X)*(Framex/100))]
        else:
            x_data = X 
        if y_update:
            tempFramesy = frames-delay
            Framey = max(0, (frame + 1-delay)*100//tempFramesy)
            alpha += alphaFunc(Framey) if alphaFunc != None else Framey
            y_data = func(x_data, alpha) if alpha else func(x_data, np.nan)
        else:
            y_data = func(x_data)
        if coordinates:
            x_data, y_data = func(x_data)
        line1.set_data(xshift+Transform(x_data) if Transform != None else xshift +
                       x_data, Transform(y_data) + yshift if Transform != None else yshift+y_data)
        ax.relim()
        ax.autoscale_view()
        return line1,
    # Set animation parameters for the first animation
    ani = animation.FuncAnimation(
        fig, update1, frames=frames, interval=intervals, blit=False, repeat=False, cache_frame_data=False)
    return ani, update1
