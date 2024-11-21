from tkinter import ttk
import tkinter as tk
import customtkinter

from ui.SignalPane import SignalPane
from ui.FileSelector import FileSelectorDel

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
        # Set columns weight
        self.columnconfigure(0,weight=1)
        
        # Handy numbers
        self.name = ''
        self.index = index
        self.presenter = presenter
        
        self.noOfRows = 0
        self.fileSelector = FileSelectorDel(self,presenter,entryText=entryText)
        self.fileSelector.grid(row=self.noOfRows,column=0,sticky='EW')
        
        self.noOfRows +=1
        self.signalSelection = customtkinter.CTkFrame(self)
        self.signalSelection.grid(row=self.noOfRows,column=0,sticky='EW')
        self.signalSelection.columnconfigure(1,weight=1)
        
        self.noOfSigSelRows =0
        self.selX = customtkinter.CTkLabel(self.signalSelection, text = 'Select X', width = 70)
        self.selX.grid(row=self.noOfSigSelRows,column=0,sticky='EW', padx = 0, pady = 3)
        
        self.signalCollection = customtkinter.CTkComboBox(self.signalSelection,state='readonly',values=comboboxList)
        self.signalCollection.grid(row=self.noOfSigSelRows,column=1,sticky='EW', padx = (3,0), pady = 3)
        # self.signalCollection.bind("<<ComboboxSelected>>",lambda event: self.presenter.AddSignal(event, self))
        
        self.noOfSigSelRows +=1
        self.selX = customtkinter.CTkLabel(self.signalSelection, text = 'Select Y', width = 70)
        self.selX.grid(row=self.noOfSigSelRows,column=0,sticky='EW', padx = 0, pady = 3)
        
        self.signalCollection = customtkinter.CTkComboBox(self.signalSelection,state='readonly',values=comboboxList)
        self.signalCollection.grid(row=self.noOfSigSelRows,column=1,sticky='EW', padx = (3,0), pady = 3)
        self.signalCollection.bind("<<ComboboxSelected>>",lambda event: self.presenter.AddSignal(event, self))
        
        self.noOfRows +=1
        self.interior = customtkinter.CTkFrame(self,height=0)
        self.interior.grid(row=self.noOfRows,column=0,sticky='NEW')        
        self.interior.columnconfigure(0,weight=1)
        
      
        
        
    def PrintCombo(self,event):
        '''Test fun'''
        selection = self.signalCollection.get()
        
        self.noOfRows +=1
        sigPane = SignalPane(self, self.presenter, sigName = selection, bg = 'red')
        sigPane.grid(row=self.noOfRows,column=0,sticky='EW')
        
    