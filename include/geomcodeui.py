import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass

class GeomCodeUI(ttk.Frame):
    '''Object containing the GUI of the geometry code.'''

    def __init__(self,parent,presenter)->None:
        super().__init__(parent)
        '''Initialize the GeomCode UI.'''
      
        print('ciao')