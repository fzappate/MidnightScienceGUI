from tkinter import ttk
import tkinter as tk

class SignalPane(tk.Frame):
    def __init__(self, 
                 parent, 
                 presenter,
                 signal,
                 index = 0,
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
        self.index = index
        self.presenter = presenter
        
        # Define columns weight
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=0)
        self.columnconfigure(2,weight=0)
        
        # Handy icons
        self.delIcon = '\u274C' # X
        self.optIcon = '\u2630' # ☰ 
        
        # Signal label
        colNo = 0
        self.label = ttk.Label(self,text=self.signal.name)
        self.label.grid(row=0,column=colNo,sticky='W',padx = (4,0))
        
        unitList, scalingList = self.presenter.GetUnitsList(signal)
        
        # Signal color
        colNo+=1
        self.colorBox = ttk.Label(self,text = '\u2588\u2588\u2588\u2588',foreground=self.signal.color)
        self.colorBox.grid(row=0,column=colNo)
        
        # Signal units
        colNo+=1
        self.unitsCb = ttk.Combobox(self,width = 7,value=unitList,state='readonly')
        self.unitsCb.grid(row=0,column=colNo,sticky='EW', padx=(3,0))
        
        self.unitsCb.set(signal.units)
        self.unitsCb.bind("<<ComboboxSelected>>",lambda event: self.presenter.ModifySignalScaling(event, self, scalingList))
        
        # Signal options
        colNo+=1
        self.optBtn = ttk.Button(self,text = self.optIcon, width=3,command=lambda: self.presenter.OpenSignalOptions(self, self.optBtn))
        self.optBtn.grid(row=0,column=colNo,sticky='EW', padx=(3,0))
        
        # Signal delete
        colNo+=1
        self.delBtn = ttk.Button(self,text = self.delIcon, width=3,command=lambda: self.presenter.DeleteSignal(self))
        self.delBtn.grid(row=0,column=colNo,sticky='EW', padx = 3)


