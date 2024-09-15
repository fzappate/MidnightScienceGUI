import tkinter as tk
from tkinter import ttk

from include.geomcodeinputsui import GeomCodeInputsUI


class GeomCodeModuleUI(ttk.Frame): 
    def __init__(self,parent,presenter)->None:
        super().__init__(parent)
        
        # Allow the tab to stretch in all direction
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)

        # Input panel must be placed in a canvas to use the scroll bar
        self.inputCanvas = tk.Canvas(self)
        self.inputCanvas.columnconfigure(0,weight=1)

        self.inputsPanel = GeomCodeInputsUI(self.inputCanvas,presenter)

        self.scrollbar=ttk.Scrollbar(self,orient="vertical", command=self.inputCanvas.yview)

        self.inputCanvas.configure(yscrollcommand=self.scrollbar.set)
        # Create an handle for the frame window so that it can be configured later 
        self.internal = self.inputCanvas.create_window((0, 0), window=self.inputsPanel, anchor="nw")

        self.scrollbar.grid(row=0,column=1,sticky='NSE')
        self.inputCanvas.grid(row=0,column=0,sticky='NEWS')

        # Bind methods
        # Horizontally stretch the frame inside the canvas to fill the canvas when it is resized
        self.inputCanvas.bind("<Configure>", lambda e: self.inputCanvas.itemconfig(self.internal, width=e.width))
        # Scroll bar configures 
        self.inputsPanel.bind("<Configure>",lambda e: self.inputCanvas.configure(scrollregion=self.inputsPanel.bbox("all")))
        self.inputsPanel.bind('<Enter>', self.boundToMouseWheel)
        self.inputsPanel.bind('<Leave>', self.unboundToMouseWheel)

        # Run button 
        self.runButton = ttk.Button(self,text = 'Run')
        self.runButton.grid(row=1,column=0,sticky='E')


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
        


