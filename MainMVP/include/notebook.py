import tkinter as tk
from tkinter import ttk 

from include.geompreprocui import GeomPreprocUI
from ui.plotter import Plotter
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


class HorizTabCollection(ttk.Frame):
    '''Class of widget containing the notebook with the tab of the GUI.'''

    def __init__(self,parent,presenter)->None:
        super().__init__(parent)
        '''Initialize the notebook widget of the application UI.'''

        # Set the grid configuration of this object
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        # Create tab notebook 
        self.tab_notebook = ttk.Notebook(self)
        self.tab_notebook.grid(row=0,column=0,sticky='NEWS')

        # Create the objects to put in the tabs
        self.plotter = Plotter(self.tab_notebook,presenter)
        self.geomPreproc = GeomPreprocUI(self.tab_notebook,presenter) 
        self.multics = ttk.Frame(self.tab_notebook)
        
        # Add the tabs (frame) to the notebook
        self.tab_notebook.add(self.plotter, text='Plotter')
        self.tab_notebook.add(self.geomPreproc, text='Geometrical Preprocessor')
        self.tab_notebook.add(self.multics, text='Multics')
        
        self.tab_notebook.pack(expand=1, fill="both")