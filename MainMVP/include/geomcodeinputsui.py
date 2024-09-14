import tkinter as tk
from tkinter import ttk 

from include.labelhelpinput import LabelHelpEntry
from include.collapsiblepane import CollapsiblePane
from include.expandablelist import ExpandableList

class GeomCodeInputsUI(ttk.Frame):    
    '''This class is meant to be as close as possible to a simple collection of inputs.
    The actions should be performed by the methods of it's parent class GearGenControls'''

    def __init__(self, parent, presenter,*args,**kwargs)->None:
        super().__init__(parent,*args,**kwargs)     
        '''Initialize the input panel.'''

        # Make sure that the grid column takes up all the space 
        self.columnconfigure(0,weight=1)

        # Create the main frame and collapsible panes first 
        self.topFrame = ttk.Frame(self)
        self.gearDataPane = CollapsiblePane(self,'-','+','Gear Dictionary')
        self.recessDataPane = CollapsiblePane(self,'-','+','Recess Dictionary')
        self.lateralFeatPane = CollapsiblePane(self,'-','+','Lateral Features')
        self.latGroovePane = CollapsiblePane(self,'-','+','Lateral Grooves')
        # Make sure that the frames can stretch horizontally 
        self.topFrame.columnconfigure(0,weight=1)
        self.gearDataPane.columnconfigure(0,weight=1)
        self.recessDataPane.columnconfigure(0,weight=1)
        self.lateralFeatPane.columnconfigure(0,weight=1)
        self.latGroovePane.columnconfigure(0,weight=1)

        self.LabelHelpEntryList = []
        for idx, dict in enumerate(presenter.model.geomCodeInputs.dictCollection):

            # Create a LabelHelpEntry object for each element in the inputDict and place it in the frame stated in the dict 
            if dict['pane'] == 'Gear Dictionary':
                if dict['entryType'] =='LabelHelpEntry':
                    lheTemp = LabelHelpEntry(self.gearDataPane.frame, dict, idx)
                    
                if dict['entryType'] =='ExpandableList':
                    lheTemp = ExpandableList(self.recessDataPane.frame, dict, idx)

            elif dict['pane'] == 'Recess Dictionary':
                if dict['entryType'] =='LabelHelpEntry':
                    lheTemp = LabelHelpEntry(self.recessDataPane.frame, dict, idx)
                    
                if dict['entryType'] =='ExpandableList':
                    lheTemp = ExpandableList(self.recessDataPane.frame, dict, idx)
                    
            elif dict['pane'] == 'Lateral Features':
                if dict['entryType'] =='LabelHelpEntry':
                    lheTemp = LabelHelpEntry(self.lateralFeatPane.frame, dict, idx)
                    
                if dict['entryType'] =='ExpandableList':
                    lheTemp = ExpandableList(self.lateralFeatPane.frame, dict, idx)
                      
            elif dict['pane'] == 'Lateral Grooves':
                if dict['entryType'] =='LabelHelpEntry':
                    lheTemp = LabelHelpEntry(self.latGroovePane.frame, dict, idx)
                    
                if dict['entryType'] =='ExpandableList':
                    lheTemp = ExpandableList(self.latGroovePane.frame, dict, idx)
                    
            else:
                if dict['entryType'] =='LabelHelpEntry':
                    lheTemp = LabelHelpEntry(self.topFrame, dict, idx)   
                    
                if dict['entryType'] =='ExpandableList':
                    lheTemp = ExpandableList(self.topFrame.frame, dict, idx)
                    
            # Place the Label Help Entry in the frame 
            lheTemp.grid(row=idx,column=0,sticky = 'EW')

            # Add the LabelHelpEntry object in a list for future handling
            self.LabelHelpEntryList.insert(len(self.LabelHelpEntryList),lheTemp)

        # Place the main frame and the collapsible frames in the grid
        self.topFrame.grid(row=0,column=0,sticky='EW')
        self.gearDataPane.grid(row=1,column=0,sticky='EW')
        self.recessDataPane.grid(row=2,column=0,sticky='EW')
        self.lateralFeatPane.grid(row=3,column=0,sticky='EW')
        self.latGroovePane.grid(row=4,column=0,sticky='EW')

    

