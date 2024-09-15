import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog

from presenter.presenter import Presenter


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


class FileSelector(ttk.Frame):
    """ This object contains the graphical elements to select a working folder."""

    def __init__(self,parent,presenter:Presenter, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        '''Initialize the path selector.'''

        # Set the grid configuration of this object
        self.columnconfigure(0,weight=0)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=0)

        # Draw the graphical interface of the path selector 
        self.lab = ttk.Label(self, text = 'File', width = 20)
        self.lab.grid(row=0, column=0)

        self.pathEntry = ttk.Entry(self, justify='right')
        self.pathEntry.insert(0,presenter.model.settings.workingFolder)
        self.pathEntry.grid(row=0,column=1,sticky = "EW")
        self.pathEntry.bind('<Return>', presenter.SetWorkingFolderManually)
        self.pathEntry.bind('<FocusOut>', presenter.SetWorkingFolderManually)

        self.navigate = ttk.Button(self, text="...", command= lambda:presenter.BrowseResFile())
        self.navigate.grid(row=0, column=2)