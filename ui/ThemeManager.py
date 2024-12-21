import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import customtkinter


class ThemeManager(customtkinter.CTkFrame):
    """
    Nothing yet
    """
    def __init__(self, parent, presenter, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        '''Initialize the aux bar object.'''
        
        iconSize = (30, 30)

        # New project image
        themeIcon = os.path.join(os.getcwd(), './docs/images/themeIcon.png')
        self.themeIcon = customtkinter.CTkImage(Image.open(themeIcon), size = iconSize)
        
        # Change theme button
        colNo = 0 
        themeButton = customtkinter.CTkButton(self, text = '',width = 10,image=self.themeIcon, command = presenter.ChangeTheme)
        themeButton.grid(row=0, column=colNo, padx=(3, 6), ipady=1, ipadx=1)