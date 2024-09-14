from tkinter import ttk
from tkinter import PhotoImage
import tkinter as tk
from PIL import Image,ImageTk
import os
class AuxBar(ttk.Frame):
    '''File bar class containing all the buttons for the auxiliary functions.'''

    def __init__(self, parent,presenter)->None:
        '''Initialize the aux bar object.'''
        super().__init__(parent)
        
        iconSize = (30, 30)

        # Load save image
        saveIconPath = os.path.join(os.getcwd(),'MainMVP\images\saveIcon.png')
        self.saveIcon = Image.open(saveIconPath)
        self.saveIcon = self.saveIcon.resize(iconSize)
        self.saveIcon = ImageTk.PhotoImage(self.saveIcon)

        # Load load image
        loadIconPath = os.path.join(os.getcwd(),'MainMVP\images\loadIcon.png')
        self.loadIcon = Image.open(loadIconPath)
        self.loadIcon = self.loadIcon.resize(iconSize)
        self.loadIcon = ImageTk.PhotoImage(self.loadIcon)

        # Save button 
        save_button = tk.Button(self, image=self.saveIcon,command=presenter.SaveGearGenData)
        save_button.grid(row=0, column=0,   ipady=1, ipadx=1)

        # Load buttion
        load_button = ttk.Button(self, image=self.loadIcon,command=presenter.LoadData)
        load_button.grid(row=0, column=1, ipady=1, ipadx=1)