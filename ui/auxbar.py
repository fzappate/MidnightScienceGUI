from tkinter import ttk
from tkinter import PhotoImage
import tkinter as tk
from PIL import Image,ImageTk
import os
class AuxBar(tk.Frame):
    '''File bar class containing all the buttons for the auxiliary functions.'''

    def __init__(self, parent,presenter,*args, **kwargs)->None:
        super().__init__(parent,*args, **kwargs)
        '''Initialize the aux bar object.'''
        
        iconSize = (30, 30)

        # Load save image
        saveIconPath = os.path.join(os.getcwd(),'.\images\saveIcon.png')
        self.saveIcon = Image.open(saveIconPath)
        self.saveIcon = self.saveIcon.resize(iconSize)
        self.saveIcon = ImageTk.PhotoImage(self.saveIcon)

        # Load load image
        loadIconPath = os.path.join(os.getcwd(),'.\images\loadIcon.png')
        self.loadIcon = Image.open(loadIconPath)
        self.loadIcon = self.loadIcon.resize(iconSize)
        self.loadIcon = ImageTk.PhotoImage(self.loadIcon)
        
        # Load reload image
        reloadIconPath = os.path.join(os.getcwd(),'./images/reloadIcon.png')
        self.reloadIcon = Image.open(reloadIconPath)
        self.reloadIcon = self.reloadIcon.resize(iconSize)
        self.reloadIcon = ImageTk.PhotoImage(self.reloadIcon)

        # Save button 
        save_button = ttk.Button(self, image=self.saveIcon, command=presenter.SaveProjectModel)
        save_button.grid(row=0, column=0, padx=(3,3), ipady=1, ipadx=1)

        # Load button
        load_button = ttk.Button(self, image=self.loadIcon)
        load_button = ttk.Button(self, image=self.loadIcon,command=presenter.LoadProject)
        load_button.grid(row=0, column=1, padx=(3,3), ipady=1, ipadx=1)
        
        # Reload button
        # reload_button = ttk.Button(self, image=self.reloadIcon, command = presenter.ReloadResults)
        # # reload_button = ttk.Button(self, image=self.reloadIcon,command=xxx)
        # reload_button.grid(row=0, column=2, padx=(3,3), ipady=1, ipadx=1)