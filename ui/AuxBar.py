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

        # New project image
        newProjIconPath = os.path.join(os.getcwd(), './docs/images/newProjIcon.png')
        self.newProjIconPath = customtkinter.CTkImage(Image.open(newProjIconPath), size = iconSize)

        # Save image
        saveProjIconPath = os.path.join(os.getcwd(), './docs/images/saveProjIcon.png')
        self.saveProjIconPath = customtkinter.CTkImage(Image.open(saveProjIconPath), size = iconSize)
        
        # Load image
        loadProjIconPath = os.path.join(os.getcwd(), './docs/images/loadProjIcon.png')
        self.loadProjIconPath = customtkinter.CTkImage(Image.open(loadProjIconPath), size = iconSize)
        

        # New project button 
        colNo = 0 
        # save_button = customtkinter.CTkButton(self, text = '',width = 10,image=self.newProjIconPath, command=presenter.CreateNewProject)
        # save_button.grid(row=0, column=colNo, padx=(3, 3), ipady=1, ipadx=1)
        
        # Save button 
        # colNo +=1
        save_button = customtkinter.CTkButton(self, text = '',width = 10,image=self.saveProjIconPath, command=presenter.SaveProjectModel)
        save_button.grid(row=0, column=colNo, padx=(3, 3), ipady=1, ipadx=1)

        # Load button
        colNo +=1
        load_button = customtkinter.CTkButton(self, text = '',width = 10, image=self.loadProjIconPath, command=presenter.LoadExistingProject)
        load_button.grid(row=0, column=colNo, padx=(3, 3), ipady=1, ipadx=1)
        