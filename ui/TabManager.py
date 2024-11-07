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
        '''Initialize TabManager options widget.'''
        super().__init__(parent, *args, **kwargs)
        
        # Add button to add a new plot tab
        self.addButton = ttk.Button(self, text='Add', command=presenter.AddPlotTab)
        self.addButton.grid(row=0, column=0, sticky='NEWS')
        
        # Options button for tab configuration (functionality can be added later)
        self.optsButton = ttk.Button(self, text='Opts')
        self.optsButton.grid(row=0, column=1, sticky='NEWS')
        
        # Delete button to remove the current plot tab
        self.delButton = ttk.Button(self, text='Canc', command=presenter.DeletePlotTab)
        self.delButton.grid(row=0, column=2, sticky='NEWS')
