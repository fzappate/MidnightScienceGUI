import tkinter as tk
from tkinter import ttk
from tkinter import ttk, colorchooser
import customtkinter

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
        
        labelSize = 150
        btnSize = 100
        entrySize = 50
        padY = 2
        padX = 3
        self.parent = parent
        self.presenter = presenter
        
        self.title = plotModel.name
        leftMargin = plotModel.leftMargin
        rightMargin = plotModel.rightMargin
        bottomMargin = plotModel.bottomMargin
        topMargin = plotModel.topMargin
        self.selectedCanvasColor = plotModel.canvasColor
        self.selectedPlotColor = plotModel.plotColor
        self.selectedToolbarColor = plotModel.toolbarColor
        


        # Title frame
        rowNo = 0
        self.titleFrame = customtkinter.CTkFrame(parent)
        self.titleFrame.grid( row=rowNo, column=0, sticky='NEW')
        self.titleFrame.columnconfigure(1,weight=1)
        
        self.titleLab = customtkinter.CTkLabel(self.titleFrame,text=' Title',anchor = 'w',width=labelSize)
        self.titleLab.grid( row=0, column=0, pady=padY)
        
        self.titleEntry = customtkinter.CTkEntry(self.titleFrame)
        self.titleEntry.grid( row=0, column=1, padx=(padX, padX), sticky='EW')
        self.UpdateEntry(self.titleEntry, self.title)
        self.titleEntry.bind("<FocusOut>",lambda event: self.ValidatePlotTitle( self.titleEntry,self.title))
        self.titleEntry.bind("<Return>",lambda event: self.ValidatePlotTitle( self.titleEntry, self.title))



        # Plot margins
        rowNo +=1
        self.plotMarginsFrame = customtkinter.CTkFrame(parent)
        self.plotMarginsFrame.grid( row=rowNo, column=0, sticky='NEW')
        self.plotMarginsFrame.columnconfigure(1,weight=1)
        
        self.xAxisLimLab = customtkinter.CTkLabel(self.plotMarginsFrame, anchor = 'w',text = ' Set plot margins',width=labelSize)
        self.xAxisLimLab.grid( row=0, column=0,  pady=padY)
        
        self.marginsFrame = customtkinter.CTkFrame(self.plotMarginsFrame)
        self.marginsFrame.grid( row=0, column=1, sticky='EW')
        self.marginsFrame.columnconfigure(0,weight=1)
        self.marginsFrame.columnconfigure(1,weight=1)
        self.marginsFrame.columnconfigure(2,weight=1)
        self.marginsFrame.columnconfigure(3,weight=1)

        self.plotMarginLeft = customtkinter.CTkEntry(self.marginsFrame, width=entrySize)
        self.plotMarginLeft.grid( row=0, column=0, padx=padX, sticky='EW')
        self.UpdateEntry(self.plotMarginLeft, str(leftMargin))
        
        self.plotMarginRight = customtkinter.CTkEntry(self.marginsFrame, width=entrySize)
        self.plotMarginRight.grid(row=0,column=1,padx=padX,sticky='EW')
        self.UpdateEntry(self.plotMarginRight, str(rightMargin))
        
        self.plotMarginBottom = customtkinter.CTkEntry(self.marginsFrame, width=entrySize)
        self.plotMarginBottom.grid(row=0,column=2,padx=padX,sticky='EW')    
        self.UpdateEntry(self.plotMarginBottom, str(bottomMargin))
        
        self.plotMarginTop = customtkinter.CTkEntry(self.marginsFrame, width=entrySize)
        self.plotMarginTop.grid(row=0,column=3,padx=(padX,padX),sticky='EW')    
        self.UpdateEntry(self.plotMarginTop, str(topMargin))
        
        self.plotMarginLeft.bind("<FocusOut>",lambda event: self.ValidateSmallerMarginEntry(self.plotMarginLeft, self.plotMarginRight, leftMargin))
        self.plotMarginLeft.bind("<Return>",lambda event: self.ValidateSmallerMarginEntry(self.plotMarginLeft, self.plotMarginRight, leftMargin))
        self.plotMarginRight.bind("<FocusOut>",lambda event: self.ValidateGreaterMarginEntry(self.plotMarginRight, self.plotMarginLeft, rightMargin))
        self.plotMarginRight.bind("<Return>",lambda event: self.ValidateGreaterMarginEntry(self.plotMarginRight, self.plotMarginLeft, rightMargin))
        self.plotMarginBottom.bind("<FocusOut>",lambda event: self.ValidateSmallerMarginEntry(self.plotMarginBottom, self.plotMarginTop, bottomMargin))
        self.plotMarginBottom.bind("<Return>",lambda event: self.ValidateSmallerMarginEntry(self.plotMarginBottom, self.plotMarginTop, bottomMargin))
        self.plotMarginTop.bind("<FocusOut>",lambda event: self.ValidateGreaterMarginEntry(self.plotMarginTop, self.plotMarginBottom, topMargin))
        self.plotMarginTop.bind("<Return>",lambda event: self.ValidateGreaterMarginEntry(self.plotMarginTop, self.plotMarginBottom, topMargin))
        
     
        # Select canvas color pane
        rowNo +=1
        self.mainCanvasColorFrame = customtkinter.CTkFrame(parent)
        self.mainCanvasColorFrame.grid(row=rowNo,column=0, sticky = 'NEW')
        self.mainCanvasColorFrame.columnconfigure(1,weight=1)
        
        self.canvasColorLab = customtkinter.CTkLabel(self.mainCanvasColorFrame, anchor = 'w',text = ' Select canvas color',width=labelSize)
        self.canvasColorLab.grid(row=0,column=0,  pady=padY)
        
        self.canvasColorFrame = customtkinter.CTkFrame(self.mainCanvasColorFrame)
        self.canvasColorFrame.grid(row=0,column=1, sticky = 'EW')
        self.canvasColorFrame.columnconfigure(0,weight=1)
        self.canvasColorFrame.columnconfigure(1,weight=1)
        
        self.canvasColorSample = customtkinter.CTkLabel(self.canvasColorFrame,text='\u2588\u2588\u2588\u2588')
        self.canvasColorSample.grid(row=0,column=0)
        
        self.canvasColorButton = customtkinter.CTkButton(self.canvasColorFrame,text='Color',command=self.SelectCanvasColor)
        self.canvasColorButton.grid(row=0,column=1)
        
        
        # Select plot color pane
        rowNo +=1
        self.mainPlotColorFrame = customtkinter.CTkFrame(parent)
        self.mainPlotColorFrame.grid(row=rowNo,column=0, sticky = 'NEW')
        self.mainPlotColorFrame.columnconfigure(1,weight=1)
        
        self.plotColorLab = customtkinter.CTkLabel(self.mainPlotColorFrame, text = ' Select plot color', anchor = 'w',width=labelSize)
        self.plotColorLab.grid(row=0,column=0, pady=padY)
        
        self.plotColorFrame = customtkinter.CTkFrame(self.mainPlotColorFrame)
        self.plotColorFrame.grid(row=0,column=1, sticky = 'EW')
        self.plotColorFrame.columnconfigure(0,weight=1)
        self.plotColorFrame.columnconfigure(1,weight=1)
        
        self.plotColorSample = customtkinter.CTkLabel(self.plotColorFrame,text='\u2588\u2588\u2588\u2588')
        self.plotColorSample.grid(row=0,column=0)
        
        self.plotColorButton = customtkinter.CTkButton(self.plotColorFrame,text='Color',command=self.SelectPlotColor)
        self.plotColorButton.grid(row=0,column=1)
        

    
        # Select toolbar color pane
        rowNo +=1
        self.mainToolbarColorFrame = customtkinter.CTkFrame(parent)
        self.mainToolbarColorFrame.grid(row=rowNo,column=0, sticky = 'NEW')
        self.mainToolbarColorFrame.columnconfigure(1,weight=1)
        
        self.xAxisLabLab = customtkinter.CTkLabel(self.mainToolbarColorFrame, text = ' Select toolbar color',anchor = 'w',width=labelSize)
        self.xAxisLabLab.grid(row=0,column=0, pady=padY)
        
        self.toolbarColorFrame = customtkinter.CTkFrame(self.mainToolbarColorFrame)
        self.toolbarColorFrame.grid(row=0,column=1, sticky = 'EW')
        self.toolbarColorFrame.columnconfigure(0,weight=1)
        self.toolbarColorFrame.columnconfigure(1,weight=1)
        
        self.toolbarColorSample = customtkinter.CTkLabel(self.toolbarColorFrame,text='\u2588\u2588\u2588\u2588')
        self.toolbarColorSample.grid(row=0,column=0)
        
        self.plotColorButton = customtkinter.CTkButton(self.toolbarColorFrame,text='Color',command=self.SelectToolbarColor)
        self.plotColorButton.grid(row=0,column=1)
        
        # Button frame
        rowNo +=1
        btnFrame = customtkinter.CTkFrame(parent)
        btnFrame.grid(row=rowNo,column=0, sticky = 'NEW')
        btnFrame.columnconfigure(0,weight=1)
        
        cancelBtn = customtkinter.CTkButton(btnFrame,text = 'Cancel', width = btnSize, command=lambda:self.presenter.ClosePlotOptions(self))
        cancelBtn.grid(row = 0, column=0,padx = padX, pady = (6*padY,padY), sticky = 'E')
        applyBtn = customtkinter.CTkButton(btnFrame,text = 'Apply', width = btnSize, command=lambda:self.ApplyPlotOptions())
        applyBtn.grid(row = 0, column=1,padx = padX,pady = (6*padY,padY), sticky = 'E')
        okBtn = customtkinter.CTkButton(btnFrame,text = 'Ok', width = btnSize, command=lambda:self.presenter.OkPlotOptions(self))
        okBtn.grid(row = 0, column=2,padx = (padX, padX),pady = (6*padY,padY), sticky = 'E')
        
    def ApplyPlotOptions(self)->None:
        '''Run all the validations before applying.'''
        
        err = 0
        err += self.ValidatePlotTitle(self.titleEntry, self.title)
        err += self.ValidateSmallerMarginEntry(self.plotMarginLeft, self.plotMarginRight)
        # err += ValidateRightMarginEntry
        # err += ValidateTopMarginEntry
        # err += ValidateBottomMarginEntry
        
        if not err: 
            self.presenter.ApplyPlotOptions(self)
        
    def UpdateEntry(self,entry:ttk.Entry,txt:str)->None:
        """This function takes whatever entry, deleted the text, and write the new 
        text given as input. """
        # Delete and rewrite the entry text 
        entry.delete(0,tk.END)
        entry.insert(0,txt)
        
        
    def ValidatePlotTitle(self,titleEntry, previousVal):
        '''Make sure that the plot title just entered doesn't already exists.'''
        tabListName = self.presenter.view.projectNotebook.list().copy()
        inputTitle = titleEntry.get()
        
        if inputTitle in tabListName:
            self.UpdateEntry(titleEntry,previousVal)
            return 1
            
        return 0
        
                        
    def ValidateSmallerMarginEntry(self,smallerMarginEntry,greaterMarginEntry, previousVal)->None:
        '''Validate entries.'''
        # Check if the entry is a number, and if it is right with respect to 
        # its counterpart
        try:
            smallerMargin = float(smallerMarginEntry.get())
            greaterMargin = float(greaterMarginEntry.get())
            if smallerMargin<0 or smallerMargin>1:
                self.presenter.PrintError('Entry must be a number between 0 and 1.')
                self.UpdateEntry(smallerMarginEntry,previousVal)
                return 1
            
            if smallerMargin>=greaterMargin:
                self.presenter.PrintError('This margin cannot be greater than ' + str(greaterMargin))
                self.UpdateEntry(smallerMarginEntry,previousVal)
                return 1
            
            return 0
        
        except:
            self.presenter.PrintError('Entry must be a number between 0 and 1.')
            self.UpdateEntry(smallerMarginEntry,previousVal)
            return 1
            
            
    def ValidateGreaterMarginEntry(self,greaterMarginEntry,smallerMarginEntry, previousVal)->None:
        '''Validate entries.'''
        # Check if the entry is a number, and if it is right with respect to 
        # its counterpart
        try:
            greaterMargin = float(greaterMarginEntry.get())
            smallerMargin = float(smallerMarginEntry.get())
            if greaterMargin<0 or greaterMargin>1:
                self.presenter.PrintError('Entry must be a number between 0 and 1.')
                self.UpdateEntry(greaterMarginEntry,previousVal)
                return 1
            
            if greaterMargin<=smallerMargin:
                self.presenter.PrintError('This margin cannot be smaller than ' + str(smallerMargin))
                self.UpdateEntry(greaterMarginEntry,previousVal)
                return 1
            
            return 0
        
        except:
            self.presenter.PrintError('Entry must be a number between 0 and 1.')
            self.UpdateEntry(greaterMarginEntry,previousVal)
            return 1
            
            
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
                return 1
            
            if currentEntry>=otherEntry:
                self.presenter.PrintError('Bottom margin must be smaller than top margin.')
                self.UpdateEntry(event.widget,previousVal)
                return 1
            
            return 0
        
        except:
            self.presenter.PrintError('Entry must be a number between 0 and 1.')
            self.UpdateEntry(event.widget,previousVal)
            return 1
            
            
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
                return 1
            
            if currentEntry<=otherEntry:
                self.presenter.PrintError('Top margin must be greater than bottom margin.')
                self.UpdateEntry(event.widget,previousVal)
                return 1
            
            return 0
        
        except:
            self.presenter.PrintError('Entry must be a number between 0 and 1.')
            self.UpdateEntry(event.widget,previousVal)
            return 1
 
            
    def SelectCanvasColor(self):
        '''Select canvas color'''
        colorCode = colorchooser.askcolor(title='Select a canvas color')
            
        try:
            self.selectedCanvasColor=colorCode[1]
            self.canvasColorSample.configure(text_color=colorCode[1])
            
        except:
            '''Nothing'''
            
            
    def SelectPlotColor(self):
        '''Select plot color'''
        colorCode = colorchooser.askcolor(title='Select a plot color')
            
        try:
            self.selectedPlotColor=colorCode[1]
            self.plotColorSample.configure(text_color=colorCode[1])
            
        except:
            '''Nothing'''
      
            
    def SelectToolbarColor(self):
        '''Select toolbar color'''
        colorCode = colorchooser.askcolor(title='Select a toolbar color')
            
        try:
            self.selectedToolbarColor=colorCode[1]
            self.toolbarColorSample.configure(text_color=colorCode[1])
            
        except:
            '''Nothing'''
        