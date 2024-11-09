import tkinter as tk
from tkinter import ttk
from tkinter import ttk, colorchooser

class PlotOptions(tk.Frame):
    def __init__(self,
                 parent,
                 presenter,
                 plotModel,
                 *args,
                 **kwargs):
        
        ''' Initialize a subplot options pane.'''
        super().__init__(parent,*args,**kwargs)
        '''Initialize the plot options window.'''
        self.presenter = presenter
        
        labelSize = 20
        btnSize = 10
        entrySize = 5
        self.parent = parent
        self.presenter = presenter
        
        title = plotModel.name
        leftMargin = plotModel.leftMargin
        rightMargin = plotModel.rightMargin
        bottomMargin = plotModel.bottomMargin
        topMargin = plotModel.topMargin
        self.selectedCanvasColor = plotModel.canvasColor
        self.selectedPlotColor = plotModel.plotColor
        self.selectedToolbarColor = plotModel.toolbarColor
        
        # Title frame
        rowNo = 0
        self.titleFrame = tk.Frame(parent, pady=3, bg = 'red')
        self.titleFrame.grid(row=rowNo,column=0, pady=3, sticky = 'NEW')
        self.titleFrame.columnconfigure(1,weight=1)
        
        self.titleLab = ttk.Label(self.titleFrame,text='Title',width=labelSize)
        self.titleLab.grid(row=0,column=0, pady=3)
        
        self.titleEntry = tk.Entry(self.titleFrame)
        self.titleEntry.grid(row=0,column=1,padx=3,sticky='EW')
        self.UpdateEntry(self.titleEntry, title)

        
                
        # Plot margins
        rowNo +=1
        self.plotMarginsFrame = tk.Frame(parent, pady=3, bg = 'red')
        self.plotMarginsFrame.grid(row=rowNo,column=0, sticky = 'NEW')
        
        self.xAxisLimLab = ttk.Label(self.plotMarginsFrame, text = 'Set plot margins',width=labelSize)
        self.xAxisLimLab.grid(row=0,column=0)
        
        self.marginsFrame = tk.Frame(self.plotMarginsFrame)
        self.marginsFrame.grid(row=0,column=1)

        self.plotMarginLeft = tk.Entry(self.marginsFrame, width= entrySize)
        self.plotMarginLeft.grid(row=0,column=0,padx=3)
        self.UpdateEntry(self.plotMarginLeft, str(leftMargin))
        
        self.plotMarginRight = tk.Entry(self.marginsFrame, width= entrySize)
        self.plotMarginRight.grid(row=0,column=1,padx=3)
        self.UpdateEntry(self.plotMarginRight, str(rightMargin))
        
        self.plotMarginBottom = tk.Entry(self.marginsFrame, width= entrySize)
        self.plotMarginBottom.grid(row=0,column=2,padx=3)    
        self.UpdateEntry(self.plotMarginBottom, str(bottomMargin))
        
        self.plotMarginTop = tk.Entry(self.marginsFrame, width= entrySize)
        self.plotMarginTop.grid(row=0,column=3,padx=3)    
        self.UpdateEntry(self.plotMarginTop, str(topMargin))
        
        
        self.plotMarginLeft.bind("<FocusOut>",lambda event: self.ValidateLeftMarginEntry(event, self.plotMarginRight, leftMargin))
        self.plotMarginLeft.bind("<Return>",lambda event: self.ValidateLeftMarginEntry(event, self.plotMarginRight, leftMargin))
        self.plotMarginRight.bind("<FocusOut>",lambda event: self.ValidateRightMarginEntry(event, self.plotMarginLeft, rightMargin))
        self.plotMarginRight.bind("<Return>",lambda event: self.ValidateRightMarginEntry(event, self.plotMarginLeft, rightMargin))
        self.plotMarginBottom.bind("<FocusOut>",lambda event: self.ValidateBottomMarginEntry(event, self.plotMarginTop, bottomMargin))
        self.plotMarginBottom.bind("<Return>",lambda event: self.ValidateBottomMarginEntry(event, self.plotMarginTop, bottomMargin))
        self.plotMarginTop.bind("<FocusOut>",lambda event: self.ValidateTopMarginEntry(event, self.plotMarginBottom, topMargin))
        self.plotMarginTop.bind("<Return>",lambda event: self.ValidateTopMarginEntry(event, self.plotMarginBottom, topMargin))
        
                
        # Select canvas color pane
        rowNo +=1
        self.mainCanvasColorFrame = tk.Frame(parent, pady=3, bg = 'blue')
        self.mainCanvasColorFrame.grid(row=rowNo,column=0, sticky = 'NEW')
        self.mainCanvasColorFrame.columnconfigure(1,weight=1)
        
        self.canvasColorLab = ttk.Label(self.mainCanvasColorFrame, text = 'Select canvas color',width=labelSize)
        self.canvasColorLab.grid(row=0,column=0)
        
        self.canvasColorFrame = tk.Frame(self.mainCanvasColorFrame, bg='black')
        self.canvasColorFrame.grid(row=0,column=1, sticky = 'EW')
        self.canvasColorFrame.columnconfigure(0,weight=1)
        self.canvasColorFrame.columnconfigure(1,weight=1)
        
        self.canvasColorSample = ttk.Label(self.canvasColorFrame,text='\u2588\u2588\u2588\u2588', foreground=self.selectedCanvasColor)
        self.canvasColorSample.grid(row=0,column=0)
        
        self.canvasColorButton = ttk.Button(self.canvasColorFrame,text='Color',command=self.SelectCanvasColor)
        self.canvasColorButton.grid(row=0,column=1,padx=3,pady=3)
        
        # Select plot color pane
        rowNo +=1
        self.mainPlotColorFrame = tk.Frame(parent, pady=3, bg = 'blue')
        self.mainPlotColorFrame.grid(row=rowNo,column=0, sticky = 'NEW')
        self.mainPlotColorFrame.columnconfigure(1,weight=1)
        
        self.plotColorLab = ttk.Label(self.mainPlotColorFrame, text = 'Select plot color',width=labelSize)
        self.plotColorLab.grid(row=0,column=0)
        
        self.plotColorFrame = tk.Frame(self.mainPlotColorFrame, bg='black')
        self.plotColorFrame.grid(row=0,column=1, sticky = 'EW')
        self.plotColorFrame.columnconfigure(0,weight=1)
        self.plotColorFrame.columnconfigure(1,weight=1)
        
        self.plotColorSample = ttk.Label(self.plotColorFrame,text='\u2588\u2588\u2588\u2588', foreground=self.selectedPlotColor)
        self.plotColorSample.grid(row=0,column=0)
        
        self.plotColorButton = ttk.Button(self.plotColorFrame,text='Color',command=self.SelectPlotColor)
        self.plotColorButton.grid(row=0,column=1,padx=3,pady=3)
        
        # Select toolbar color pane
        rowNo +=1
        self.mainToolbarColorFrame = tk.Frame(parent, pady=3, bg = 'blue')
        self.mainToolbarColorFrame.grid(row=rowNo,column=0, sticky = 'NEW')
        self.mainToolbarColorFrame.columnconfigure(1,weight=1)
        
        self.xAxisLabLab = ttk.Label(self.mainToolbarColorFrame, text = 'Select toolbar color',width=labelSize)
        self.xAxisLabLab.grid(row=0,column=0)
        
        self.toolbarColorFrame = tk.Frame(self.mainToolbarColorFrame, bg='black')
        self.toolbarColorFrame.grid(row=0,column=1, sticky = 'EW')
        self.toolbarColorFrame.columnconfigure(0,weight=1)
        self.toolbarColorFrame.columnconfigure(1,weight=1)
        
        self.toolbarColorSample = ttk.Label(self.toolbarColorFrame,text='\u2588\u2588\u2588\u2588', foreground=self.selectedToolbarColor)
        self.toolbarColorSample.grid(row=0,column=0)
        
        self.plotColorButton = ttk.Button(self.toolbarColorFrame,text='Color',command=self.SelectToolbarColor)
        self.plotColorButton.grid(row=0,column=1,padx=3,pady=3)
        
        # Button frame
        rowNo +=1
        btnFrame = tk.Frame(parent, pady=5, bg = 'cyan')
        btnFrame.grid(row=rowNo,column=0, sticky = 'NEW')
        btnFrame.columnconfigure(0,weight=1)
        
        cancelBtn = ttk.Button(btnFrame,text = 'Cancel', width = btnSize, command=lambda:self.presenter.ClosePlotOptions(self))
        cancelBtn.grid(row = 0, column=0, sticky = 'E')
        applyBtn = ttk.Button(btnFrame,text = 'Apply', width = btnSize, command=lambda:self.presenter.ApplyPlotOptions(self))
        applyBtn.grid(row = 0, column=1, sticky = 'E')
        okBtn = ttk.Button(btnFrame,text = 'Ok', width = btnSize, command=lambda:self.presenter.OkPlotOptions(self))
        okBtn.grid(row = 0, column=2, sticky = 'E')
        
        
    def UpdateEntry(self,entry:ttk.Entry,txt:str)->None:
        """This function takes whatever entry, deleted the text, and write the new 
        text given as input. """
        # Delete and rewrite the entry text 
        entry.delete(0,tk.END)
        entry.insert(0,txt)
        
                        
    def ValidateLeftMarginEntry(self,event,otherLimit, previousVal)->None:
        '''Validate entries.'''
        # Check if the entry is a number, and if it is right with respect to 
        # its counterpart
        try:
            currentEntry = float(event.widget.get())
            otherEntry = float(otherLimit.get())
            if currentEntry<0 or currentEntry>1:
                self.presenter.PrintError('Entry must be a number between 0 and 1.')
                self.UpdateEntry(event.widget,previousVal)
            
            if currentEntry>=otherEntry:
                self.presenter.PrintError('Left margin must be smaller than right margin.')
                self.UpdateEntry(event.widget,previousVal)
        except:
            self.presenter.PrintError('Entry must be a number between 0 and 1.')
            self.UpdateEntry(event.widget,previousVal)
            
            
    def ValidateRightMarginEntry(self,event,otherLimit, previousVal)->None:
        '''Validate entries.'''
        # Check if the entry is a number, and if it is right with respect to 
        # its counterpart
        try:
            currentEntry = float(event.widget.get())
            otherEntry = float(otherLimit.get())
            if currentEntry<0 or currentEntry>1:
                self.presenter.PrintError('Entry must be a number between 0 and 1.')
                self.UpdateEntry(event.widget,previousVal)
            
            if currentEntry<=otherEntry:
                self.presenter.PrintError('Right margin must be smaller than left margin.')
                self.UpdateEntry(event.widget,previousVal)
        except:
            self.presenter.PrintError('Entry must be a number between 0 and 1.')
            self.UpdateEntry(event.widget,previousVal)
            
            
    def ValidateBottomMarginEntry(self,event,otherLimit, previousVal)->None:
        '''Validate entries.'''
        # Check if the entry is a number, and if it is right with respect to 
        # its counterpart
        try:
            currentEntry = float(event.widget.get())
            otherEntry = float(otherLimit.get())
            if currentEntry<0 or currentEntry>1:
                self.presenter.PrintError('Entry must be a number between 0 and 1.')
                self.UpdateEntry(event.widget,previousVal)
            
            if currentEntry>=otherEntry:
                self.presenter.PrintError('Bottom margin must be smaller than top margin.')
                self.UpdateEntry(event.widget,previousVal)
        except:
            self.presenter.PrintError('Entry must be a number between 0 and 1.')
            self.UpdateEntry(event.widget,previousVal)
            
            
    def ValidateTopMarginEntry(self,event,otherLimit, previousVal)->None:
        '''Validate entries.'''
        # Check if the entry is a number, and if it is right with respect to 
        # its counterpart
        try:
            currentEntry = float(event.widget.get())
            otherEntry = float(otherLimit.get())
            if currentEntry<0 or currentEntry>1:
                self.presenter.PrintError('Entry must be a number between 0 and 1.')
                self.UpdateEntry(event.widget,previousVal)
            
            if currentEntry<=otherEntry:
                self.presenter.PrintError('Top margin must be greater than bottom margin.')
                self.UpdateEntry(event.widget,previousVal)
        except:
            self.presenter.PrintError('Entry must be a number between 0 and 1.')
            self.UpdateEntry(event.widget,previousVal)
 
            
    def SelectCanvasColor(self):
        '''Select canvas color'''
        colorCode = colorchooser.askcolor(title='Select a canvas color')
            
        try:
            self.selectedCanvasColor=colorCode[1]
            self.canvasColorSample.config(foreground=colorCode[1])
            
        except:
            '''Nothing'''
            
            
    def SelectPlotColor(self):
        '''Select plot color'''
        colorCode = colorchooser.askcolor(title='Select a plot color')
            
        try:
            self.selectedPlotColor=colorCode[1]
            self.plotColorSample.config(foreground=colorCode[1])
            
        except:
            '''Nothing'''
      
            
    def SelectToolbarColor(self):
        '''Select toolbar color'''
        colorCode = colorchooser.askcolor(title='Select a toolbar color')
            
        try:
            self.selectedToolbarColor=colorCode[1]
            self.toolbarColorSample.config(foreground=colorCode[1])
            
        except:
            '''Nothing'''
        