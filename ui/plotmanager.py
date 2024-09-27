from tkinter import ttk
import tkinter as tk

from ui.fileselector import FileSelectorDel


class PlotManager(tk.Frame):    
    def __init__(self, parent, presenter,*args,**kwargs)->None:
        """
        Initialize an instance of the class of PlotManager. 
        This is a control panel that manages the result files and signals.
        
        args: 
        - all the Frame arguments
            - background, bg: set background color
            - borderwidth, bd: set border width
            - ...
        
        -----USAGE-----
        This is used exactly as a Frame widget.
        """  
        super().__init__(parent,*args,**kwargs)
        
        self.toggleFrameList = []
        self.noOfRows = 0
        self.presenter = presenter
        
        # Set PlotManager columns weight
        self.columnconfigure(0,weight=1)

        # Results file selection
        self.noOfRows
        self.addPlot = ttk.Button(self,text='Add Plot',command = lambda:self.presenter.AddSubplot(self)) 
        self.addPlot.grid(row=self.noOfRows,column=0,sticky='W')
    
