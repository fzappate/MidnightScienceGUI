import tkinter as tk
from tkinter import ttk 

from include.labelhelpinput import LabelHelpEntry

class GearGenInputsUI(tk.Frame):    
    '''Class of widgets containign the panel containing the inputs entry of the gear generator.'''

    def __init__(self, parent, presenter,*args,**kwargs)->None:
        super().__init__(parent,*args,**kwargs)     
        '''Initialize the input panel.'''
        
        # Allow the content of GearGenInputsUI to expand horizontally
        self.columnconfigure(0,weight=1)

        self.LabelHelpEntryList = []
        for idx, dict in enumerate(presenter.model.gearGenInputs.dictCollection):

            # Create a LabelHelpEntry object for each element in the inputDict 
            lheTemp = LabelHelpEntry(self, dict, idx)
            lheTemp.grid(row = idx,column=0,sticky = 'EW')

            # Add the LabelHelpEntry object in a list for future handling
            self.LabelHelpEntryList.insert(len(self.LabelHelpEntryList),lheTemp)

            




