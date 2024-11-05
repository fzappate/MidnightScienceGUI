import tkinter as tk
from tkinter import ttk 
from ui.ResizableFrame import ResizableFrameTopEdge
     
class VerticalScrollText(ResizableFrameTopEdge):
    '''Text object with vertical scroll.'''

    def __init__(self,parent,*args,**kwargs):
        super().__init__(parent,*args, **kwargs)
        '''Initialize the text object with vertical scroll.'''

        # Set the grid configuration of this object
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        
        
        self.text = tk.Text(self)
        self.text.grid_rowconfigure(0, weight=1)
        # self.text.insert('1.0','Please eneter a comment')

        # Scroll bar 
        text_scroll = ttk.Scrollbar(self, orient='vertical',command = self.text.yview)
        
        self.text.grid(column =0, row=0,sticky='NEWS',padx=3,pady=2)
        text_scroll.grid(row=0,column=1,sticky='NS',padx=(0,3),pady=2)

        # Link the text to the scroll bar
        self.text['yscrollcommand'] = text_scroll.set