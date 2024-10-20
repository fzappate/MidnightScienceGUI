import tkinter as tk
from tkinter import ttk, colorchooser

class SignalOptions(tk.Frame):
    def __init__(self,
                 parent,
                 *args,
                 **kwargs):
        '''Initialzie signal options widget.'''
        super().__init__(parent,*args,**kwargs)
        
        self.columnconfigure(0,weight=1)
        
        # Handy numbers
        self.optsWidth=10
        self.btnSize = 6
        self.lineWidthOptsList = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
        self.lineStyleOptsList = ['-','--',':','-.']
        self.lineMarkerOptsList = ['','.','o','s','^','v','*','+','x','D','>','<']
        
        # OPTIONS FRAME
        self.optsFrame = tk.Frame(self)
        self.optsFrame.columnconfigure(0,weight=1)
        self.optsFrame.grid(row=0,column=0)
        
        # Select color
        rowNo = 0
        self.colorLabel = ttk.Label(self.optsFrame,text='Select Color')
        self.colorLabel.grid(row=rowNo,column=0,pady=3,sticky='EW')
        
        self.colorButton = ttk.Button(self.optsFrame,text='Color',command=self.OpenColorChooser)
        self.colorButton.grid(row=rowNo,column=1,padx=3,pady=3,sticky='EW')
        
        # Select line width
        rowNo+=1
        self.lineWidthLabel = ttk.Label(self.optsFrame,text='Select Line Width')
        self.lineWidthLabel.grid(row=rowNo, column=0,pady=3,sticky='EW')
        
        self.lineWidthCb = ttk.Combobox(self.optsFrame,values=self.lineWidthOptsList,width=self.optsWidth,state="readonly")
        self.lineWidthCb.grid(row = rowNo, column=1,padx=3,pady=3)
        self.lineWidthCb.current(1)
        
        # Select line style
        rowNo+=1
        self.lineStyleLabel = ttk.Label(self.optsFrame,text='Select Line Style')
        self.lineStyleLabel.grid(row=rowNo,column=0,pady=3,sticky='EW')
        
        self.lineStyleCb = ttk.Combobox(self.optsFrame,values=self.lineStyleOptsList,width=self.optsWidth,state="readonly")
        self.lineStyleCb.grid(row=rowNo,column=1,padx=3,pady=3)
        self.lineStyleCb.current(0)
        
        # Select line marker
        rowNo+=1
        self.lineMarkerLabel = ttk.Label(self.optsFrame,text='Select Line Marker')
        self.lineMarkerLabel.grid(row=rowNo,column=0,pady=3,sticky='EW')
        
        self.lineMarkerCb = ttk.Combobox(self.optsFrame,values=self.lineMarkerOptsList, width = self.optsWidth,state="readonly")
        self.lineMarkerCb.grid(row=rowNo,column=1,padx=3,pady=3)
        self.lineMarkerCb.current(0)
        
        # BUTTON FRAME
        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.grid(row=1,column=0,sticky='EW')
        self.buttonFrame.columnconfigure(0,weight=1)
        
        self.cancelButton = ttk.Button(self.buttonFrame,text='Cancel',width=self.btnSize)
        self.cancelButton.grid(row=0,column=0,sticky='E')
        
        self.applyButton = ttk.Button(self.buttonFrame,text='Apply',width=self.btnSize)
        self.applyButton.grid(row=0,column=1)
        
        self.okButton = ttk.Button(self.buttonFrame,text='Ok',width=self.btnSize)
        self.okButton.grid(row=0,column=2)
        
    def OpenColorChooser(self)->None:
        '''Open color chooser.'''
        colorCode = colorchooser.askcolor(title='Select a color')
    