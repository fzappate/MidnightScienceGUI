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
        
class PlotUI(tk.Frame):
    '''Class of plot where the GearGen gear set is plot.'''

    def __init__(self,parent,*args, **kwargs)->None:
        '''Initialize the PlotUI object.'''
        super().__init__(parent,*args, **kwargs)
                
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        
        self.fig, axs = plt.subplots(1)
    
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        

        
        
    def AddSubplot(self,plotModel):
        '''
        Add a subplot to the plot.
        '''
        self.toolbar.destroy()
        self.canvas.get_tk_widget().destroy()
        
        # self.fig.
        self.fig, axList = plt.subplots(plotModel.noOfSubplots,1)
        x = [1, 2, 3, 4]
        y1 = [1, 2, 3, 4]
        
        if plotModel.noOfSubplots == 1:
            axList.plot(x,y1) 
        else:
            for ii in range(0,plotModel.noOfSubplots):
                axList[ii].plot(x,y1) 
            
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)





