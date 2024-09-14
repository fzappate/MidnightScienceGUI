import tkinter as tk
from tkinter import ttk

from include.geargenplotcontrolsui import GearGenPlotControlsUI
from include.geargenplotui import GearGenPlotUI
from include.geompreproccontrolsui import GeomPreprocControlsUI
from include.geargeninputsui import GearGenInputsUI


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


class GearGenUI(ttk.Frame):
    '''Class of widget containing the GearGen UI.'''

    def __init__(self,parent,presenter)->None:
        super().__init__(parent)
        '''Initialize the GearGen UI.'''

        # Set the grid configuration of this object
        self.columnconfigure(1,weight=1)
        self.rowconfigure(0,weight=1)        

        # Plot panel
        self.plot = GearGenPlotUI(self)
        self.plot.grid(row=0,column=1)   

        # Plot Controls panel
        self.plotControls = GearGenPlotControlsUI(self,presenter)
        self.plotControls.grid(row=0,column=2,sticky='N')

        # Input panel 
        self.inputsPanel = GearGenInputsUI(self,presenter)
        self.inputsPanel.grid(row=0,column=0,sticky='N')
        
        # Button panel
        self.buttonPanel = GeomPreprocControlsUI(self,presenter)
        self.buttonPanel.grid(row=1,column=0,sticky='S')
        