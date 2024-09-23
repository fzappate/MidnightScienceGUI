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
        self.noOfRows
        self.addPlot = ttk.Button(self,text='Add Plot',command = self.AddSubplot) 
        self.addPlot.grid(row=self.noOfRows,column=0,sticky='W')
    
    def AddSubplot(self)->None:
        '''Add a toggle frame to the plot manager pane.'''
        subplotLabel = "Subplot " + str(self.noOfRows)
        self.noOfRows += 1 
        self.toggleFrame = TogglePane(self, label = subplotLabel, bg = 'cyan')
        self.toggleFrame.grid(row = self.noOfRows, column = 0, sticky='EW')
        
        # Toggle pane content
        inputFileSelector = ResFileManager(self.toggleFrame.interior, self.presenter, bg = 'blue')
        inputFileSelector.grid(row=0,column=0,sticky='EW')



class ResFileManager(tk.Frame):
    def __init__(self, parent, presenter,*args,**kwargs)->None:
        """
        Initialize an instance of the class of ResFileManager. 
        This is a control panel that manages the result displayed in one subplot.
        
        args: 
        - all the Frame arguments
            - background, bg: set background color
            - borderwidth, bd: set border width
            - ...
        
        -----USAGE-----
        This is used exactly as a Frame widget.
        """  
        super().__init__(parent,*args,**kwargs)
        self.presenter = presenter
        self.noOfRows = 0
        self.columnconfigure(0,weight=1)
        
        addFileBtn = ttk.Button(self,text='Add Result File', command= self.AddResFile)
        addFileBtn.grid(row=self.noOfRows,column=0,sticky='W')
        
    def AddResFile(self)->None:
        '''Add result pane.'''
        self.noOfRows += 1
        self.resFilePane = ResFilePane(self, self.presenter)
        self.resFilePane.grid(row = self.noOfRows,column=0, sticky = 'EW')
        
        
        
class ResFilePane(tk.Frame):
    def __init__(self, parent, presenter,*args,**kwargs)->None:
        """
        Initialize an instance of the class of ResFilePane. 
        This is a pane where, given a result file, signals can be selected.
        
        args: 
        - all the Frame arguments
            - background, bg: set background color
            - borderwidth, bd: set border width
            - ...
        
        -----USAGE-----
        This is used exactly as a Frame widget.
        """  
        super().__init__(parent,*args,**kwargs)
        # Set columns weight
        self.columnconfigure(0,weight=1)
        
        # Handy numbers
        self.noOfRows = 0
        self.presenter = presenter
        
        self.fileSelector = FileSelector(self,presenter, bg = 'grey40')
        self.fileSelector.grid(row=self.noOfRows,column=0,sticky='EW')
        
        self.noOfRows +=1
        listOfSignals = ["Option 1", "Option 2", "Option 3"]
        self.signalCollection = ttk.Combobox(self,state='readonly', values=listOfSignals)
        self.signalCollection.grid(row=self.noOfRows,column=0,sticky='EW', padx = 3, pady = 2)
        
        self.signalCollection.bind("<<ComboboxSelected>>", self.PrintCombo)
        
    def PrintCombo(self,event):
        '''Test fun'''
        selection = self.signalCollection.get()
        
        self.noOfRows +=1
        sigPane = SignalPane(self, self.presenter, sigName = selection, bg = 'red')
        sigPane.grid(row=self.noOfRows,column=0,sticky='EW')

        
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
        self.delIcon = '\u2297' # ⊗
        self.delIcon = '\u26DD' # ⛝
        self.delIcon = '\u2BBF' # ⮿
        self.delIcon = '\u2BBE' # ⮾
        self.delIcon = '\u2B59' # ⭙ 
        self.delIcon = '\U0001F5D1' #🗑
        self.optIcon = '\U0001F3A8' # 🎨
        self.optIcon = '\U0001F6E0' # 🛠️
        self.optIcon = '\u2699' # ⚙️ 
        self.optIcon = '\U0001F527' # 🔧
        
        self.label = ttk.Label(self,text=sigName)
        self.label.grid(row=0,column=0,sticky='W',padx = (4,0))
        
        self.optBtn = ttk.Button(self,text = self.optIcon, width=3)
        self.optBtn.grid(row=0,column=1,sticky='EW', padx=(3,0))
        
        self.delBtn = ttk.Button(self,text = self.delIcon, width=3)
        self.delBtn.grid(row=0,column=2,sticky='EW', padx = 3)
        