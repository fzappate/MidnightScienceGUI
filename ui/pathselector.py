import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog

from presenter.presenter import Presenter


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


class PathSelector(tk.Frame):
    """ This object contains the graphical elements to select a working folder."""

    def __init__(self,parent,presenter:Presenter,*args, **kwargs):
        super().__init__(parent,*args, **kwargs)
        '''Initialize the path selector.'''

        # Set the grid configuration of this object
        self.columnconfigure(0,weight=0)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=0)

        # Draw the graphical interface of the path selector 
        self.lab = ttk.Label(self, text = 'Working Folder', width = 20)

        self.pathEntry = ttk.Entry(self)
        self.pathEntry.insert(0,presenter.model.settings.workingFolder)
        self.pathEntry.bind('<Return>', presenter.SetWorkingFolderManually)
        self.pathEntry.bind('<FocusOut>', presenter.SetWorkingFolderManually)

        self.navigate = ttk.Button(self, text="Browse..", command= lambda:presenter.BrowseProjectFolder())
        
        self.lab.grid(row=0, column=0, padx = (3,3))
        self.pathEntry.grid(row=0,column=1,sticky = "EW", padx = (3,3))
        self.navigate.grid(row=0, column=2, padx = (3,3))