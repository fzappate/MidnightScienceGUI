import tkinter as tk
from abc import ABC, abstractmethod

class ResizableFrame(tk.Frame, ABC):    
    def __init__(self, *args, **kwargs):
        '''
        This is a virtual class of ResizableFrame. 
        This is the parent of ResizableFrameRightEdge, ResizableFrameLeftEdge, ResizableFrameTopEdge, ResizableFrameBottomEdge.
        
        Valid resource names: background, bd, bg, borderwidth, class, colormap, container, cursor, height, highlightbackground, 
        highlightcolor, highlightthickness, relief, takefocus, visual, width.

        
        -----USAGE-----
        This class should not be used. One of its children should be used instead. 
        '''
        super().__init__(*args, **kwargs)
        self.pack_propagate(0)
        self.grid_propagate(0)

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
        pass

    @abstractmethod
    def MonitorCursorPosition(self,event):        
        pass
    

    def StopResize(self, event):
        '''Disable any resize mode and set the standard arrow as cursor.'''
        self.resizeMode = self.NONE
        self.config(cursor='')



class ResizableFrameRightEdge(ResizableFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        '''
        Initialize a resizable frame that can be resized dragging the right edge.
        
        Valid resource names: background, bd, bg, borderwidth, class, colormap, container, cursor, height, highlightbackground, 
        highlightcolor, highlightthickness, relief, takefocus, visual, width.

        
        -----USAGE-----
            
        root.columnconfigure(0,weight = 0)

        resFrame = ResizableFrame(root, background = "blue",width = 100, height = 100)
        
        resFrame.grid(row = 0, column=0,sticky = 'NWS')
        '''


    def StartResize(self, event):
        '''Set the resize mode if the left button of the mouse is clicked close to the edge that must be resized.'''
        # Extract the size of the frame
        width = self.winfo_width()

        # If the mouse left button is clicked close to the right edge allow horizontal resizing
        if  event.x > width-self.dragBandWidth : 
            self.resizeMode = self.HORIZONTAL        
        else:
            self.resizeMode = self.NONE
            

    def MonitorCursorPosition(self,event):        
        '''Check whether the cursor is close to the right edge of the frame.'''
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



class ResizableFrameLeftEdge(ResizableFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        '''
        Initialize a resizable frame that can be resized dragging the left edge.
        
        Valid resource names: background, bd, bg, borderwidth, class, colormap, container, cursor, height, highlightbackground, 
        highlightcolor, highlightthickness, relief, takefocus, visual, width.

        
        -----USAGE-----
            
        root.columnconfigure(0,weight = 0)

        resFrame = ResizableFrame(root, background = "blue",width = 100, height = 100)
        
        resFrame.grid(row = 0, column=0,sticky = 'NES')
        '''

            # Resize mode


    def StartResize(self, event):
        '''Set the resize mode if the left button of the mouse is clicked close to the edge that must be resized.'''
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