from tkinter import ttk
import tkinter as tk

from ui.resizableframe import ResizableFrameRightEdge 

from include.labelhelpinput import LabelHelpEntry
from include.collapsiblepane import CollapsiblePane
from include.expandablelist import ExpandableList
from ui.fileselector import FileSelector

class SignalSelectionFrame(ResizableFrameRightEdge):
    def __init__(self,parent,presenter, *args, **kwargs)->None:
        super().__init__(parent,*args, **kwargs)
        '''Graphicalm object that wraps the widgets necessary to select the signals to plot. '''

        # Make sure that the content of SignalSelector stretches from left to right and top to bottom
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0, weight=1)

        # Input panel must be placed in a canvas to use the scroll bar
        self.inputCanvas = tk.Canvas(self)
        self.inputCanvas.columnconfigure(0,weight=1)
        self.signalSelectionContent = SignalSelectionContent(self.inputCanvas,presenter)
        self.scrollbar=ttk.Scrollbar(self,orient="vertical", command=self.inputCanvas.yview)
        self.inputCanvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Create an handle for the frame window so that it can be configured later 
        self.internal = self.inputCanvas.create_window((0, 0), window=self.signalSelectionContent, anchor="nw")

        self.scrollbar.grid(row=0,column=1,sticky='NSE',padx = (0,5))
        self.inputCanvas.grid(row=0,column=0,sticky='NEWS')

        # Bind methods
        # Horizontally stretch the frame inside the canvas to fill the canvas when it is resized
        self.inputCanvas.bind("<Configure>", lambda e: self.inputCanvas.itemconfig(self.internal, width=e.width))
        # Scroll bar configures 
        self.signalSelectionContent.bind("<Configure>",lambda e: self.inputCanvas.configure(scrollregion=self.signalSelectionContent.bbox("all")))
        self.signalSelectionContent.bind('<Enter>', self.boundToMouseWheel)
        self.signalSelectionContent.bind('<Leave>', self.unboundToMouseWheel)

        # Run button 
        self.runButton = ttk.Button(self,text = 'Run')
        self.runButton.grid(row=1,column=0,sticky='E')


    def boundToMouseWheel(self, event):
        self.inputCanvas.bind_all("<MouseWheel>", self._on_mousewheel)


    def unboundToMouseWheel(self, event):
        self.inputCanvas.unbind_all("<MouseWheel>")


    def _on_mousewheel(self, event):
        # If frame is greater than canvas scroll, otherwise not.
        inputsPanelLength = self.inputsPanel.winfo_height()
        canvasLength = self.inputCanvas.winfo_height()
        if (inputsPanelLength > canvasLength):
                self.inputCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
                
                
class SignalSelectionContent(ttk.Frame):    
    '''This class contains all the UI widget necesary to navigate the signals of a result file.'''

    def __init__(self, parent, presenter,*args,**kwargs)->None:
        super().__init__(parent,*args,**kwargs)     
        '''Initialize the SignalSelectionContent panel.'''

        self.allSignals = []
        
        # Make sure that the grid column takes up all the space 
        self.columnconfigure(0,weight=1)

        # Create the main frame and collapsible panes first 
        self.fileSelector = FileSelector(self,presenter)
        self.fileSelector.grid(row=0,column=0,sticky='EW')
        
        self.frame = ttk.Frame(self)
        self.frame.columnconfigure(0,weight=1)
        self.frame.columnconfigure(1,weight=0)
        
        self.signalCollection = ttk.Combobox(self.frame,state='readonly')
        self.signalCollection.grid(row=0,column=0,sticky='EW')
        
        self.addSignBtn = ttk.Button(self.frame,text="Add",width=10, command=self.addSignal)
        self.addSignBtn.grid(row=0,column=1,sticky='EW')
        
        self.frame.grid(row=1,column=0,sticky='EW')
        
        
    def addSignal(self):
        entryText = self.signalCollection.get()
        ent = ErasableEntry(self,entryText)
        entryPosition = len(self.allSignals)+2
        ent.grid(row = entryPosition,column=0,sticky='EW')
        self.allSignals.append(ent)
        
        
class ErasableEntry(ttk.Frame):
    def __init__(self,parent,text,*args,**kwargs)->None:
        super().__init__(parent,*args,**kwargs)

        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=0)
        
        self.firstEntry = ttk.Entry(self)
        self.firstEntry.insert(0, text)
        self.firstEntry.grid(row=1,column=0,sticky='EW')

        self.eraseButton = ttk.Button(self,text='X',width = 5,command=self.destroy)
        self.eraseButton.grid(row=1,column=1,sticky='EW')
        