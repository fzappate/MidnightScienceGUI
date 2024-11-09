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
    # LEVEL 1
    L1_bg = '#252525'
    L1_fg = '#cccccc'
    
    frame_L1_bg = L1_bg
    
    label_L1_bg = L1_bg
    label_L1_fg = L1_fg
    
    button_L1_bg = L1_bg
    button_L1_fg = L1_fg

    # Create a custom theme from scratch
    style.theme_create('MSDarkTheme', parent='vista', settings={
        'TFrame': {
            'configure':{
                'background': frame_L1_bg
            }
        },
        'TLabel': {
            'configure': {
                'background': label_L1_bg,
                'foreground': label_L1_fg,
            }
        },
        'TButton': {
            'configure':{
                # 'foreground': '#ff0000'
            },
            'map': {
                'background': [('active', '#0000ff')]
            }
        }
    })

    # 'map': {
    #     'background': [('!active', '#ff0000'),('!pressed', '#ff0000'), ('pressed', '#ff0000')],
    #     'foreground': [('active', 'white'), ('pressed', 'white')],
    #     'relief': [('pressed', 'sunken'), ('!pressed', 'raised')]
    # }
            
    # Activate the new custom theme
    style.theme_use('MSDarkTheme')
