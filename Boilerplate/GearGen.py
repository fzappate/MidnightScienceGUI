import tkinter as tk
from tkinter import ttk

from ControlWidgets import TestControlWidget
from geargenplot import GearGenPlot
from geargenplotcontrols import GearGenPlotControls

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass

class GearGenerator():
    def __init__(self, parent):

        self.parent = parent
        self.parent.rowconfigure(0,weight = 1)
        self.parent.columnconfigure(0,weight=0)
        self.parent.columnconfigure(1,weight=1)

        # Control frame ==================================================
        self.controlFrame = ttk.Frame(self.parent)
        self.controlFrame.grid(row=0,column=0,sticky="NS")
        self.controlFrame.rowconfigure(0,weight=1)
        self.controlPanel = ControlWidgets.TestControlWidget(self.controlFrame)

        # Results frame ==================================================
        self.resultsFrame = ttk.Frame(self.parent)
        self.resultsFrame.grid(row=0,column=1,sticky="NEWS")
        self.resultsFrame.rowconfigure(0,weight=1)
        self.resultsFrame.columnconfigure(0,weight=1)
        self.resultsFrame.columnconfigure(1,weight=0)

        # Plot frame 
        plotFrame = ttk.Frame(self.resultsFrame)
        plotFrame.grid(row=0,column=0)
        gearPlot = GearGenPlot(plotFrame)

        # Setting frame 
        settingFrame = ttk.Labelframe(self.resultsFrame,text="Plot Settings")
        settingFrame.grid(row=0,column=1,sticky="NS")
        controls = GearGenPlotControls(settingFrame,gearPlot)

        # lab2 = ttk.Label(self.resultsFrame, text = 'results frame')
        # lab2.grid(row=0,column=0)