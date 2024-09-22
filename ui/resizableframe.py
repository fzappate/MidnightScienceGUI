import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod

class ResizableFrame(tk.Frame, ABC):    
    def __init__(self, *args, **kwargs):
        """
        Initialize an instance of the virtual class of ResizableFrame. 
        This is the parent of ResizableFrameRightEdge, ResizableFrameLeftEdge, ResizableFrameTopEdge, ResizableFrameBottomEdge.
        
        Valid arguments: background, bd, bg, borderwidth, class, colormap, container, cursor, height, highlightbackground, 
        highlightcolor, highlightthickness, relief, takefocus, visual, width.

        
        -----USAGE-----
        This class should not be used. One of its children should be used instead. 
        """                
        super().__init__(*args, **kwargs)
        self.pack_propagate(0)
        self.grid_propagate(0)
        
        # By default, resizable frames should have only one children frame that expands in all directions
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        # Resize mode
        self.NONE = 0
        self.HORIZONTAL = 1
        self.VERTICAL = 2

        self.resizeMode = self.NONE
        
        self.bind("<ButtonPress-1>", self.StartResize)
        self.bind("<ButtonRelease-1>", self.StopResize)
        self.bind("<Motion>", self.MonitorCursorPosition)

        self.cursor = ''
        self.dragBandWidth = 5

    @abstractmethod
    def StartResize(self, event):
        """Set the resize mode if the left button of the mouse is clicked close to the edge that must be resized."""
        pass

    @abstractmethod
    def MonitorCursorPosition(self,event):        
        pass    

    def StopResize(self, event):
        """Disable any resize mode and set the standard arrow as cursor."""
        self.resizeMode = self.NONE
        self.config(cursor='')



class ResizableFrameRightEdge(ResizableFrame):
    def __init__(self, *args, **kwargs):
        """
        Initialize an instance of the class of ResizableFrameRightEdge. 
        This is a frame that can be resized when dragging its right edge.
        
        args: 
        - all the Frame arguments
            - background, bg: set background color
            - borderwidth, bd: set border width
            - ...
        
        -----USAGE-----
            
        root.columnconfigure(0,weight = 0)

        resFrame = ResizableFrameRightEdge(root, background = "blue",width = 100, height = 100)
        
        resFrame.grid(row = 0, column=0,sticky = 'NWS')
        """        
        super().__init__(*args, **kwargs)

    def StartResize(self, event):
        # Extract the size of the frame
        width = self.winfo_width()

        # If the mouse left button is clicked close to the right edge allow horizontal resizing
        if  event.x > width-self.dragBandWidth : 
            self.resizeMode = self.HORIZONTAL     
        else:
            self.resizeMode = self.NONE

    def MonitorCursorPosition(self,event):        
        """Check whether the cursor is close to the right edge of the frame."""
        # Extract the size of the frame
        width = self.winfo_width()
        height = self.winfo_height()

        # If the cursor is close to the right edge change cursor icon
        if  event.x > width-self.dragBandWidth : 
            self.config(cursor='sb_h_double_arrow')
        else:
            self.config(cursor='')
        
        # If horizontal resizing is allowed then resize frame with cursor
        if self.resizeMode == self.HORIZONTAL:
            self.config(width = event.x)



