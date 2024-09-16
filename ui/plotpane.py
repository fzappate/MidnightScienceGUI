import tkinter as tk
from tkinter import ttk 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk


class PlotPane(ttk.Frame):
    '''Class of plot where the GearGen gear set is plot.'''

    def __init__(self,parent,*args, **kwargs)->None:
        super().__init__(parent,*args, **kwargs)
        '''Initialize the GearGen plot object.'''

        # Set the grid option of this object 
        self.plotFrame = tk.Frame(self,bg='red', width=10,height=10)
        self.plotFrame.grid(row=0,column=0,sticky="NEWS")
        self.plotFrame.columnconfigure(0,weight=1)
        self.plotFrame.rowconfigure(0,weight=1)

        # Create a figure
        self.figure = Figure(figsize=(6, 6), dpi=100)
        
        # Create FigureCanvasTkAgg object
        self.canv = FigureCanvasTkAgg(self.figure, self.plotFrame)
        self.canv.draw() 
        self.canv.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Create the toolbar
        NavigationToolbar2Tk(self.canv, self.plotFrame)

        # Create axes        
        self.ax = self.figure.add_subplot()
        self.ax.set_aspect('equal', adjustable='box')

        self.plotFrame.bind("<Configure>", lambda e: self.resize)
        
    
    
    

    def resize(self,event):
            print(self.plotFrame.winfo_width(), self.plotFrame.winfo_height())
            ...







