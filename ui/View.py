"""
View Module
===========

This module defines the `View` class, which represents the main graphical user
interface for the application. The `View` class is responsible for setting up 
and managing the user interface elements in line with the MVP (Model-View-Presenter)
architecture pattern.

Author: Federico Zappaterra
Version: 1.0.0
Date: 2024-11-05

Classes
-------
View(tk.Tk)
    Represents the main user interface of the application.

"""

import tkinter as tk
from tkinter import ttk 
import customtkinter

from presenter.Presenter import Presenter
from ui.PathSelector import PathSelector
from ui.VerticalScrollText import VerticalScrollText
from ui.AuxBar import AuxBar
from ui.TabManager import TabManager
from ui.ThemeManager import ThemeManager
from ui.ProjectNotebook import ProjectNotebook

# from utilities.MSStyles import applyMSDarkThemeK
import customtkinter
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


# class View(ThemedTk):
class View(customtkinter.CTk):
# class View(tk.Tk):

    """
    Main UI of the application and view element of the MVP framework.
    Inherits from `tk.Tk` and represents the main window of the application.
    """

    def __init__(self) -> None:
        """
        Initialize the graphical interface.
        
        Sets up the main application window, including size and background configuration.
        """
        super().__init__()
        
        # Window title
        self.title("Midnight Science Plotter")
    
        # Set theme
        customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("./utilities/MSdark.json") 
        
        # Get screen width and height
        ws = self.winfo_screenwidth()  # Width of the screen
        hs = self.winfo_screenheight()  # Height of the screen
        
        # Set window dimensions to 70% of screen size
        w = 0.7 * ws
        h = 0.7 * hs

        # Calculate x and y coordinates for positioning
        x = (ws * 0.1)
        y = (hs * 0.1)

        # Set the dimensions and position of the window
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def initView(self, presenter: Presenter) -> None:
        """
        Set up the elements in the graphical interface.
        
        Parameters
        ----------
        presenter : Presenter
            The presenter object that handles the business logic and interaction.
        """
        self.presenter = presenter
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=0)

        # Path selector
        self.pathSelector = PathSelector(self, presenter)
        self.pathSelector.grid(row=0, column=0, sticky='EW')

        # Icon frame
        self.iconFrame = customtkinter.CTkFrame(self)
        self.iconFrame.grid(row=1, column=0, sticky='EW',ipady = 2)
        self.iconFrame.columnconfigure(2, weight=1)

        self.auxBar = AuxBar(self.iconFrame, presenter)
        self.auxBar.grid(row=0, column=0, sticky='EW')

        self.tabManager = TabManager(self.iconFrame, presenter)
        self.tabManager.grid(row=0, column=1, sticky='EW')
        
        self.themeManager = ThemeManager(self.iconFrame, presenter)
        self.themeManager.grid(row=0, column=2, sticky='E')
        self.themeManager.columnconfigure(0, weight=1)

        # Main tabs
        self.projectNotebook = ProjectNotebook(self)
        self.projectNotebook.grid(row=2, column=0, sticky='NEWS', padx=(0, 0), pady=(0, 0))

        # Text widget
        self.textPane = VerticalScrollText(self, height=150)
        self.textPane.text.configure(state='disabled')
        self.textPane.grid(row=3, column=0, sticky='EW', padx=(0, 0), pady=(3, 0))
