import tkinter as tk
from tkinter import ttk 


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
        self.pathEntry.grid(row=1,column=0,sticky = "EW", padx = 3, pady = (0,2),columnspan=2)
        self.pathEntry.bind('<Return>', presenter.SetWorkingFolderManually)
        self.pathEntry.bind('<FocusOut>', presenter.SetWorkingFolderManually)
      
      
        
class FileSelectorDel(tk.Frame):
    """ This object contains the graphical elements to select a working folder."""

    def __init__(self,parent,presenter, entryText = '', *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        '''Initialize the path selector.'''

        self.presenter = presenter
        
        # Set the grid configuration of this object
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=0)

        # Draw the graphical interface of the path selector 
        self.lab = ttk.Label(self, text = 'Select Result File')
        self.lab.grid(row=0, column=0, sticky = 'EW',padx = (0,0), pady = (0,3))
        self.navigateIcon = "\U0001F5C1" # 🗈
        self.navigate = ttk.Button(self, text=self.navigateIcon,width = 3, command= lambda:presenter.BrowseResFile(self,self.master))
        self.navigate.grid(row=0, column=1, padx = (0,3), pady = (0,3))
        self.deleteIcon = "\u274C" # ❌ 
        self.delBtn = ttk.Button(self, text=self.deleteIcon, width = 3, command= lambda:self.presenter.DeleteResultFile(self.master))
        self.delBtn.grid(row=0, column=2, padx = (0,0), pady = (0,3))
        
        self.pathEntry = ttk.Entry(self)
        self.pathEntry.insert(0,entryText)
        self.pathEntry.grid(row=1,column=0,sticky = "EW", padx = (0,1), pady = (0,3),columnspan=3)
        self.pathEntry.bind('<Return>', lambda event: presenter.FileSelectorReturn(event,self,self.master))
        self.pathEntry.bind('<FocusOut>', lambda event: presenter.FileSelectorReturn(event,self,self.master))
        
    def UpdateEntry(self,entryText)->None:
        '''Update the text of FileSelector entry.'''
        self.pathEntry.delete(0,'end')
        self.pathEntry.insert(0,entryText)
        
    def GetEntry(self)->None:
        '''Get the entry text.'''
        return self.pathEntry.get()
    
