from tkinter import ttk
import tkinter as tk

from ui.ResizableFrame import ResizableFrameRightEdgeScrollV


class PlotManager(ResizableFrameRightEdgeScrollV):    
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
        # Store the inputs
        self.toggleFrameList = []
        self.presenter = presenter
        
        # Configure parent object
        self.scrollFrame.columnconfigure(0,weight=1)
        self.scrollFrame.rowconfigure(1,weight=1)

        # Results file selection
        self.noOfRows = 0
        self.addPlot = ttk.Button(self.scrollFrame,text='Add Subplot',command = lambda:self.presenter.AddSubplot(self)) 
        self.addPlot.grid(row=self.noOfRows,column=0,sticky='NW')
        
        self.noOfRows += 1    
        self.noOfIntRows = 0    
        self.interior = tk.Frame(self.scrollFrame)
        self.interior.grid(row=self.noOfRows,column=0,sticky='NEWS')
        self.interior.columnconfigure(0,weight=1)
    
