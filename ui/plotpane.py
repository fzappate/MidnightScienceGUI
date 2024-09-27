import tkinter as tk
from tkinter import ttk 

# Important order of import
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk


class PlotPane(tk.Frame):
    '''Class of plot where the GearGen gear set is plot.'''

    def __init__(self,parent,*args, **kwargs)->None:
        super().__init__(parent,*args, **kwargs)
        '''Initialize the GearGen plot object.'''
        
        x = [1, 2, 3, 4]
        y1 = [1, 2, 3, 4]
        y2 = [4, 3, 2, 1]

        # Adjust rows and columns weight of PlotPane frame
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        # Create a figure
        self.figure = Figure( dpi=100, facecolor = 'cyan')
        
        # Create FigureCanvasTkAgg object
        self.canv = FigureCanvasTkAgg(self.figure, self)
        self.canv.get_tk_widget().config(bg= 'green')
        self.canv.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canv.draw() 

        # Create the toolbar
        NavigationToolbar2Tk(self.canv, self)

        # Create axes        
        self.ax = self.figure.add_subplot()
        self.ax.set_aspect('auto')
        
        self.ax.plot(x,y1)

        self.bind("<Configure>", lambda e: self.resize)
        
    
    # Uselesssss
    def resize(self,event):
        print("ciaooo")
        print(self.plotFrame.winfo_width(), self.plotFrame.winfo_height())
        ...
        
        
class GraphFrameContainer(tk.Frame):
    '''Class of plot where the GearGen gear set is plot.'''

    def __init__(self,parent,*args, **kwargs)->None:
        super().__init__(parent,*args, **kwargs)
        '''Initialize the GearGen plot object.'''
        
        x = [1, 2, 3, 4]
        y1 = [1, 2, 3, 4]
        
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.graphFrameList = []
        self.frame1 = GraphFrame(self)
        self.frame1.grid(row = 0, column=0,sticky='NEWS')
        


class GraphFrame(tk.Frame):
    '''Class of plot where the GearGen gear set is plot.'''

    def __init__(self,parent,*args, **kwargs)->None:
        super().__init__(parent,*args, **kwargs)
        '''Initialize the GearGen plot object.'''
        x = [1, 2, 3, 4]
        y1 = [1, 2, 3, 4]
        y2 = [-1, -2, -3, -4]
        
        
        self.fig, axs = plt.subplots(2)
        self.fig.suptitle('Vertically stacked subplots')
        axs[0].plot(x, y1)
        axs[0].plot()
        axs[1].plot(x, y2)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        
        
# class GraphFrame(tk.Frame):
#     '''Class of plot where the GearGen gear set is plot.'''

#     def __init__(self,parent,*args, **kwargs)->None:
#         super().__init__(parent,*args, **kwargs)
#         '''Initialize the GearGen plot object.'''
#         x = [1, 2, 3, 4]
#         y1 = [1, 2, 3, 4]
        
#         self.fig = Figure()
#         self.ax = self.fig.add_subplot(111)
#         self.ax.plot(x,y1)
#         self.canvas = FigureCanvasTkAgg(self.fig, master=self)
#         self.toolbar = NavigationToolbar2Tk(self.canvas, self)
#         self.toolbar.update()
#         self.toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
#         self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)





