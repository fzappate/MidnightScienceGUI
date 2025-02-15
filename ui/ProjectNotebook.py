"""
ProjectNotebook Module
======================

This module defines the `ProjectNotebook` class, which is a custom widget that 
represents a notebook containing the tab structure of the graphical user interface (GUI).
The notebook is dynamically populated in runtime by the presenter, which adds or modifies
the tabs as necessary.

Author: Federico Zappaterra
Version: 1.0.0
Date: 2024-11-06

Classes
-------
ProjectNotebook(ttk.Notebook)
    A custom notebook widget that manages the tabs for the application's user interface.

"""
import tkinter as tk
from tkinter import ttk

class ProjectNotebook(ttk.Notebook):
    """
    A custom ttk.Notebook widget that manages the tabs for the application. 
    The notebook is filled with tabs at runtime by the presenter.

    Attributes:
        None (inherited from ttk.Notebook): Inherits attributes from ttk.Notebook to manage 
                                             and display tabs.

    Methods:
        __init__(parent, *args, **kwargs):
            Initializes the ProjectNotebook widget and prepares it to hold dynamic tabs.

    Example usage:
        notebook = ProjectNotebook(parent_widget)
    """
    
    def __init__(self, parent, presenter, *args, **kwargs) -> None:
        """
        Initializes the ProjectNotebook widget, which will be populated with tabs 
        dynamically by the presenter.

        Args:
            parent (tk.Widget): The parent widget where this notebook will be placed.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments for further customization of the widget.
        """
        '''Initialize the notebook widget of the application UI.'''
        super().__init__(parent, *args, **kwargs)
        
        self.bind("<<NotebookTabChanged>>", presenter.UpdateSelectedTabIndx)
