import tkinter as tk

from include.presenter import Presenter
from ui.pathselector import PathSelector
from ui.notebook import HorizTabCollection
from ui.filebar import FileBar
from ui.customtext import VerticalScrollText
from ui.auxbar import AuxBar

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


class UI(tk.Tk):
    '''Main UI of the application and view element of the MVP framework.'''

    def __init__(self) -> None:
        '''Initialize the graphical interface.'''
        
        super().__init__()
        self.title("Midnight Science GUI")

        # get screen width and height
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen
        w = 0.8*ws
        h = 0.8*hs
        # calculate x and y coordinates for the Tk root window
        x = (ws*0.1)
        y = (hs*0.1)

        # set the dimensions of the screen 
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))


    def initUI(self,presenter:Presenter)->None:
        '''Set up the element in the graphical interface.'''

        self.columnconfigure(0, weight=1)
        self.rowconfigure(3,weight=1)
        self.rowconfigure(4,weight=0)
        
        self.fileBar = FileBar(self)
        self.fileBar.grid(row=0,column=0,sticky = 'W')

        self.auxBar = AuxBar(self,presenter)
        self.auxBar.grid(row = 1,column=0,sticky='W')

        self.pathSelector = PathSelector(self,presenter)
        self.pathSelector.grid(row=2,column=0,sticky='EW')

        self.mainTabColl = HorizTabCollection(self,presenter)
        self.mainTabColl.grid(row=3,column=0,sticky='NEWS')

        self.text = VerticalScrollText(self,height = 150)
        self.text.grid(row=4,column=0,sticky='EW')