class ResizeScrollVFrameRightEdge(ResizableFrameRightEdge):
    def __init__(self, parent, *args, **kw):
        """
        Initialize an instance of the class of ResizeScrollVFrameRightEdge. 
        This is a frame that can be scrolled and resized when dragging its right edge.
        
        args: 
        - all the Frame arguments
            - background, bg: set background color
            - borderwidth, bd: set border width
            - ...
        
        -----USAGE-----
            
        root.columnconfigure(0,weight = 0)

        resScrollFrame = ResizeScrollVFrameRightEdge(root)
        
        resScrollFrame.grid(row = 0, column=0,sticky = 'NWS')
        
        frame = th.Frame(resSizeScroll, bg = blue)
        
        frame.grid(row = 0, column = 0, sticky = 'NEWS')
        """  

        super().__init__(parent, *args, **kw)
        # Insipired by:
        # https://stackoverflow.com/questions/16188420/tkinter-scrollbar-for-frame
        
        # Create a canvas object and a vertical scrollbar for scrolling it
        self.vscrollbar = ttk.Scrollbar(self, orient='vertical')
        self.vscrollbar.pack(fill='y', side='right', expand=False,padx = (0,self.dragBandWidth),pady = (3,3))
        
        self.canvas = tk.Canvas(self,highlightthickness=0, yscrollcommand=self.vscrollbar.set)
        self.canvas.grid(row=0,column=0,sticky='NEW',padx = (3,3),pady = (3,3))
        self.canvas.pack(side='left', fill='both', expand=True,padx = (0,self.dragBandWidth),pady = (3,3))
        
        # There is no need to bond the scrollbar to the canvas because boundToMouseWheel is used
        # self.vscrollbar.config(command=self.canvas.yview)
        
        # Reset the canvas view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it
        self.interior = tk.Frame(self.canvas, bg = 'red')
        self.interior.columnconfigure(0,weight=1)
        self.interior.rowconfigure(0,weight=1)
        self.interior_id = self.canvas.create_window(0, 0, window=self.interior, anchor='nw')

        # Bind the frame to the scrollbar so that it can be scrolled while paning over it
        self.bind('<Enter>', self.boundToMouseWheel)
        self.bind('<Leave>', self.unboundToMouseWheel)
        
        # Bind canvas to frame and viceversa
        self.interior.bind('<Configure>', self._configure_interior)
        self.canvas.bind('<Configure>', self._configure_canvas)
        
    def _configure_interior(self,event):
        # Update the scrollbars to match the size of the inner frame.
        size = (self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
        self.canvas.config(scrollregion="0 0 %s %s" % size)
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # Update the canvas's width to fit the inner frame.
            self.canvas.config(width=self.interior.winfo_reqwidth())
        
    def _configure_canvas(self,event):
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # Update the inner frame's width to fill the canvas.
            self.canvas.itemconfigure(self.interior_id, width=self.canvas.winfo_width())
        
    def boundToMouseWheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def unboundToMouseWheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        # If frame is greater than canvas scroll, otherwise not.
        interiorLength = self.interior.winfo_height()
        canvasLength = self.canvas.winfo_height()
        if (interiorLength > canvasLength):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")



class ResizableFrameLeftEdge(ResizableFrame):
    def __init__(self, *args, **kwargs):
        """
        Initialize an instance of the class of ResizableFrameRightEdge. 
        This is a frame that can be resized when dragging its right edge.
        
        args: 
        - all the Frame arguments
            - background, bg: set background color
            - borderwidth, bd: set border width
            - ...
        
        -----USAGE-----
            
        root.columnconfigure(0,weight = 0)

        resFrame = ResizableFrameRightEdge(root, background = "blue",width = 100, height = 100)
        
        resFrame.grid(row = 0, column=0,sticky = 'NWS')
        """ 
        super().__init__(*args, **kwargs)

    def StartResize(self, event):
        # Extract the size of the frame
        width = self.winfo_width()

        # If the mouse left button is clicked close to the right edge allow horizontal resizing
        if  event.x < self.dragBandWidth : 
            self.resizeMode = self.HORIZONTAL    
        else:
            self.resizeMode = self.NONE


    def MonitorCursorPosition(self,event):        
        '''Check whether the cursor is close to the left edge of the frame.'''
        # Extract the size of the frame
        width = self.winfo_width()
        height = self.winfo_height()

        # If the cursor is close to the right edge change cursor icon
        if  event.x < self.dragBandWidth : 
            self.config(cursor='sb_h_double_arrow')
        else:
            self.config(cursor='')

        # If horizontal resizing is allowed then resize frame with cursor
        if self.resizeMode == self.HORIZONTAL:
            self.config(width = width - event.x)
    


class ResizableFrameTopEdge(ResizableFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        '''
        Initialize a resizable frame that can be resized dragging the top edge.
        
        Valid resource names: background, bd, bg, borderwidth, class, colormap, container, cursor, height, highlightbackground, 
        highlightcolor, highlightthickness, relief, takefocus, visual, width.

        
        -----USAGE-----
            
        root.columnconfigure(0,weight = 0)

        resFrame = ResizableFrame(root, background = "blue",width = 100, height = 100)
        
        resFrame.grid(row = 0, column=0,sticky = 'NES')
        '''


    def StartResize(self, event):
        '''Set the resize mode if the left button of the mouse is clicked close to the edge that must be resized.'''
        # Extract the size of the frame
        width = self.winfo_width()

        # If the mouse left button is clicked close to the right edge allow horizontal resizing
        if  event.y < self.dragBandWidth : 
            self.resizeMode = self.VERTICAL        
        else:
            self.resizeMode = self.NONE


    def MonitorCursorPosition(self,event):        
        '''Check whether the cursor is close to the left edge of the frame.'''
        # Extract the size of the frame
        width = self.winfo_width()
        height = self.winfo_height() 

        # If the cursor is close to the right edge change cursor icon
        if  event.y < self.dragBandWidth : 
            self.config(cursor='sb_v_double_arrow')
        else:
            self.config(cursor='')

        # If horizontal resizing is allowed then resize frame with cursor
        if self.resizeMode == self.VERTICAL:
            self.config(height = height - event.y)