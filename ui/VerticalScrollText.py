"""
Module: VerticalScrollText

This module contains the `VerticalScrollText` class, which is a custom widget 
that combines a Tkinter Text widget with a vertical scrollbar. The class is 
derived from `ResizableFrameTopEdge`, allowing for resizing the widget by dragging 
its top edge. This widget is particularly useful for displaying multi-line text 
with scrollable content, while also offering the flexibility of resizing.

Usage:
    - This widget can be used in any Tkinter-based application where a 
      scrollable text box with resizing capabilities is needed.
    - The widget automatically integrates a vertical scrollbar with the Text widget.
"""

import tkinter as tk
from tkinter import ttk 
from ui.resizableframe import ResizableFrameTopEdge

class VerticalScrollText(ResizableFrameTopEdge):
    '''Text object with vertical scroll.'''

    def __init__(self, parent, *args, **kwargs):
        """
        Initialize the text object with a vertical scrollbar. This class combines 
        a Tkinter Text widget with a vertical scrollbar, and is based on the 
        ResizableFrameTopEdge class, allowing resizing by dragging the top edge.

        Arguments:
        - parent: The parent widget (typically a Tkinter window or frame)
        - *args, **kwargs: Additional arguments passed to the parent class (ResizableFrameTopEdge)

        Example usage:
        root = tk.Tk()
        vertical_scroll_text = VerticalScrollText(root, background="lightgray", width=400, height=300)
        vertical_scroll_text.grid(row=0, column=0, sticky="NEWS")
        """
        super().__init__(parent, *args, **kwargs)  # Initialize the parent class (ResizableFrameTopEdge)
        '''Initialize the text object with vertical scroll.'''
        
        # Set the grid configuration of this object (to make it resizable)
        self.columnconfigure(0, weight=1)  # Make the first column expand
        self.rowconfigure(0, weight=1)  # Make the first row expand

        # Create the Text widget for multi-line input
        self.text = tk.Text(self)
        self.text.grid_rowconfigure(0, weight=1)  # Allow the Text widget to expand vertically

        # Create a vertical scrollbar linked to the Text widget
        text_scroll = ttk.Scrollbar(self, orient='vertical', command=self.text.yview)

        # Grid the Text widget and scrollbar, configuring them for resizing
        self.text.grid(column=0, row=0, sticky='NEWS', padx=3, pady=2)  # Text widget fills the available space
        text_scroll.grid(row=0, column=1, sticky='NS', padx=(0, 3), pady=2)  # Scrollbar placed on the right

        # Link the scrollbar to the Text widget, allowing scroll functionality
        self.text['yscrollcommand'] = text_scroll.set
