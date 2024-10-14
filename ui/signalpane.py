from tkinter import ttk
import tkinter as tk

class SignalPane(tk.Frame):
    def __init__(self, 
                 parent, 
                 presenter,
                 signal,
                 indx = 0,
                 *args,
                 **kwargs)->None:
        """
        Initialize an instance of the class of SignalPane. 
        This is a pane that stores the signal name, the option and delete buttons.
        
        args: 
        - all the Frame arguments
            - background, bg: set background color
            - borderwidth, bd: set border width
            - ...
        
        -----USAGE-----
        This is used exactly as a Frame widget.
        """  
        super().__init__(parent,*args,**kwargs)
        
        self.signal = signal
        
        self.signalName = signal 
        self.indx = indx
        self.presenter = presenter
        # Define columns weight
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=0)
        self.columnconfigure(2,weight=0)
        
        # Handy icons
        self.delIcon = '\U0001F5D1' # 🗑
        self.optIcon = '\U0001F527' # 🔧
        
        self.label = ttk.Label(self,text=self.signal.name)
        self.label.grid(row=0,column=0,sticky='W',padx = (4,0))
        
        unitList, scalingList = self.presenter.GetUnitsList(signal)
        
        self.unitsCb = ttk.Combobox(self,width = 7,value=unitList,state='readonly')
        self.unitsCb.grid(row=0,column=1,sticky='EW', padx=(3,0))
        # if len(unitList)>0:
        self.unitsCb.current(0)
        self.unitsCb.bind("<<ComboboxSelected>>",lambda event: self.presenter.ModifySignalScaling(event, self, scalingList))
            
        self.optBtn = ttk.Button(self,text = self.optIcon, width=3)
        self.optBtn.grid(row=0,column=2,sticky='EW', padx=(3,0))
        
        self.delBtn = ttk.Button(self,text = self.delIcon, width=3,command=lambda: self.presenter.DeleteSignal( self))
        self.delBtn.grid(row=0,column=3,sticky='EW', padx = 3)

