import tkinter as tk
from tkinter import ttk 


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


class HorizTabCollection(tk.Frame):
    '''Class of widget containing the notebook with the tab of the GUI.'''

    def __init__(self,parent,presenter,*args, **kwargs)->None:
        super().__init__(parent,*args, **kwargs)
        '''Initialize the notebook widget of the application UI.'''

        # Set the grid configuration of this object
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        # Create tab notebook 
        self.plotNotebook = ttk.Notebook(self)

        # # Create the objects to put in the tabs
        # self.plotter = Plotter(self.tab_notebook,presenter, bg = 'red')
        # self.multics = tk.Frame(self.tab_notebook, bg = 'green')
        
        # # Add the tabs (frame) to the notebook
        # self.tab_notebook.add(self.plotter, text='Plotter',padding="3")
        # self.tab_notebook.add(self.multics, text='Multics',padding="3")
        
        self.plotNotebook.pack(expand=1, fill="both",padx=(3,3),pady=(2,2))