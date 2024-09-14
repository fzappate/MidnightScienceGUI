import tkinter as tk
from tkinter import ttk 
import pathselector

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


# Root 
root = tk.Tk()
root.title("Path Selector") 
root.geometry('600x400')


pathSel = pathselector.PathSelector(root)



root.mainloop()