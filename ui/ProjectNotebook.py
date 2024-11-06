import tkinter as tk
from tkinter import ttk

class ProjectNotebook(ttk.Notebook):
    '''Class of widget containing the notebook with the tab of the GUI.'''

    def __init__(self,parent,*args, **kwargs)->None:
        super().__init__(parent,*args, **kwargs)
        '''Initialize the notebook widget of the application UI.'''