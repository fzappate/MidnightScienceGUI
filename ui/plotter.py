import tkinter as tk
from tkinter import ttk 


from ui.plotmanager import PlotManagerPane
from ui.plotpane import PlotPane
from ui.plotpane import GraphFrameContainer
from ui.geompreprocplotcontrolsui import GeomPreprocPlotControlsUI

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


class Plotter(tk.Frame):
    def __init__(self,parent,presenter,*args, **kwargs)->None:
        super().__init__(parent,*args, **kwargs)
        '''Container of the whole plotter.'''

        # Set the grid configuration of this object
        self.columnconfigure(0,weight=0)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=0)
        self.rowconfigure(0,weight=1)        
        
        # Signal selection 
        self.plotManagerPane = PlotManagerPane(self,presenter,width = 330,bg = 'gray30')
        self.plotManagerPane.grid(row=0,column=0,sticky='NES', padx=3, pady=3)
        
        # Plot
        # self.plot = PlotPane(self, bg = 'green')
        self.plot = GraphFrameContainer(self, bg = 'green')
        self.plot.grid(row=0,column=1, sticky='NEWS', padx=3, pady=3)      