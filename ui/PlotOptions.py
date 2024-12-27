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
        
        # Title frame
        rowNo = 0
        self.titleFrame = tk.Frame(parent, pady=3)
        self.titleFrame.grid(row=rowNo,column=0, pady=3, sticky = 'NEW')
        self.titleFrame.columnconfigure(1,weight=1)
        
        self.titleLab = ttk.Label(self.titleFrame,text='Title',width=labelSize)
        self.titleLab.grid(row=0,column=0, pady=3)
        
        self.titleEntry = tk.Entry(self.titleFrame)
        self.titleEntry.grid(row=0,column=1,padx=3,sticky='EW')
        self.UpdateEntry(self.titleEntry, title)

        
                
        # Plot margins
        rowNo +=1
        self.plotMarginsFrame = tk.Frame(parent, pady=3)
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
        
        # Button frame
        rowNo +=1
        btnFrame = tk.Frame(parent, pady=5)
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
        