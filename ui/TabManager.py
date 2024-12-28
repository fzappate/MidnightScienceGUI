"""
TabManager Module
=================

This module defines the `TabManager` class, which is responsible for providing a user 
interface for managing tabs in the application. The `TabManager` class includes buttons 
for adding, configuring, and deleting plot tabs. It is part of the graphical user interface 
(GUI) and interacts with the presenter to perform tab management operations.

Author: Federico Zappaterra
Version: 1.0.0
Date: 2024-11-06

Classes
-------
TabManager(tk.Frame)
    Represents a widget for managing tabs with options to add, configure, and delete them.

"""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class TabManager(tk.Frame):    
    """
    A tkinter Frame widget that provides options for managing tabs. This includes buttons
    for adding, configuring, and deleting plot tabs.

    Attributes:
        addButton (ttk.Button): Button for adding a new plot tab.
        optsButton (ttk.Button): Button for configuring the options of a plot tab.
        delButton (ttk.Button): Button for deleting the current plot tab.
    
    Methods:
        __init__(parent, presenter, *args, **kwargs):
            Initializes the TabManager with buttons for tab management operations.
    """
    
    def __init__(self,
                 parent,
                 presenter,
                 *args,
                 **kwargs):
        """
        Initializes the TabManager with buttons for adding, configuring, and deleting plot tabs.

        Args:
            parent (tk.Widget): The parent widget to place this frame.
            presenter: The presenter object that handles the logic for adding and deleting plot tabs.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments for further customization of the frame.
        """
        super().__init__(parent, *args, **kwargs)
        '''Initialize TabManager options widget.'''
        
        self.presenter = presenter
        
        iconSize = (30, 30)

        # Load add tab image
        addTabIconPath = os.path.join(os.getcwd(), self.presenter.ResourcePath('./assets/newTabIcon.png'))
        self.addTabIcon = Image.open(addTabIconPath)
        self.addTabIcon = self.addTabIcon.resize(iconSize)
        self.addTabIcon = ImageTk.PhotoImage(self.addTabIcon)

        # # Load load image
        delTabIconPath = os.path.join(os.getcwd(), self.presenter.ResourcePath('./assets/delTabIcon.png'))
        self.delTabIcon = Image.open(delTabIconPath)
        self.delTabIcon = self.delTabIcon.resize(iconSize)
        self.delTabIcon = ImageTk.PhotoImage(self.delTabIcon)
        
        # # Load reload image
        optsTabIconPath = os.path.join(os.getcwd(), self.presenter.ResourcePath('./assets/optsTabIcon.png'))
        self.optsTabIcon = Image.open(optsTabIconPath)
        self.optsTabIcon = self.optsTabIcon.resize(iconSize)
        self.optsTabIcon = ImageTk.PhotoImage(self.optsTabIcon)
        
        # Add button to add a new plot tab
        self.addButton = ttk.Button(self, text='Add', image=self.addTabIcon, command=presenter.AddPlotTab)
        self.addButton.grid(row=0, column=0, padx=(3, 3), ipady=1, ipadx=1, sticky='NEWS')
        
        # Options button for tab configuration (functionality can be added later)
        self.optsButton = ttk.Button(self, image=self.optsTabIcon, command = lambda: self.presenter.OpenPlotOptions(self.optsButton))
        self.optsButton.grid(row=0, column=1, padx=(3, 3), ipady=1, ipadx=1, sticky='NEWS')
        
        # Delete button to remove the current plot tab
        self.delButton = ttk.Button(self, image=self.delTabIcon, command=presenter.DeletePlotTab)
        self.delButton.grid(row=0, column=2, padx=(3, 3), ipady=1, ipadx=1, sticky='NEWS')
