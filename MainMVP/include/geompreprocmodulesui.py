from tkinter import ttk
from include.geargenmoduleui import GearGenModuleUI
from include.geomcodemoduleui import GeomCodeModuleUI
from include.resizableframe import ResizableFrameRightEdge 

class GeomPreprocModulesUI(ResizableFrameRightEdge):
    def __init__(self,parent,presenter, *args, **kwargs)->None:
        super().__init__(parent,*args, **kwargs)
        '''Object that contains a notebook with the modules of the geometrical preprocessor. '''

        # Make sure that the content of GeomPreprocModulesUI stretches from left to right
        self.columnconfigure(0,weight=0)
        # Make sure that the content of GeomPreprocModulesUI stretches from top to bottom
        self.rowconfigure(0, weight=1)


        # Create tab notebook 
        self.tab_notebook = ttk.Notebook(self)

        # Create modules object
        self.gearGenInputs = GearGenModuleUI(self.tab_notebook,presenter)
        self.geomCodeInputs = GeomCodeModuleUI(self.tab_notebook,presenter)

        self.tab_notebook.add(self.gearGenInputs, text='Gear Generator')
        self.tab_notebook.add(self.geomCodeInputs, text='Geometry Code')

        self.tab_notebook.pack(expand=1, fill="both",padx=(0,5))