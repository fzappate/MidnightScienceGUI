from tkinter import ttk
import tkinter as tk
import customtkinter

from ui.SignalPane import SignalPane
from ui.FileSelector import FileSelectorDel
from ui.CTkScrollableComboBox import CTkScrollableComboBox

class ResFilePane(customtkinter.CTkFrame):
    def __init__(self, parent, presenter,index = 0,entryText = '',comboboxList = [],*args,**kwargs)->None:
        """
        Initialize an instance of the class of ResFilePane. 
        This is a pane where, given a result file, signals can be selected.
        
        args: 
        - all the Frame arguments
            - background, bg: set background color
            - borderwidth, bd: set border width
            - ...
        
        -----USAGE-----
        This is used exactly as a Frame widget.
        """  
        super().__init__(parent,*args,**kwargs)
        # Handy numbers
        self.name = ''
        self.index = index
        self.presenter = presenter
        self.signalList = comboboxList
        labelWidth = 70
        # Set column weight
        self.columnconfigure(1,weight=1)
        
        self.noOfRows = 0
        self.fileSelector = FileSelectorDel(self,presenter,entryText=entryText)
        self.fileSelector.grid(row=self.noOfRows,column=0,sticky='EW',columnspan=2)
        
        # X Axis Selection
        self.noOfRows +=1
        self.selX = customtkinter.CTkLabel(self, text = 'Select X', anchor = 'w',width = labelWidth)
        self.selX.grid(row=self.noOfRows,column=0,sticky='EW', padx = (3,0), pady = 3)
        
        # self.xSignalCollection = CTkScrollableComboBox(self, self.presenter.AddXAxisSignal,values = comboboxList)
        self.xSignalCollection = customtkinter.CTkComboBox(self, values = comboboxList, command = lambda event: self.presenter.AddXAxisSignal(event, self))
        self.xSignalCollection.grid(row=self.noOfRows,column=1,sticky='EW', padx = (3,0), pady = 3)
        self.xSignalCollection.set('')
        
        # Frame for selected X Axis signal
        self.noOfRows +=1
        self.xAxisInterior = customtkinter.CTkFrame(self,height=0,width=0)
        self.xAxisInterior.grid(row=self.noOfRows,column=0,sticky='NEW', padx = (3,0),columnspan=2)
        self.xAxisInterior.columnconfigure(0,weight=1)
                
        # Y Axis Selection
        self.noOfRows +=1
        self.selX = customtkinter.CTkLabel(self, text = 'Select Y', anchor = 'w',width = labelWidth)
        self.selX.grid(row=self.noOfRows,column=0,sticky='EW', padx = (3,0), pady = 3)
        
        # self.ySignalCollection = CTkScrollableComboBox(self,self.presenter.AddSignal,values=comboboxList)
        self.ySignalCollection = customtkinter.CTkComboBox(self,values=comboboxList, command = lambda event: self.presenter.AddSignal(event,self))
        self.ySignalCollection.grid(row=self.noOfRows,column=1,sticky='EW', padx = (3,0), pady = 3)
        self.ySignalCollection.set('')
        
        # Frame for selected signals
        self.noOfRows +=1
        self.yAxisInterior = customtkinter.CTkFrame(self,height=0,width=0)
        self.yAxisInterior.grid(row=self.noOfRows,column=0,sticky='NEW', padx = (3,0),pady= (0,6),columnspan=2)     
        self.yAxisInterior.columnconfigure(0,weight=1)   
                
   