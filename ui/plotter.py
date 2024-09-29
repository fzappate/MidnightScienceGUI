import tkinter as tk
from tkinter import ttk 

# from ui.plotpane import PlotPane
from ui.plotpane import PlotUI
from ui.resizableframe import ResizeScrollVFrameRightEdge
from ui.plotmanager import PlotManager
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


class Plotter(tk.Frame):
    def __init__(self,parent,presenter,*args, **kwargs)->None:
        """
        Initialize Plotter. 
        This is a frame containing all the widgets necessary to plot results. 
        
        -----USAGE-----
        This widget can be used exactly as a frame. 
        """
        super().__init__(parent,*args, **kwargs)

        # Set the grid configuration of this object
        self.columnconfigure(0,weight=0)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=0)
        self.rowconfigure(0,weight=1)        
        
        # Plot manager
        self.plotManagerPane = ResizeScrollVFrameRightEdge(self, width = 330,bg = 'cyan')
        self.plotManagerPane.grid(row=0,column=0,sticky='NES', padx=3, pady=3)
        
        self.plotManager = PlotManager(self.plotManagerPane.interior,presenter, bg = 'green')
        self.plotManager.grid(row=0,column=0,sticky='NEW')
        
        # Plot frame
        self.plot = PlotUI(self, bg = 'green')
        self.plot.grid(row=0,column=1, sticky='NEWS', padx=3, pady=3)      