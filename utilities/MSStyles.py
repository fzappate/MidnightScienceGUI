# styles.py
import tkinter as tk
from tkinter import ttk

# from tkinter import ttk


def applyMSDarkTheme(root):
    
    style = ttk.Style()
    
    # # Get the current default theme
    # current_theme = style.theme_use()  # This will give you the current theme
    # print("Current theme:", current_theme)
    # style.theme_use('darkly')  # This will give you the current theme
    # current_theme = style.theme_use()  # This will give you the current theme
    # print("Current theme:", current_theme)
    # print(style.theme_names())

    # Create a custom theme from scratch
    style.theme_create('MSDarkTheme', parent='vista', settings={
        'TLabel': {
            'configure': {
                'background': '#4CAF50',
                'foreground': 'white',
                'font': ('Helvetica', 12, 'bold'),
                'padding': 10
            }
        }
    })

    # Activate the new custom theme
    style.theme_use('MSDarkTheme')
