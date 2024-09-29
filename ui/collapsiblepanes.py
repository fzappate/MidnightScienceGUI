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
        
        # Create the header frame
        self.headerFrame = tk.Frame(self)
        self.headerFrame.grid(row=0,column=0,sticky = 'EW')
        
        # Create expand button
        self.expandButton = ttk.Button( self.headerFrame, command = self._activate, width=3)
        
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
        self.label = tk.Label(self.headerFrame,text = label)
        self.label.grid(row = 0, column=1,sticky='W')
        
        # Create expandable frame
        self.interior = tk.Frame(self)
        self.interior.columnconfigure(0,weight=1)
        
        # Tkinter variable storing integer value
        self._variable = tk.IntVar()        

        # This will create a separator
        # A separator is a line, we can also set thickness
        self._separator = ttk.Separator(self, orient ="horizontal")
        self._separator.grid(row = 2, column = 0, sticky ="we")
  
        # This will call activate function of class
        self._activate()
 
    def _activate(self):
        if (self.isCollapsed==True):
            # As soon as button is pressed it removes this widget
            # but is not destroyed means can be displayed again
            self.interior.grid_forget()
 
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
            self.interior.grid(row = 1, column = 0,sticky='EW')
            
            if self.iconMode == 'img':
                self.expandButton.configure(image = self.collapseIcon)
            elif self.iconMode == 'text':
                self.expandButton.configure(text = self.collapseText)

            # # Change the property isCollpased to False
            self.isCollapsed = True
            

class TogglePaneDel(tk.Frame):
    def __init__(self, 
                 parent, 
                 presenter,
                 togglePaneNo = 0,
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
        self.parent = parent
        self.presenter = presenter
        self.togglePaneNo = togglePaneNo
        self.iconMode = iconMode
        self.expImgPath = expImgPath
        self.collImgPath = collImgPath
        self.isCollapsed = True
        self.expandText = expandText
        self.collapseText = collapseText
 
        # Set the weight so that the header label takes up the excess of space
        self.columnconfigure(0, weight = 1)
        
        # Create the header frame
        self.headerFrame = tk.Frame(self)
        self.headerFrame.columnconfigure(1,weight=1)
        self.headerFrame.grid(row=0,column=0,sticky = 'EW')
                
        # Create expand button
        self.expandButton = ttk.Button( self.headerFrame, command = self._activate, width=3)
        
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
        self.label = tk.Label(self.headerFrame,text = label)
        self.label.grid(row = 0, column=1,sticky='W')
        
        # Create header delete button
        self.delIcon = '\u2B59' # ⭙ 
        self.delBtn = ttk.Button( self.headerFrame, text = self.delIcon, command=lambda:self.presenter.DeleteSubplot(self),width=3)
        self.delBtn.grid(row = 0, column=2,sticky='E')
        
        # Create expandable frame
        self.interior = tk.Frame(self)
        self.interior.columnconfigure(0,weight=1)
        
        # Tkinter variable storing integer value
        self._variable = tk.IntVar()        

        # This will create a separator
        # A separator is a line, we can also set thickness
        self._separator = ttk.Separator(self, orient ="horizontal")
        self._separator.grid(row = 2, column = 0, sticky ="we")
  
        # This will call activate function of class
        self._activate()
 
    def _activate(self):
        if (self.isCollapsed==True):
            # As soon as button is pressed it removes this widget
            # but is not destroyed means can be displayed again
            self.interior.grid_forget()
 
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
            self.interior.grid(row = 1, column = 0,sticky='EW')
            
            if self.iconMode == 'img':
                self.expandButton.configure(image = self.collapseIcon)
            elif self.iconMode == 'text':
                self.expandButton.configure(text = self.collapseText)

            # # Change the property isCollpased to False
            self.isCollapsed = True
            

  