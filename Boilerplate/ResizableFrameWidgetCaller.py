from tkinter import ttk
import tkinter as tk
import os 
from  resizableframe import *


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass 

                    
# Root 
root = tk.Tk()
root.title("Command Widget") 
root.geometry('600x400')

# Expand topFrame and botFrame horizontally
root.columnconfigure(0,weight = 1)
# Make sure that topFrame takes all the space available in the window
root.rowconfigure(0,weight = 1)

# Divide the main window in top and bottom
# Add top frame
topFrame = tk.Frame(root,bg = 'green')
topFrame.grid(row=0,column=0,sticky = 'NEWS')
# Make sure the central frame takes up all the space available
topFrame.columnconfigure(1,weight=1)
# Make sure that the widgets in topFrame takes up all the vertical space available
topFrame.rowconfigure(0,weight=1)

# Place frames in topFrame
resFrameRight = ResizableFrameRightEdge(topFrame,width = 100, background = "blue")
resFrameRight.grid(row = 0, column=0,sticky = 'NWS')

frame1 = tk.Frame(topFrame, bg= "red")
frame1.grid(row = 0, column = 1,sticky = 'NEWS')

resFrameLeft = ResizableFrameLeftEdge(topFrame,background= "green",width = 100)
resFrameLeft.grid(row = 0, column = 2,sticky = 'NES')

# Add bottom frame
botFrame = ResizableFrameTopEdge(root,bg = 'yellow',height = 100)
botFrame.grid(row=1,column=0,sticky = 'NEWS')

# Implement a notebook inside the first frame
# tab_notebook = ttk.Notebook(resFrameRight)
# # Implement frames inside the notebook
# tab1 = ttk.Frame(tab_notebook)
# tab2 = ttk.Frame(tab_notebook)
# tab_notebook.add(tab1, text='Tab1',sticky='news')
# tab_notebook.add(tab2, text='Tab2',sticky='news')

# tab_notebook.grid(row=0,column=0,sticky='NEWS',padx=(100, 100))
# tab_notebook.grid(row=0,column=0,sticky='NEWS')
# tab_notebook.pack(expand=True, fill="both")


root.mainloop()