import tkinter as tk
from tkinter import ttk

from ui.CollapsiblePane import CollapsiblePaneDelOpts


class SubplotPane(CollapsiblePaneDelOpts):
    def __init__(self, 
                 parent, 
                 presenter,
                 index,
                 subplotModel,
                 *args,**kwargs):
    
        ''''''
        super().__init__(parent,subplotModel.isCollapsed,*args,**kwargs)
        
        # Store the inputs
        self.index = index
        self.presenter = presenter
        
        # Configure the master widget
        self.collapsibleFrame.rowconfigure(3,weight=1)
        self.headerLabel.configure(text=subplotModel.name)
        self.expandButton.configure(command = lambda:self.UpdateSubplotPaneAndModelState())
        self.optsBtn.configure(command=lambda:self.presenter.OpenSubplotOptions(self,self.optsBtn))
        self.delBtn.configure(command=lambda:self.presenter.DeleteSubplot(self))
        
        # Add the widgets        
        self.noOfRows = 0
        self.addFileBtn = ttk.Button(self.collapsibleFrame,text='Add Result File', command= lambda:self.presenter.AddResultFile(self))
        self.addFileBtn.grid(row=self.noOfRows,column=0,sticky='EW', pady = (3,3))
            
        self.noOfRows +=1
        self.interior = ttk.Frame(self.collapsibleFrame,height=0)
        self.interior.grid(row=self.noOfRows,column=0,sticky='NEWS',pady = (3,12))
        self.interior.columnconfigure(0,weight=1)

        
    def UpdateSubplotPaneAndModelState(self)->None:
        '''First it calls the SwitchState function of the parent CollapsiblePane to update its status.
        Then, it saves its status in the model.'''
        self.SwitchState()
        
        self.presenter.SaveSubplotStateIntoModel(self)
            
        
            
            