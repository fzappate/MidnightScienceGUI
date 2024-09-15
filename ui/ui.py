import tkinter as tk

from presenter.presenter import Presenter
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
        self.config(bg='black')
        
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
        
        self.fileBar = FileBar(self,presenter, background = 'gray30')
        self.fileBar.grid(row=0,column=0,sticky = 'EW', padx = (3,3),pady = (2,2))

        self.auxBar = AuxBar(self,presenter, background = 'gray30')
        self.auxBar.grid(row = 1,column=0,sticky='EW', padx = (3,3),pady = (2,2))

        self.pathSelector = PathSelector(self,presenter, background = 'gray30')
        self.pathSelector.grid(row=2,column=0,sticky='EW', padx = (3,3),pady = (2,2))

        self.mainTabColl = HorizTabCollection(self,presenter, background = 'gray30')
        self.mainTabColl.grid(row=3,column=0,sticky='NEWS', padx = (3,3),pady = (2,2))

        self.text = VerticalScrollText(self,height = 150, background = 'gray30')
        self.text.grid(row=4,column=0,sticky='EW', padx = (3,3),pady = (2,2))

