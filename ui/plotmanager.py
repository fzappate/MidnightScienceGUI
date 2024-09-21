from tkinter import ttk
import tkinter as tk

from ui.resizableframe import ResizableFrameRightEdge 
from ui.signalentry import SignalEntry
from ui.fileselector import FileSelector
from ui.collapsiblepanes import TogglePaneDel
from ui.collapsiblepanes import TogglePane

class PlotManagerPane(ResizableFrameRightEdge):
    def __init__(self,parent,presenter, *args, **kwargs)->None:
        super().__init__(parent,*args, **kwargs)
        '''Graphicalm object that wraps the widgets necessary to select the signals to plot. '''

        # Make sure that the content of SignalSelector stretches from left to right and top to bottom
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0, weight=1)

        # Input panel must be placed in a canvas to use the scroll bar
        self.inputCanvas = tk.Canvas(self)
        self.inputCanvas.columnconfigure(0,weight=1)
        self.inputCanvas.configure(bg='green')
        self.scrollbar=ttk.Scrollbar(self,orient="vertical", command=self.inputCanvas.yview)
        self.inputCanvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.plotManager = PlotManager(self.inputCanvas,presenter, bg = 'cyan')        
        
        # Create an handle for the frame window so that it can be configured later 
        self.internal = self.inputCanvas.create_window((0, 0), window=self.plotManager, anchor="nw")

        self.inputCanvas.grid(row=0,column=0,sticky='NEWS',padx = (3,3),pady = (3,3))
        self.scrollbar.grid(row=0,column=1,sticky='NSE',padx = (0,3),pady = (3,3))

        # Bind methods
        # Horizontally stretch the frame inside the canvas to fill the canvas when it is resized
        self.inputCanvas.bind("<Configure>", lambda e: self.inputCanvas.itemconfig(self.internal, width=e.width))
        # Scroll bar configures 
        self.plotManager.bind("<Configure>",lambda e: self.inputCanvas.configure(scrollregion=self.plotManager.bbox("all")))
        self.plotManager.bind('<Enter>', self.boundToMouseWheel)
        self.plotManager.bind('<Leave>', self.unboundToMouseWheel)


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
                
                
class PlotManager(tk.Frame):    
    '''This class contains all the UI widget necesary to navigate the signals of a result file.'''

    def __init__(self, parent, presenter,*args,**kwargs)->None:
        super().__init__(parent,*args,**kwargs)     
        '''Initialize the PlotManager panel.'''

        self.toggleFrameList = []
        self.noOfRows = 0
        self.presenter = presenter
        
        # Set PlotManager columns weight
        self.columnconfigure(0,weight=1)

        # Results file selection
        rowNo = 0
        self.fileSelector = ttk.Button(self,text='Add Plot',command = self.AddToggleFrame) 
        self.fileSelector.grid(row=rowNo,column=0,sticky='W')
        
        # subplotLabel = "Subplot " + str(self.noOfRows)
        # toggleFrame = TogglePaneDel(self, label = subplotLabel, bg = 'yellow')
        # self.toggleFrameList.append(toggleFrame)
        # self.noOfRows +=1
        # toggleFrame.grid(row = self.noOfRows, column = 0, sticky='WE')
        
        # rowNo+=1
        # self.fileSelector = FileSelector(self,presenter, bg = 'grey40')
        # self.fileSelector.grid(row=rowNo,column=0,sticky='EW')
        
        # rowNo+=1
        # self.sigSelLab = ttk.Label(self,text = 'Signal Selection')
        # self.sigSelLab.grid(row=rowNo,column=0,sticky='EW',padx = 3, pady = (4,0))
        
        # rowNo+=1
        # self.signalCollection = ttk.Combobox(self,state='readonly')
        # self.signalCollection.grid(row=rowNo,column=0,sticky='EW', padx = 3, pady = 2)
        
        # self.addSignBtn = ttk.Button(self,text="Add",width=5, command=self.AddSignal)
        # self.addSignBtn.grid(row=rowNo,column=1,sticky='EW', padx = (0,3), pady = 2)
        
        # rowNo+=1
        # self.sigListLab = ttk.Label(self,text='Signal List')
        # self.sigListLab.grid(row=rowNo,column=0,sticky='EW',padx = 3, pady = (4,0))
        
    def AddToggleFrame(self)->None:
        '''Add a toggle frame to the plot manager pane.'''
        subplotLabel = "Subplot " + str(self.noOfRows)
        self.toggleFrame = TogglePaneDel(self, label = subplotLabel)
        self.toggleFrameList.append(self.toggleFrame)
        self.noOfRows +=1
        self.toggleFrame.grid(row = self.noOfRows, column = 0, sticky='EW')
        
    # def AddSignal(self):
    #     '''Perform all the actions to add a signal in the ui, model, and plot canvas.'''
        
    #     # Add SignalEntry in the PlotManager 
    #     entryText = self.signalCollection.get()
    #     ent = SignalEntry(self,entryText,bg='gray40')
    #     entryPosition = len(self.allSignals)+5 # Change this based on how many row we have
    #     ent.grid(row = entryPosition,column=0,sticky='EW')
    #     self.allSignals.append(ent)
        
    #     # Add signal data in the PlotData
    #     self.presenter.AddSignalToPlotData(entryText)
    #     # Plot the signals in plotData
    #     self.presenter.PlotPlotData()
        
        
        