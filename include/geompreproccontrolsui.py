import tkinter as tk
from tkinter import ttk 


class GeomPreprocControlsUI(ttk.Frame):
    '''Class of object containing the UI of the buttons used to operate the gear generator.'''

    def __init__(self,parent,presenter)->None:
        super().__init__(parent)
        '''Initialize the widget that control the GearGenUI'''
        # Buttons
        btn1_button = ttk.Button(self,text='Load', command= lambda:presenter.LoadGearGenData())
        btn1_button.grid(row=0,column=0)
        btn2_button = ttk.Button(self,text='Save', command= lambda:presenter.SaveGearGenData())
        btn2_button.grid(row=0,column=1)

    
    def UpdateDictionariesFromEntries(self)->None:
        '''Update the dicitonaries based on the entries of the input panel.'''

        # Iterate on the entries in the input panel
        for idx, entry in enumerate(self.inputsPanel.LabelHelpEntryList):
            # Update the dictionariy
            self.inputsDict.dictCollection[idx]["value"] = entry.get()
            # Update the LabelHelpEntry object 
            entry.value = entry.get()

