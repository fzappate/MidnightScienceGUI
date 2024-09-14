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
 
        # Here weight implies that it can grow it's
        # size if extra space is available
        # default weight is 0
        self.columnconfigure(1, weight = 1)
 
        # Tkinter variable storing integer value
        self._variable = tk.IntVar()
 
        # Checkbutton is created but will behave as Button
        # cause in style, Button is passed
        # main reason to do this is Button do not support
        # variable option but checkbutton do
        # self._button = ttk.Checkbutton(self, variable = self._variable,
        #                     command = self._activate,style ="TButton",width=3)
        iconSize = (30, 30)

        expandIconPath = os.path.join(os.getcwd(),'MainMVP\images\expandIcon.png')
        self.expandIcon = Image.open(expandIconPath)
        self.expandIcon = self.expandIcon.resize(iconSize)
        self.expandIcon = ImageTk.PhotoImage(self.expandIcon)


        collapseIconPath = os.path.join(os.getcwd(),'MainMVP\images\collapseIcon.png')
        self.collapseIcon = Image.open(collapseIconPath)
        self.collapseIcon = self.collapseIcon.resize(iconSize)
        self.collapseIcon = ImageTk.PhotoImage(self.collapseIcon)

        self._button = ttk.Button(  self,
                                    # variable = self._variable, 
                                    command = self._activate,
                                    # text = collapsed_text,
                                    image = self.expandIcon,
                                    width=3)
        
        self._button.grid(row = 0, column = 0)
 
        self.label = ttk.Label(self,text = label)
        self.label.grid(row = 0, column=1,sticky='W')
        # This will create a separator
        # A separator is a line, we can also set thickness
        self._separator = ttk.Separator(self, orient ="horizontal")
        self._separator.grid(row = 0, column = 2, sticky ="we")
 
        self.frame = ttk.Frame(self)
 
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
            self.frame.grid(row = 1, column = 0, columnspan = 2)
            self._button.configure(image = self.collapseIcon)

            # # Change the property isCollpased to False
            self.isCollapsed = True
 

# Root 
root = tk.Tk()
root.title("Command Widget") 
# root.geometry('600x400')
root.rowconfigure(0,weight=1)


frame2 = CollapsiblePane(root,'-','+','Test Label')
frame2.grid(row=0,column=0,sticky="NS")

bu1 = tk.Button(frame2.frame,text = 'ciao')
bu1.grid(row=0,column=0)

bu2 = tk.Button(frame2.frame,text = 'ciao2')
bu2.grid(row=1,column=0)

ent = tk.Entry(frame2.frame,width=20)
ent.grid(row=2,column=0)

root.mainloop()