import tkinter as tk
from tkinter import ttk

class SignalEntry(tk.Frame):
    def __init__(self,parent,text,*args,**kwargs)->None:
        super().__init__(parent,*args,**kwargs)

        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=0)
        
        self.entry = ttk.Label(self, text = text)
        self.entry.grid(row=1,column=0,sticky='EW', padx = 3, pady = 2)

        self.eraseButton = ttk.Button(self,text='x',width = 5,command=self.destroy)
        self.eraseButton.grid(row=1,column=1,sticky='EW', padx = 3, pady = 2)
        
        self.hideButton = ttk.Button(self,text='o',width = 5,command=self.destroy)
        self.hideButton.grid(row=1,column=2,sticky='EW', padx = 3, pady = 2)