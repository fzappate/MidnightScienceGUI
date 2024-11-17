import tkinter as tk
from tkinter import ttk
import customtkinter

from ui.CollapsiblePane import CollapsiblePaneDelOpts


class SubplotPane(CollapsiblePaneDelOpts):
    def __init__(self, 
                 parent, 
                 presenter,
                 index,
                 subplotModel,
                 xAxisIndx = None,
                 *args,**kwargs):
    
        ''''''
        super().__init__(parent,subplotModel.isCollapsed,*args,**kwargs)
        
        # Store the inputs
        self.index = index
        self.presenter = presenter
        self.listOfSignals = subplotModel.xAxisSignalsName
        self.xAxisIndx = subplotModel.xAxisSelectedIndx
        
        # Configure the master widget
        btnSize = 30
        self.collapsibleFrame.rowconfigure(3,weight=1)
        self.headerLabel.configure(text=subplotModel.name)
        self.expandButton.configure(command = lambda:self.UpdateSubplotPaneAndModelState())
        self.expandButton.configure(width = btnSize)
        self.optsBtn.configure(command=lambda:self.presenter.OpenSubplotOptions(self,self.optsBtn))
        self.optsBtn.configure(width = btnSize)
        self.delBtn.configure(command=lambda:self.presenter.DeleteSubplot(self))
        self.delBtn.configure(width = btnSize)
        
        # Add the widgets        
        self.noOfRows = 0
        self.addFileBtn = customtkinter.CTkButton(self.collapsibleFrame,text='Add Result File', command= lambda:self.presenter.AddResultFile(self))
        self.addFileBtn.grid(row=self.noOfRows,column=0,sticky='EW', pady = (3,3))
        # if len(self.listOfSignals)>0:
        #     self.xAxisSelect.set(self.listOfSignals[0])
            
        self.noOfRows +=1
        self.interior = customtkinter.CTkFrame(self.collapsibleFrame)
        self.interior.grid(row=self.noOfRows,column=0,sticky='NEWS')
        self.interior.columnconfigure(0,weight=1)
        
    def UpdateSubplotPaneAndModelState(self)->None:
        '''First it calls the SwitchState function of the parent CollapsiblePane to update its status.
        Then, it saves its status in the model.'''
        self.SwitchState()
        
        self.presenter.SaveSubplotStateIntoModel(self)
            
        
            
            