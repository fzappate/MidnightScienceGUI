from tkinter import ttk
import tkinter as tk

from ui.ResizableFrame import CTkResizableFrameRightEdgeScrollV
import customtkinter

class PlotManager(CTkResizableFrameRightEdgeScrollV):    
# class PlotManager(CTkResizableFrameRightEdgeScrollV):    
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

        # Results file selection
        self.noOfRows = 0
        # self.addPlot = customtkinter.CTkButton(self,text='Add Subplot',command = lambda:self.presenter.AddSubplot(self)) 
        self.addPlot = customtkinter.CTkButton(self.scrollFrame,text='Add Subplot',command = lambda:self.presenter.AddSubplot(self)) 
        self.addPlot.grid(row=self.noOfRows,column=0,sticky='NEW')
        
        self.noOfRows += 1    
        # self.interior =customtkinter.CTkFrame(self)
        self.interior =customtkinter.CTkFrame(self.scrollFrame)
        self.interior.grid(row=self.noOfRows,column=0,sticky='NEWS')
        self.interior.columnconfigure(0,weight=1)
    
        self.noOfIntRows = 0    
