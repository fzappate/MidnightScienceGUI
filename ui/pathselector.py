"""
PathSelector Module
===================

This module defines the `PathSelector` class, which represents a user interface 
element for selecting and displaying a project working folder. The `PathSelector` 
class is a part of the graphical user interface (GUI) and follows the MVP (Model-View-Presenter) 
architecture pattern, where it interacts with the `Presenter` class to handle the 
logic of setting and browsing project folder paths.

Author: Federico Zappaterra
Version: 1.0.0
Date: 2024-11-06

Classes
-------
PathSelector(tk.Frame)
    A tkinter Frame widget that provides a user interface for selecting and displaying
    the working folder for a project.
"""
import tkinter as tk
from tkinter import ttk

from presenter.presenter import Presenter

# Try to set the process DPI awareness on Windows for proper scaling
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class PathSelector(tk.Frame):
    """
    A tkinter Frame widget that provides a user interface for selecting and displaying 
    a working folder for a project.

    Attributes:
        lab (ttk.Label): Label widget that displays the text "Working Folder".
        pathEntry (ttk.Entry): Entry widget for the user to view or manually input the 
                                path to the project folder.
        navigate (ttk.Button): Button widget to allow the user to browse for a folder.
    
    Methods:
        __init__(parent, presenter: Presenter, *args, **kwargs): 
            Initializes the PathSelector frame with a label, entry field, and button.
        (None): The following three widgets are placed within the grid layout of the frame.
            - lab: A label indicating the "Working Folder".
            - pathEntry: An entry widget with the default path set to the project's folder.
            - navigate: A button that triggers browsing for a folder.

    Example usage:
        path_selector = PathSelector(parent_frame, presenter_object)
    """

    def __init__(self, parent, presenter: Presenter, *args, **kwargs):
        """
        Initializes the PathSelector frame.

        Args:
            parent (tk.Widget): The parent widget to place this frame.
            presenter (Presenter): The presenter object that handles logic for setting
                                   and browsing project folders.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments for further customization of the frame.
        """
        super().__init__(parent, *args, **kwargs)
        '''Initialize the path selector.'''

        # Configure the grid layout to ensure proper resizing of widgets
        self.columnconfigure(0, weight=0)  # Label column (fixed size)
        self.columnconfigure(1, weight=1)  # Entry column (expandable)
        self.columnconfigure(2, weight=0)  # Button column (fixed size)

        # Create and place the label for the "Working Folder" text
        self.lab = ttk.Label(self, text='Working Folder', width=20)

        # Create the entry widget for displaying and editing the folder path
        self.pathEntry = ttk.Entry(self)
        self.pathEntry.insert(0, presenter.model.settings.projectFolder)  # Set default path
        # Bind events to handle folder setting when Enter key or focus loss occurs
        self.pathEntry.bind('<Return>', presenter.SetWorkingFolderManually)
        self.pathEntry.bind('<FocusOut>', presenter.SetWorkingFolderManually)

        # Create the "Browse..." button to allow the user to select a folder
        self.navigate = ttk.Button(self, text="Browse..", command=lambda: presenter.BrowseProjectFolder())

        # Grid layout to position the widgets in the frame
        self.lab.grid(row=0, column=0, padx=(3, 3))  # Label in column 0
        self.pathEntry.grid(row=0, column=1, sticky="EW", padx=(3, 3))  # Entry in column 1 (expandable)
        self.navigate.grid(row=0, column=2, padx=(3, 3))  # Button in column 2
