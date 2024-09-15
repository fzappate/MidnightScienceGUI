from tkinter import ttk
import tkinter as tk
import os 
from PIL import Image,ImageTk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass 


class CollapsiblePane(ttk.Frame):
    """
     -----USAGE-----
    collapsiblePane = CollapsiblePane(parent,
                          expanded_text =[string],
                          collapsed_text =[string])
 
    collapsiblePane.pack()
    button = Button(collapsiblePane.frame).pack()
    """
 
    def __init__(self, parent, expanded_text ="-",
                               collapsed_text ="+",label = ""):
 
        ttk.Frame.__init__(self, parent)
 
        # These are the class variable
        # see a underscore in expanded_text and _collapsed_text
        # this means these are private to class
        self.isCollapsed = True
        self.parent = parent
        self._expanded_text = expanded_text
        self._collapsed_text = collapsed_text
 
        # Here weight implies that it can grow it's size if extra space is available
        # default weight is 0
        self.columnconfigure(1, weight = 1)
 
        # Tkinter variable storing integer value
        self._variable = tk.IntVar()
 
        # Checkbutton is created but will behave as Button
        # cause in style, Button is passed
        # main reason to do this is Button do not support
        # variable option but checkbutton do
        iconSize = (20, 20)

        expandIconPath = os.path.join(os.getcwd(),'MainMVP\images\expandIcon.png')
        self.expandIcon = Image.open(expandIconPath)
        self.expandIcon = self.expandIcon.resize(iconSize)
        self.expandIcon = ImageTk.PhotoImage(self.expandIcon)


        collapseIconPath = os.path.join(os.getcwd(),'MainMVP\images\collapseIcon.png')
        self.collapseIcon = Image.open(collapseIconPath)
        self.collapseIcon = self.collapseIcon.resize(iconSize)
        self.collapseIcon = ImageTk.PhotoImage(self.collapseIcon)

        # Create a frame to put a button and a label and manage their allaignment separately 
        self.labelFrame = ttk.Frame(self)

        self._button = ttk.Button( self.labelFrame, command = self._activate, image = self.expandIcon, width=3)
        self._button.grid(row = 0, column = 0,sticky='W')
 
        self.label = ttk.Label(self.labelFrame,text = label)
        self.label.grid(row = 0, column=1,sticky='W')

        self.labelFrame.grid(row=0,column=0,sticky = 'EW')

        # This will create a separator
        # A separator is a line, we can also set thickness
        self._separator = ttk.Separator(self, orient ="horizontal")
        self._separator.grid(row = 0, column = 2, sticky ="we")
 
        self.frame = ttk.Frame(self)
        self.frame.columnconfigure(0,weight=1)
 
        # This will call activate function of class
        self._activate()
 
    def _activate(self):
        if (self.isCollapsed==True):
            # As soon as button is pressed it removes this widget
            # but is not destroyed means can be displayed again
            self.frame.grid_forget()
 
            # This will change the text of the checkbutton
            self._button.configure(image = self.expandIcon)

            # # Change the property isCollpased to False
            self.isCollapsed = False
 
        elif (self.isCollapsed==False):
            # increasing the frame area so new widgets
            # could reside in this container
            self.frame.grid(row = 1, column = 0, columnspan = 2,sticky='EW')
            self._button.configure(image = self.collapseIcon)

            # # Change the property isCollpased to False
            self.isCollapsed = True