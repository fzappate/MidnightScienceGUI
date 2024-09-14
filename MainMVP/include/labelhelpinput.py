import tkinter as tk
from tkinter import ttk 

class LabelHelpEntry(ttk.Frame):
    '''Class of objects containing the label, the entry, and the help button of the input.'''

    def __init__(self, parent, dict , rowCounter,*args,**kwargs)->None:
        super().__init__(parent, *args,**kwargs)
        '''Initialize the label, entry, help widget.'''

        # Make sure that the entry stretches to fill the space
        self.columnconfigure(2,weight=1)

        # Extract the info from the dictionary and save them in the object 
        self.name = dict["name"]
        self.descr = dict["description"]
        self.img = dict["image"]
        self.type = dict["type"]
        self.value = dict["value"]
        self.rowPosition = rowCounter
        self.createWidget(parent)


    def createWidget(self, parent)->None:
        '''Draw the graphical representation of the label, entry, help widget.'''

        charPerLabel = 20
        charPerHelpBtn = 3
        padxy = 2

        self.label = ttk.Label(self,text=self.name,width=charPerLabel)
        self.label.grid(row=self.rowPosition,column=0)
        self.help = ttk.Button(self,text='?', width=charPerHelpBtn, command=lambda : self.openHelpWindow(parent))
        self.help.grid(row=self.rowPosition, column=1, padx=padxy, pady=padxy)
        self.entry = ttk.Entry(self)
        self.entry.grid(row=self.rowPosition,column=2,sticky='EW',padx=(0,10))


    def delete(self,start,end)->None:
        """Delete the content of the entry."""
        self.entry.delete(start,end)


    def insert(self,where,txt)->None:
        """Set the content of the entry."""
        self.entry.insert(where,txt)


    def get(self)->str:
        '''Get the content of the entry.'''
        return self.entry.get()


    def openHelpWindow(self,parent)->None:        
        '''Get the input help window.'''
        window = tk.Toplevel(parent)
