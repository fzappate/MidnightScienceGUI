from tkinter import ttk
import tkinter as tk

class SignalPane(tk.Frame):
    def __init__(self, 
                 parent, 
                 presenter,
                 sigName = 'Signal',
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
        
        # Define columns weight
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=0)
        self.columnconfigure(2,weight=0)
        
        # Handy icons
        self.delIcon = '\U0001F5D1' # 🗑
        self.optIcon = '\U0001F527' # 🔧
        
        self.label = ttk.Label(self,text=sigName)
        self.label.grid(row=0,column=0,sticky='W',padx = (4,0))
        
        self.optBtn = ttk.Button(self,text = self.optIcon, width=3)
        self.optBtn.grid(row=0,column=1,sticky='EW', padx=(3,0))
        
        self.delBtn = ttk.Button(self,text = self.delIcon, width=3,command=self.DeleteSignal)
        self.delBtn.grid(row=0,column=2,sticky='EW', padx = 3)
        
    def DeleteSignal(self):
        self.destroy()