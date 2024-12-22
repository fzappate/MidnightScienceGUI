import tkinter as tk
from tkinter import ttk 

# from ui.plotpane import PlotPane
from ui.PlotCanvas import PlotCanvas
from ui.ResFilePane import ResizableFrameRightEdgeScrollV
from ui.PlotManager import PlotManager
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


class PlotPane(tk.Frame):
    def __init__(self,parent,presenter,index,*args, **kwargs)->None:
        """
        Initialize Plotter. 
        This is a frame containing all the widgets necessary to plot results. 
        
        -----USAGE-----
        This widget can be used exactly as a frame. 
        """
        super().__init__(parent,*args, **kwargs)
        self.index = index

        # Set the grid configuration of this object
        self.rowconfigure(0,weight=1)        
        self.columnconfigure(0,weight=0)
        self.columnconfigure(1,weight=1)
        
        # Plot manager        
        self.plotManager = PlotManager(self,presenter,width=200)
        self.plotManager.grid(row=0,column=0,sticky='NEWS')
        
        # Plot frame
        self.plotCanvas=PlotCanvas(self)
        self.plotCanvas.grid(row=0,column=1, sticky='NEWS', padx=3, pady=3)      