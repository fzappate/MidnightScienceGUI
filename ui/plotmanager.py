from tkinter import ttk
import tkinter as tk

from ui.resizableframe import ResizableFrameRightEdge 
from ui.signalentry import SignalEntry
from ui.fileselector import FileSelector
from ui.collapsiblepanes import TogglePaneDel
from ui.collapsiblepanes import TogglePane
                
class PlotManager(tk.Frame):    
    def __init__(self, parent, presenter,*args,**kwargs)->None:
        """
        Initialize an instance of the class of PlotManager. 
        This is a control panel that manages the result files and signals.
        
        args: 
        - all the Frame arguments
            - background, bg: set background color
            - borderwidth, bd: set border width
            - ...
        
        -----USAGE-----
        This is used exactly as a Frame widget.
        """  
        super().__init__(parent,*args,**kwargs)     
        
        self.toggleFrameList = []
        self.noOfRows = 0
        self.presenter = presenter
        
        # Set PlotManager columns weight
        self.columnconfigure(0,weight=1)

        # Results file selection
        rowNo = 0
        self.addPlot = ttk.Button(self,text='Add Plot',command = self.AddToggleFrame) 
        self.addPlot.grid(row=rowNo,column=0,sticky='W')
        imageExpand = ".\images\expandIcon.png"
        imageCollapse = ".\images\collapseIcon.png"
        
        rowNo += 1 
        self.toggleFrame = TogglePane(self, label = "ciao",iconMode = 'img',expImgPath=imageExpand,collImgPath= imageCollapse)
        self.toggleFrame.grid(row=rowNo,column=0,sticky='W')
        
        
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
        
        
        