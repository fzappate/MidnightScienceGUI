import tkinter as tk
from tkinter import ttk

class SubplotOptions(tk.Frame):
    def __init__(self,parent,*args,**kwargs):
        ''' Initialize a subplot options pane.'''
        super().__init__(parent,*args,**kwargs)
        
        # Title frame
        topLeftFrame = tk.Frame(parent, pady=10, bg = 'red')
        topLeftFrame.grid(row=0,column=0, sticky = 'EW')
        
        titleLab = tk.Label(topLeftFrame, text = 'Title')
        titleLab.grid(row=0,column=0)
        titleEntry = tk.Entry(topLeftFrame)
        titleEntry.grid(row = 0, column=1, sticky = 'EW')

        # Axis labels frame
        midLeftFrame = tk.Frame(parent, bg = 'blue')
        midLeftFrame.grid(row=1,column=0, sticky = 'EW')
        
        xAxisLabLab = tk.Label(midLeftFrame, text = 'X Axis Label')
        xAxisLabLab.grid(row=0,column=0)
        xAxisLabEntry = tk.Entry(midLeftFrame)
        xAxisLabEntry.grid(row = 0, column=1)
        yAxisLabLab = tk.Label(midLeftFrame, text = 'Y Axis Label')
        yAxisLabLab.grid(row=1,column=0)
        yAxisLabEntry = tk.Entry(midLeftFrame)
        yAxisLabEntry.grid(row = 1, column=1)
                
        # Axis limits frame
        midRightFrame = tk.Frame(parent, bg = 'red')
        midRightFrame.grid(row=1,column=1, sticky = 'EW')
        
        xAxisLimLab = tk.Label(midRightFrame, text = 'X Axis Limits')
        xAxisLimLab.grid(row=0,column=0)
        xAxisLowLimEntry = tk.Entry(midRightFrame)
        xAxisLowLimEntry.grid(row=0,column=1)
        xAxisUpLimEntry = tk.Entry(midRightFrame)
        xAxisUpLimEntry.grid(row=0,column=2)    
            
        yAxisLimLab = tk.Label(midRightFrame, text = 'Y Axis Limits')
        yAxisLimLab.grid(row=1,column=0)
        yAxisLowLimEntry = tk.Entry(midRightFrame)
        yAxisLowLimEntry.grid(row=1,column=1)
        yAxisUpLimEntry = tk.Entry(midRightFrame)
        yAxisUpLimEntry.grid(row=1,column=2)
        
        # Grid frame
        botFrame = tk.Frame(parent, pady=10, bg = 'green')
        botFrame.grid(row=2,column=0, sticky = 'EW')
        
        gridLab = tk.Label(botFrame, text = 'Grid')
        gridLab.grid(row=0,column=2)
        gridCheckbox = ttk.Checkbutton(botFrame)
        gridCheckbox.grid(row=0,column=3)
                
        # Button frame
        btnFrame = tk.Frame(parent, pady=10, bg = 'green')
        btnFrame.grid(row=3,column=1, sticky = 'EW')
        
        cancelBtn = ttk.Button(btnFrame,text = 'Cancel', width = 15)
        cancelBtn.grid(row = 0, column=0, sticky = 'E')
        applyBtn = ttk.Button(btnFrame,text = 'Apply', width = 15)
        applyBtn.grid(row = 0, column=1, sticky = 'E')
        okBtn = ttk.Button(btnFrame,text = 'Ok', width = 15)
        okBtn.grid(row = 0, column=2, sticky = 'E')