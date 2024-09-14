import tkinter as tk
from tkinter import ttk
import matplotlib
import numpy as np

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

import geargenplotcontrols
import geargenplot
import


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


def plot(frame):

    print("Printing the figure..")
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),dpi = 100)

    # list of squares
    y = [i**2 for i in range(101)]
    # adding the subplot
    plot1 = fig.add_subplot(111)
    # plotting the graph
    plot1.plot(y)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = frame)
    canvas.draw()
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,frame)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


def plot2(frame):
       # prepare data

        print("Printing the figure 2..")
        data = {'Python': 11.27,'C': 11.16,'Java': 10.46,'C++': 7.5,'C#': 5.26 }
        languages = data.keys()
        popularity = data.values()
        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)
        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, frame)
        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, frame)
        # create axes
        axes = figure.add_subplot()
        # create the barchart
        axes.bar(languages, popularity)
        axes.set_title('Top 5 Programming Languages')
        axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# Exteranl inputs ============================================
profilePath1 = "gear1.txt"
profilePath2 = "gear2.txt"

# Root =======================================================
root = tk.Tk()
root.title("Plotter Widget")
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=0)


# Plot frame ==================================================
plotFrame = ttk.Frame(root)
plotFrame.grid(row=0,column=0,sticky="NEWS")
gearPlot = geargenplot.GearGenPlot(plotFrame)


# Setting frame ===============================================
settingFrame = ttk.Labelframe(root,text="Plot Settings")
settingFrame.grid(row=0,column=1,sticky="NS")
controls = geargenplotcontrols.GearGenPlotControls(settingFrame,gearPlot)
# test = ttk.

root.mainloop()