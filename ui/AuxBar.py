"""
AuxBar Module
=============

This module defines the `AuxBar` class, which represents a file bar in the user interface 
containing buttons for auxiliary functions such as saving, loading, and reloading a project. 
The `AuxBar` class is part of the graphical user interface (GUI) and provides easy access 
to file operations.

Author: Federico Zappaterra
Version: 1.0.0
Date: 2024-11-06

Classes
-------
AuxBar(tk.Frame)
    Represents a file bar containing buttons for saving, loading, and reloading a project.

"""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import customtkinter

class AuxBar(customtkinter.CTkFrame):
    """
    A tkinter Frame widget representing a file bar with buttons for auxiliary functions 
    such as saving, loading, and reloading a project.

    Attributes:
        saveIcon (PhotoImage): Icon for the save button.
        loadIcon (PhotoImage): Icon for the load button.
        reloadIcon (PhotoImage): Icon for the reload button.
    
    Methods:
        __init__(parent, presenter, *args, **kwargs):
            Initializes the AuxBar with buttons for saving, loading, and reloading a project.
    """

    def __init__(self, parent, presenter, *args, **kwargs) -> None:
        """
        Initializes the AuxBar with buttons for file operations.

        Args:
            parent (tk.Widget): The parent widget to place this frame.
            presenter: The presenter object that handles the logic for saving, 
                       loading, and reloading the project.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments for further customization of the frame.
        """
        super().__init__(parent, *args, **kwargs)
        '''Initialize the aux bar object.'''
        
        iconSize = (30, 30)

        # Load save image
        saveIconPath = os.path.join(os.getcwd(), './images/saveIcon.png')
        self.saveIcon = customtkinter.CTkImage(Image.open(saveIconPath), size = iconSize)

        # Load load image
        loadIconPath = os.path.join(os.getcwd(), './images/loadIcon.png')
        self.loadIcon = customtkinter.CTkImage(Image.open(loadIconPath), size = iconSize)
        
        # Load reload image
        reloadIconPath = os.path.join(os.getcwd(), './images/reloadIcon.png')
        self.reloadIcon = customtkinter.CTkImage(Image.open(reloadIconPath), size = iconSize)

        # Save button 
        save_button = customtkinter.CTkButton(self, text = '',width = 10,image=self.saveIcon, command=presenter.SaveProjectModel)
        save_button.grid(row=0, column=0, padx=(3, 3), ipady=1, ipadx=1)

        # Load button
        load_button = customtkinter.CTkButton(self, text = '',width = 10, image=self.loadIcon, command=presenter.LoadProject)
        load_button.grid(row=0, column=1, padx=(3, 3), ipady=1, ipadx=1)
        