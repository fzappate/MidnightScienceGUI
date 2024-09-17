import tkinter as tk
from tkinter import ttk 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk


class PlotPane(tk.Frame):
    '''Class of plot where the GearGen gear set is plot.'''

    def __init__(self,parent,*args, **kwargs)->None:
        super().__init__(parent,*args, **kwargs)
        '''Initialize the GearGen plot object.'''
        
        x = [1, 2, 3, 4]
        y1 = [1, 2, 3, 4]
        y2 = [4, 3, 2, 1]

        # Adjust rows and columns weight of PlotPane frame
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        # Create a figure
        self.figure = Figure( dpi=100, facecolor = 'cyan')
        
        # Create FigureCanvasTkAgg object
        self.canv = FigureCanvasTkAgg(self.figure, self)
        self.canv.get_tk_widget().config(bg= 'green')
        self.canv.draw() 
        self.canv.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Create the toolbar
        NavigationToolbar2Tk(self.canv, self)

        # Create axes        
        self.ax = self.figure.add_subplot()
        self.ax.set_aspect('auto')
        
        self.ax.plot(x,y1)

        self.bind("<Configure>", lambda e: self.resize)
        
    
    
    

    def resize(self,event):
        print("ciaooo")
        print(self.plotFrame.winfo_width(), self.plotFrame.winfo_height())
        ...







