from tkinter import ttk 
from tkinter import Label


from ui.signalselector import SignalSelectionFrame
from include.geompreprocplotui import GeomPreprocPlotUI
from ui.geompreprocplotcontrolsui import GeomPreprocPlotControlsUI

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


class Plotter(ttk.Frame):
    def __init__(self,parent,presenter)->None:
        super().__init__(parent)
        '''Container of the whole plotter.'''

        # Set the grid configuration of this object
        self.columnconfigure(0,weight=0)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=0)
        self.rowconfigure(0,weight=1)        
        
        # Signal selection 
        self.signalSelectorFrame = SignalSelectionFrame(self,presenter,width = 330)
        self.signalSelectorFrame.grid(row=0,column=0,sticky='NES')
        
        # Plot
        self.plot = ttk.Label(self,text = "Here goes the plot")
        self.plot.grid(row=0,column=1)  
        
        # Plot Controls panel
        self.plotControls = GeomPreprocPlotControlsUI(self,presenter,width = 280)
        self.plotControls.grid(row=0,column=2,sticky='NWS')