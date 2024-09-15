import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog
from numpy import pi
from ui.resizableframe import ResizableFrameLeftEdge 

try: 
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


class RotationAngle():
    '''Class of objects containing how much the gear set is rotated in the plot.'''

    def __init__(self,angle)->None:
        '''Initialize rotation angle object.'''

        self.angDeg = float(angle)
        self.angRad = self.angDeg*pi/180


    def update(self,newAng)->None:
        '''Update the rotation angle value.'''

        self.angDeg = float(newAng)
        self.angRad = self.angDeg*pi/180


class GeomPreprocPlotControlsUI(ResizableFrameLeftEdge):
    '''Class of widgets that allow the user to modify the gear generator plot.'''

    def __init__(self,parent,presenter, *args, **kwargs)->None:
        super().__init__(parent,*args, **kwargs)
        '''Initialize the gear generator plot control object.'''

        # Set the existing column to take all the space available
        self.columnconfigure(0,weight=0)
        # Make sure that the content of GeomPreprocPlotControlsUI stretches from top to bottom
        self.rowconfigure(0, weight=1)            

        # Create a frame container that can be padded to leave some ResizableFrame exposed to the cursor
        self.controlContainer = ttk.Frame(self)
        self.controlContainer.grid(row=0,column=1,sticky='NSW',padx = (5,0))
        rowNo = 0   

        # Rotation Control 
        self.rotationGearSet = RotationControl(self.controlContainer,presenter)
        self.rotationGearSet.grid(row=0,column=1,sticky="EW")
    
        rowNo = rowNo+1

        # Grid check
        self.gridControl = GridCheckButton(self.controlContainer,presenter)
        self.gridControl.grid(row=1,column=1,sticky="EW")
        
        rowNo = rowNo+1


class FileSearch():
    def __init__(self,parent,targetPlot):
        self.parent = parent 
        self.targetPlot = targetPlot

        self.filePath = tk.StringVar()
        btnWidth = 3

        self.searchLab = ttk.Label(self.parent, text = 'Add Profile')
        self.searchLab.grid(row = 0,column=0,sticky = "EW")

        self.entryPath = ttk.Entry(self.parent)
        self.entryPath.grid(row = 1, column= 0,sticky = "EW")

        self.searchButton = ttk.Button(self.parent, text = '?', width = btnWidth, command= lambda:self.browse())
        self.searchButton.grid(row = 1, column= 1,)

    # Methods =============================================

    def browse(self):
        # Allow user to select a directory and store it in global var
        # called folder_path
        filename = filedialog.askopenfilename(initialdir = "./",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
        self.filePath.set(filename)
        self.updateEntry(filename)
        return

    def updateEntry(self,txt):
        self.entryPath.delete(0,tk.END)
        self.entryPath.insert(0,txt)


class GridCheckButton(ttk.Frame):
    '''Class of widgets that allow the user to add or remove the grid in the gear generator plot.'''

    def __init__(self,parent,presenter)->None:
        super().__init__(parent)
        '''Initialize the object that allows to add or remove the grid in the gear generator object.'''

        self.columnconfigure(0,weight=1)
        
        charPerLabel = 20

        # Label
        self.lab = ttk.Label(self, text = "Plot Grid", width = charPerLabel)
        self.lab.grid(row=0,column=0,sticky='W')

        # Chekcbutton
        self.checkbox = ttk.Checkbutton(self,command = lambda: presenter.ChangeGridState())
        self.checkbox.state(['!alternate'])
        self.checkbox.grid(row=0,column=1,sticky='E')            


class RotationControl(ttk.Frame):
    '''Class of widgets that allow the user to control the rotation of the gear set in the gear generator plot.'''

    def __init__(self,parent,presenter)->None:
        super().__init__(parent)
        '''Initialize the widget that allows the rotation of the gear set in the gear generator plot.'''

        self.rotValue = RotationAngle(0)

        charPerLabel = 20
        entryWidth = 5
        btnWidth = 3

        # Lable
        self.lab = ttk.Label(self, text = "Angle", width = charPerLabel)
        self.lab.grid(row=0,column=0)

        # Entry
        self.entry = ttk.Entry(self,width = entryWidth)
        self.entry.insert(0,self.rotValue.angDeg)
        self.entry.grid(row=0,column=1)
        self.entry.bind('<Return>', lambda event: presenter.RotateGearSet())
        self.entry.bind('<FocusOut>', lambda event: presenter.RotateGearSet())

        # Rotate CCW
        self.buttLeft = ttk.Button(self,text = "<",width=btnWidth,command= lambda: presenter.RotateGearSet(-1))
        self.buttLeft.grid(row=0,column=2)

        # Rotate CW
        self.buttRight = ttk.Button(self,text = ">",width=btnWidth,command= lambda: presenter.RotateGearSet(1))
        self.buttRight.grid(row=0,column=3)
