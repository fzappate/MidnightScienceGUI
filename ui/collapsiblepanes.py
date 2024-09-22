from tkinter import ttk
import tkinter as tk
import os 
from PIL import Image,ImageTk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass 


class TogglePane(tk.Frame):
    def __init__(self, 
                 parent, 
                 iconMode = "text",
                 expandText ="+",
                 collapseText ="-",
                 label = "",
                 iconSize = 20,
                 expImgPath = "",
                 collImgPath = "",
                 *args,**kwargs):
        """
        Initialize an instance of the class of TogglePane. 
        This is a widget with a header and a toggle button that can exapand or 
        collapse the frame below it. Collapsible widget must be insert in the child frame 
        interior
        
        args: 
        - label: label displayed in the header
        - iconMode: "text" or "img". "text" is default
        - expandText: "text" option. Text displayed in the toggle button when widget is expanded
        - collapseText: "text" option. Text displayed in the toggle button when widget is collapsed
        - expImgPath: "img" option. Text displayed in the toggle button when widget is expanded
        - collImgPath: "img" option. Text displayed in the toggle button when widget is collapsed
        - iconSize: size of the toggle icon in pixels
        - all the Frame arguments
            - background, bg: set background color
            - borderwidth, bd: set border width
            - ...
        
        -----USAGE-----
        
        parentFrame = Frame(root)
        
        collapsiblePane = CollapsiblePane(parentFrame,label = 'Collapsible Widget')
        collapsiblePane.grid(row = 0, column = 0, sticky = 'NEWS')
        
        userWidget = Frame(collapsiblePane.interior)
        userWidget.grid(row = 0,column = 0, sticky = 'NEWS')
        """
        super().__init__(parent,*args,**kwargs)
 
        # Properties
        self.iconMode = iconMode
        self.expImgPath = expImgPath
        self.collImgPath = collImgPath
        self.isCollapsed = True
        self.parent = parent
        self.expandText = expandText
        self.collapseText = collapseText
 
        # Set the weight so that the header label takes up the excess of space
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        
        # Create the header frame
        self.labelFrame = tk.Frame(self)
        
        # Create expand button
        self.expandButton = ttk.Button( self.labelFrame, command = self._activate, width=3)
        
        # Set the icon/text of the expand button
        if iconMode == 'img':
            iconSizeTup = (iconSize, iconSize)
            expandIconPath = os.path.join(os.getcwd(),self.expImgPath)
            self.expandIcon = Image.open(expandIconPath)
            self.expandIcon = self.expandIcon.resize(iconSizeTup)
            self.expandIcon = ImageTk.PhotoImage(self.expandIcon)

            collapseIconPath = os.path.join(os.getcwd(),self.collImgPath)
            self.collapseIcon = Image.open(collapseIconPath)
            self.collapseIcon = self.collapseIcon.resize(iconSizeTup)
            self.collapseIcon = ImageTk.PhotoImage(self.collapseIcon)
            
            self.expandButton.config(image=self.expandIcon)
            
        elif iconMode == 'text':
            self.expandButton.config(text=self.collapseText)
            
        self.expandButton.grid(row = 0, column = 0,sticky='W')
 
        # Create header label
        self.label = tk.Label(self.labelFrame,text = label)
        self.label.grid(row = 0, column=1,sticky='W')
        
        # Create expandable frame
        self.expandFrame = tk.Frame(self)
        self.expandFrame.columnconfigure(0,weight=1)
        
        # Tkinter variable storing integer value
        self._variable = tk.IntVar()
        
        self.labelFrame.grid(row=0,column=0,sticky = 'EW')
            

 
        


        # This will create a separator
        # A separator is a line, we can also set thickness
        # self._separator = ttk.Separator(self, orient ="horizontal")
        # self._separator.grid(row = 0, column = 2, sticky ="we")
 
 
        # This will call activate function of class
        self._activate()
 
    def _activate(self):
        if (self.isCollapsed==True):
            # As soon as button is pressed it removes this widget
            # but is not destroyed means can be displayed again
            self.expandFrame.grid_forget()
 
            # This will change the text of the checkbutton
            if self.iconMode == 'img':
                self.expandButton.configure(image = self.expandIcon)
            elif self.iconMode == 'text':
                self.expandButton.configure(text = self.expandText)

            # # Change the property isCollpased to False
            self.isCollapsed = False
 
        elif (self.isCollapsed==False):
            # increasing the frame area so new widgets
            # could reside in this container
            self.expandFrame.grid(row = 1, column = 0, columnspan = 2,sticky='EW')
            
            if self.iconMode == 'img':
                self.expandButton.configure(image = self.collapseIcon)
            elif self.iconMode == 'text':
                self.expandButton.configure(text = self.collapseText)

            # # Change the property isCollpased to False
            self.isCollapsed = True
            

            
class TogglePaneDel(tk.Frame):
    """
     -----USAGE-----
    collapsiblePane = CollapsiblePane(parent,
                          expandText =[string],
                          collapsed_text =[string])
 
    collapsiblePane.pack()
    button = Button(collapsiblePane.frame).pack()
    """
 
    def __init__(self, parent, expandText ="-",
                               collapsed_text ="+",label = ""):
 
        ttk.Frame.__init__(self, parent)
 
        # These are the class variable
        # see a underscore in expandText and _collapsed_text
        # this means these are private to class
        self.isCollapsed = True
        self.parent = parent
        self.collapsedText = '\u21E9' # ⇩
        self.expandedText = '\u21E7' # ⇧
 
        # Here weight implies that it can grow it's size if extra space is available
        # default weight is 0
        self.columnconfigure(0, weight = 1)
 
        # Tkinter variable storing integer value
        self._variable = tk.IntVar()

        # Create a frame to put a button and a label and manage their allaignment separately 
        self.labelFrame = ttk.Frame(self)
        self.labelFrame.columnconfigure(0, weight = 0)
        self.labelFrame.columnconfigure(1, weight = 1)
        self.labelFrame.columnconfigure(2, weight = 0)

        self.toggleButton = ttk.Button( self.labelFrame, command = self._activate,text = self.collapsedText, width=3)
        self.toggleButton.grid(row = 0, column = 0,sticky='W')
        
        self.label = ttk.Label(self.labelFrame,text = label)
        self.label.grid(row = 0, column=1,sticky='EW')

        self.delButton = ttk.Button( self.labelFrame,text = 'x', width=3)
        self.delButton.grid(row = 0, column =2,sticky='E')
        
        self.labelFrame.grid(row=0,column=0,sticky = 'EW')

        # This will create a separator
        # A separator is a line, we can also set thickness
        # self._separator = ttk.Separator(self, orient ="horizontal")
        # self._separator.grid(row = 0, column = 1, sticky ="WE")
 
        self.subplotManagerPane = ttk.Frame(self)
        self.subplotManagerPane.columnconfigure(0,weight=1)
 
        # This will call activate function of class
        self._activate()
 
    def _activate(self):
        if (self.isCollapsed==True):
            # As soon as button is pressed it removes this widget
            # but is not destroyed means can be displayed again
            self.subplotManagerPane.grid_forget()
 
            # This will change the text of the checkbutton
            self.toggleButton.configure(text = self.collapsedText)

            # # Change the property isCollpased to False
            self.isCollapsed = False
 
        elif (self.isCollapsed==False):
            # increasing the frame area so new widgets
            # could reside in this container
            self.subplotManagerPane.grid(row = 1, column = 0, columnspan = 2,sticky='EW')
            self.toggleButton.configure(text = self.expandedText)

            # # Change the property isCollpased to False
            self.isCollapsed = True
