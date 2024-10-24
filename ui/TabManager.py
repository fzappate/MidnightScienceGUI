import tkinter as tk
from tkinter import ttk

class TabManager(tk.Frame):    
    def __init__(self,
                 parent,
                 *args,
                 **kwargs):
        '''Initialzie TabManager options widget.'''
        super().__init__(parent,*args,**kwargs)
        
        self.addButton = ttk.Button(self,text='Add')
        self.addButton.grid(row=0,column=0, sticky='NEWS')
        
        self.optsButton = ttk.Button(self,text='Opts')
        self.optsButton.grid(row=0,column=1, sticky='NEWS')
        
        self.delButton = ttk.Button(self,text='Canc')
        self.delButton.grid(row=0,column=2, sticky='NEWS')