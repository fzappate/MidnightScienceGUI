from tkinter import ttk
import tkinter as tk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass
    
class FileBar(tk.Frame):
    '''File bar class containing all the buttons of the file bar.'''

    def __init__(self, parent,presenter,*args, **kwargs)->None:
        super().__init__(parent,*args, **kwargs)
        '''Initialize the file bar object.'''
        file_button = ttk.Button(self, text='File', width= 10)
        file_button.grid(row=0, column=0, padx=(3,3))