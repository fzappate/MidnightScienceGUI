import tkinter as tk
from tkinter import ttk, colorchooser

class SignalOptions(tk.Frame):
    def __init__(self,
                 parent,
                 presenter,
                 signal,
                 sigIndx,
                 resIndx,
                 subplotIndx,
                 *args,
                 **kwargs):
        '''Initialzie signal options widget.'''
        super().__init__(parent,*args,**kwargs)
        
        self.signal = signal
        self.parent = parent
        self.sigIndx = sigIndx
        self.resIndx = resIndx
        self.subplotIndx = subplotIndx
        self.presenter = presenter
        self.selectedColor = signal.color
        
        self.columnconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        
        # Handy numbers
        self.optsWidth=10
        self.btnSize = 6
        self.lineWidthOptsList = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
        self.lineStyleOptsList = ['-','--',':','-.']
        self.lineMarkerSymbolList = ['',
                                     '\u2022', # •
                                     '\u25CF', # ●
                                     '\u25A0', # ■ 
                                     '\u25B2', # ▲
                                     '\u25BC', # ▼
                                     '\u2731', # ✱ 
                                     '\u271A', # ✚
                                     '\u2716', # ✖
                                     '\u25C6', # ◆
                                     '\u25B7', # ▶ 
                                     '\u25C1'] # ◀
                                     
        
        self.lineMarkerOptsList = ['None','.','o','s','^','v','*','+','x','D','>','<']
        
        # OPTIONS FRAME
        self.optsFrame = tk.Frame(self,width=self.optsWidth)
        self.optsFrame.columnconfigure(0,weight=1)
        self.optsFrame.grid(row=0,column=0,sticky='NEWS')
        
        # Select color
        rowNo = 0
        self.colorLabel = ttk.Label(self.optsFrame,text='Select Color')
        self.colorLabel.grid(row=rowNo,column=0,pady=3,sticky='EW')
        
        self.colorFrame = ttk.Frame(self.optsFrame)
        self.colorFrame.grid(row=rowNo,column=1,sticky='EW')
        self.colorFrame.columnconfigure(0,weight=1)
        
        self.colorSample = ttk.Label(self.colorFrame,text='\u2588\u2588\u2588\u2588', foreground=self.selectedColor)
        self.colorSample.grid(row=0,column=0)
        
        self.colorButton = ttk.Button(self.colorFrame,text='Color',width=self.btnSize,command=self.OpenColorChooser)
        self.colorButton.grid(row=rowNo,column=1,padx=3,pady=3,sticky='E')
        
        # Select line width
        rowNo+=1
        self.lineWidthLabel = ttk.Label(self.optsFrame,text='Select Line Width')
        self.lineWidthLabel.grid(row=rowNo, column=0,pady=3,sticky='EW')
        
        self.lineWidthCb = ttk.Combobox(self.optsFrame,values=self.lineWidthOptsList,width=self.optsWidth,state="readonly")
        self.lineWidthCb.grid(row = rowNo, column=1,padx=3,pady=3)
        self.lineWidthCb.set(self.signal.width)
        
        # Select line style
        rowNo+=1
        self.lineStyleLabel = ttk.Label(self.optsFrame,text='Select Line Style')
        self.lineStyleLabel.grid(row=rowNo,column=0,pady=3,sticky='EW')
        
        self.lineStyleCb = ttk.Combobox(self.optsFrame,values=self.lineStyleOptsList,width=self.optsWidth,state="readonly")
        self.lineStyleCb.grid(row=rowNo,column=1,padx=3,pady=3)
        self.lineStyleCb.set(self.signal.style)
        
        # Select line marker
        rowNo+=1
        self.lineMarkerLabel = ttk.Label(self.optsFrame,text='Select Line Marker')
        self.lineMarkerLabel.grid(row=rowNo,column=0,pady=3,sticky='EW')
        
        self.lineMarkerCb = ttk.Combobox(self.optsFrame,values=self.lineMarkerSymbolList, width = self.optsWidth,state="readonly")
        self.lineMarkerCb.grid(row=rowNo,column=1,padx=3,pady=3)
        markerIndx = self.lineMarkerOptsList.index(self.signal.marker)
        markerSymbol = self.lineMarkerSymbolList[markerIndx]
        self.lineMarkerCb.set(markerSymbol)
        
        # BUTTON FRAME
        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.grid(row=1,column=0,sticky='EW')
        self.buttonFrame.columnconfigure(0,weight=1)
        
        self.cancelButton = ttk.Button(self.buttonFrame,
                                       text='Cancel',
                                       width=self.btnSize,
                                      command=lambda: self.presenter.CloseSignalOptions(self))
        self.cancelButton.grid(row=0,column=0,sticky='E')
        
        self.applyButton = ttk.Button(self.buttonFrame,
                                      text='Apply',
                                      width=self.btnSize,
                                      command=lambda: self.presenter.ApplySignalOptions(self))
        self.applyButton.grid(row=0,column=1)
        
        self.okButton = ttk.Button(self.buttonFrame,
                                   text='Ok',
                                   width=self.btnSize,
                                   command=lambda: self.presenter.OkSignalOptions(self))
        self.okButton.grid(row=0,column=2)
        
    def OpenColorChooser(self):
        '''Open color chooser.'''
        colorCode = colorchooser.askcolor(title='Select a color')
        try:
            self.selectedColor=colorCode[1]
            self.colorSample.config(foreground=colorCode[1])
            
        except:
            print("color not selected")
            
    def GetMarkerOpts(self):
        '''Get marker options.'''
        markerSymbol = self.lineMarkerCb.get()
        symbolIndx = self.lineMarkerSymbolList.index(markerSymbol)
        return self.lineMarkerOptsList[symbolIndx]
        
            
            
        
    