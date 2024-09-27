import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog

# from presenter.presenter import Presenter


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


class FileSelector(tk.Frame):
    """ This object contains the graphical elements to select a working folder."""

    def __init__(self,parent,presenter, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        '''Initialize the path selector.'''

        # Set the grid configuration of this object
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=0)

        # Draw the graphical interface of the path selector 
        self.lab = ttk.Label(self, text = 'File', width = 7)
        self.lab.grid(row=0, column=0, sticky = 'EW',padx = 3, pady = 2)
        self.iconCode = "\U0001F5C1" # 🗈
        self.navigate = ttk.Button(self, text=self.iconCode,width = 3, command= lambda:presenter.BrowseResFile())
        self.navigate.grid(row=0, column=1, padx = (0,3), pady = 2)
        
        self.pathEntry = ttk.Entry(self, justify='right')
        self.pathEntry.insert(0,presenter.model.settings.resultsFilePath)
        self.pathEntry.grid(row=1,column=0,sticky = "EW", padx = 3, pady = (0,2),columnspan=2)
        self.pathEntry.bind('<Return>', presenter.SetWorkingFolderManually)
        self.pathEntry.bind('<FocusOut>', presenter.SetWorkingFolderManually)
        
class FileSelectorDel(tk.Frame):
    """ This object contains the graphical elements to select a working folder."""

    def __init__(self,parent,presenter, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        '''Initialize the path selector.'''

        # Set the grid configuration of this object
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=0)

        # Draw the graphical interface of the path selector 
        self.lab = ttk.Label(self, text = 'File', width = 7)
        self.lab.grid(row=0, column=0, sticky = 'EW',padx = 3, pady = 2)
        self.navigateIcon = "\U0001F5C1" # 🗈
        self.navigate = ttk.Button(self, text=self.navigateIcon,width = 3, command= lambda:presenter.BrowseResFile())
        self.navigate.grid(row=0, column=1, padx = (0,3), pady = 2)
        self.deleteIcon = "\u274C" # ❌ 
        self.delBtn = ttk.Button(self, text=self.deleteIcon, width = 3, command= self.DeleteFileSelector)
        self.delBtn.grid(row=0, column=2, padx = (0,3), pady = 2)
        
        self.pathEntry = ttk.Entry(self, justify='right')
        self.pathEntry.insert(0,presenter.model.settings.resultsFilePath)
        self.pathEntry.grid(row=1,column=0,sticky = "EW", padx = 3, pady = (0,2),columnspan=2)
        self.pathEntry.bind('<Return>', presenter.SetWorkingFolderManually)
        self.pathEntry.bind('<FocusOut>', presenter.SetWorkingFolderManually)
    
    def DeleteFileSelector(self):
        self.destroy()
