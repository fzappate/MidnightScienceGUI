import tkinter as tk
from tkinter import ttk 

import ControlWidgets

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass

# Root 
root = tk.Tk()
root.title("Command Widget") 
# root.geometry('600x400')
root.rowconfigure(0,weight=1)

# Inputs frame
command_frame = ttk.Frame(root)
command_frame.grid(row=0,column=0,sticky="NS")
# command_frame.grid(row=0,column=0, sticky = 'NS')
commandWidget = ControlWidgets.TestControlWidget(command_frame)

root.mainloop()