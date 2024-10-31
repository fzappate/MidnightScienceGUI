import tkinter as tk
from tkinter import ttk

from ui.CollapsiblePane import CollapsiblePaneDelOpts


class SubplotPane(CollapsiblePaneDelOpts):
    def __init__(self, 
                 parent, 
                 presenter,
                 subplotModel,
                 xAxisIndx = None,
                 *args,**kwargs):
    
        ''''''
        super().__init__(parent,*args,**kwargs)
        
        # Store the inputs
        self.presenter = presenter
        self.listOfSignals = subplotModel.xAxisSignalsName
        self.xAxisIndx = subplotModel.xAxisSelectedIndx
        
        # Configure the master widget
        self.collapsibleFrame.rowconfigure(3,weight=1)
        self.headerLabel.configure(text=subplotModel.name)
        self.optsBtn.configure(command=lambda:self.presenter.OpenSubplotOptions(self,self.optsBtn))
        self.delBtn.configure( command=lambda:self.presenter.DeleteSubplot(self))
        
        # Add the widgets        
        self.noOfRows = 0
        self.xAxisLabel = ttk.Label(self.collapsibleFrame,text = 'Select X axis')
        self.xAxisLabel.grid(row=self.noOfRows,column=0,sticky='W')
        
        self.noOfRows +=1
        self.xAxisSelect = ttk.Combobox(self.collapsibleFrame,state='readonly',values=self.listOfSignals)
        self.xAxisSelect.grid(row=self.noOfRows,column=0,sticky='EW')
        self.xAxisSelect.bind("<<ComboboxSelected>>",lambda event: self.presenter.SelectXAxis(event, self))
        
        self.noOfRows +=1
        self.addFileBtn = ttk.Button(self.collapsibleFrame,text='Add Result File', command= lambda:self.presenter.AddResultFile(self))
        self.addFileBtn.grid(row=self.noOfRows,column=0,sticky='W')
        # Check if the list of signals is empty, if not set the first one
        if len(self.listOfSignals)>0:
            self.xAxisSelect.current(self.xAxisIndx)
            
        self.noOfRows +=1
        self.interior = tk.Frame(self.collapsibleFrame)
        self.interior.grid(row=self.noOfRows,column=0,sticky='NEWS')
        self.interior.columnconfigure(0,weight=1)
            
        
            
            