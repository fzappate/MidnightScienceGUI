from tkinter import ttk 


from include.geompreprocplotcontrolsui import GeomPreprocPlotControlsUI
from include.geompreprocplotui import GeomPreprocPlotUI
from include.geargeninputsui import GearGenInputsUI
from include.geompreprocmodulesui import GeomPreprocModulesUI
from include.geompreproccontrolsui import GeomPreprocControlsUI

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


class GeomPreprocUI(ttk.Frame):
    def __init__(self,parent,presenter)->None:
        super().__init__(parent)
        '''Container of the whole geometrical preprocessor model.'''

        # Set the grid configuration of this object
        self.columnconfigure(0,weight=0)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=0)
        self.rowconfigure(0,weight=1)        

        # Plot panel
        self.plot = GeomPreprocPlotUI(self)
        self.plot.grid(row=0,column=1)   

        # Plot Controls panel
        self.plotControls = GeomPreprocPlotControlsUI(self,presenter,width = 280)
        self.plotControls.grid(row=0,column=2,sticky='NWS')

        # Input panel 
        self.geomPreprocTabs = GeomPreprocModulesUI(self,presenter,width = 330)
        self.geomPreprocTabs.grid(row=0,column=0,sticky='NES')
        
