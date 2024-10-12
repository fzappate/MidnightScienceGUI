import tkinter as tk
from tkinter import ttk

from ui.resfilepane import ResFilePane

class ResFileManager(tk.Frame):
    def __init__(self, parent, presenter,listOfSignals = [],*args,**kwargs)->None:
        """
        Initialize an instance of the class of ResFileManager. 
        This is a control panel that manages the result displayed in one subplot.
        It consists of a file selector and a combobox
        
        args: 
        - all the Frame arguments
            - background, bg: set background color
            - borderwidth, bd: set border width
            - ...
        
        -----USAGE-----
        This is used exactly as a Frame widget.
        """  
        super().__init__(parent,*args,**kwargs)
        self.presenter = presenter
        self.listOfSignals = listOfSignals
        self.noOfRows = 0
        
        self.columnconfigure(0,weight=1)
        xAxisLabel = ttk.Label(self,text = 'Select X axis')
        xAxisLabel.grid(row=self.noOfRows,column=0,sticky='W')
        
        self.noOfRows +=1
        xAxisSelext = ttk.Combobox(self,state='readonly',values=listOfSignals)
        xAxisSelext.grid(row=self.noOfRows,column=0,sticky='EW')
        
        self.noOfRows +=1
        addFileBtn = ttk.Button(self,text='Add Result File', command= lambda:self.presenter.AddResultFile(self))
        addFileBtn.grid(row=self.noOfRows,column=0,sticky='W')
        