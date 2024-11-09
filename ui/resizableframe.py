"""
ResizableFrame Module
======================

This module provides a set of classes that implement resizable frames in a Tkinter
application. The frames can be resized by dragging their edges. This module defines 
the base class `ResizableFrame` and its children that allow resizing from different 
edges: left, right, and top. These classes are designed to be used as part of a 
customizable user interface where resizing behavior is required.

Author: Federico Zappaterra
Version: 1.0.0
Date: 2024-11-06

Classes
-------
ResizableFrame(ABC, tk.Frame)
    A base class that defines the core functionality for creating resizable frames.
    
ResizableFrameLeftEdge(ResizableFrame)
    A frame that can be resized by dragging its left edge.

ResizableFrameRightEdge(ResizableFrame)
    A frame that can be resized by dragging its right edge.
    
ResizableFrameTopEdge(ResizableFrame)
    A frame that can be resized by dragging its top edge.

ResizableFrameRightEdgeScrollV(ResizableFrameRightEdge)
    A specialized resizable frame with vertical scrolling functionality.

Usage Example
-------------
To use a resizable frame, you can instantiate one of the derived classes and 
place it in a Tkinter layout. For example:

    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    resizable_frame = ResizableFrameRightEdge(root, background="blue", width=200, height=150)
    resizable_frame.grid(row=0, column=0, sticky="NEWS")

This will create a frame that can be resized by dragging its right edge. You can 
combine this with other Tkinter widgets like `Canvas` or `Scrollbar` for more complex 
layouts and behaviors.

"""


import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod

class ResizableFrame(tk.Frame, ABC):
    """
    A base class for creating resizable frames in a Tkinter application. This class 
    serves as a parent for specific resizable frame types, such as 
    ResizableFrameRightEdge, ResizableFrameLeftEdge, ResizableFrameTopEdge, and 
    ResizableFrameBottomEdge.
    
    This class defines the basic logic for resizing frames using mouse events, but 
    should not be used directly. Instead, one of its child classes should be used.

    Arguments:
        Valid arguments include all common Tkinter Frame options such as background, 
        bd, bg, borderwidth, class, colormap, container, cursor, height, highlightbackground, 
        highlightcolor, highlightthickness, relief, takefocus, visual, width.
        
    Example usage:
        # Do not instantiate this class directly
        resFrame = ResizableFrameRightEdge(parent_frame)
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the ResizableFrame base class. Sets up the resize behavior and 
        initializes the events for resizing operations.
        
        Arguments:
            *args, **kwargs: Arguments passed to the tkinter Frame constructor.
        """
        super().__init__(*args, **kwargs)
        
        # Prevent the frame from resizing its children automatically
        self.pack_propagate(0)
        self.grid_propagate(0)
        
        # Configure the default layout to allow resizing in all directions
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Constants for resize modes
        self.NONE = 0  # No resizing
        self.HORIZONTAL = 1  # Horizontal resizing
        self.VERTICAL = 2  # Vertical resizing

        # Initial resize mode (none)
        self.resizeMode = self.NONE
        
        # Mouse event bindings for resizing
        self.bind("<ButtonPress-1>", self.StartResize)
        self.bind("<ButtonRelease-1>", self.StopResize)
        self.bind("<Motion>", self.MonitorCursorPosition)

        # Resize parameters
        self.cursor = ''  # Current cursor icon
        self.dragBandWidth = 5  # Width of the draggable area to trigger resize

    @abstractmethod
    def StartResize(self, event):
        """
        Determines whether resizing should start based on mouse position near the frame edge.
        
        This method should be implemented in subclasses to handle specific edge-resizing logic.
        
        Args:
            event (tk.Event): The mouse event that triggers the resize action.
        """
        pass

    @abstractmethod
    def MonitorCursorPosition(self, event):
        """
        Monitors the cursor position to determine whether it is near the edge 
        of the frame for resizing and adjusts the cursor icon accordingly.
        
        This method should be implemented in subclasses to provide specific behavior 
        for resizing in a particular direction.

        Args:
            event (tk.Event): The mouse event for monitoring the cursor position.
        """
        pass    

    def StopResize(self, event):
        """
        Stops the resizing operation and restores the default cursor when the mouse button is released.
        
        Args:
            event (tk.Event): The mouse event for releasing the button and stopping the resize.
        """
        # Reset resize mode and cursor
        self.resizeMode = self.NONE
        self.config(cursor='')



class ResizableFrameRightEdge(ResizableFrame):
    """
    A frame that can be resized by dragging its right edge. Inherits from `ResizableFrame`.
    
    This class implements the logic for resizing a frame horizontally by dragging its right edge.
    
    Arguments:
        All arguments accepted by `tk.Frame` are valid, including background, bg, borderwidth, etc.
        
    Example usage:
        resFrame = ResizableFrameRightEdge(root, background="blue", width=100, height=100)
        resFrame.grid(row=0, column=0, sticky="NWS")
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initializes the ResizableFrameRightEdge class, setting up the right-edge resizing behavior.
        
        Arguments:
            *args, **kwargs: Arguments passed to the `ResizableFrame` constructor.
        """
        super().__init__(*args, **kwargs)

    def StartResize(self, event):
        """
        Determines if the mouse click is near the right edge of the frame to initiate horizontal resizing.
        
        Args:
            event (tk.Event): The mouse event that triggers the resizing.
        """
        # Get the current width of the frame
        width = self.winfo_width()

        # If the mouse is clicked close to the right edge, enable horizontal resizing
        if event.x > width - self.dragBandWidth:
            self.resizeMode = self.HORIZONTAL
        else:
            self.resizeMode = self.NONE

    def MonitorCursorPosition(self, event):
        """
        Monitors the cursor position and changes the cursor icon if it's close to the right edge of the frame.
        
        Also resizes the frame horizontally if resizing is allowed.
        
        Args:
            event (tk.Event): The mouse motion event that tracks the cursor position.
        """
        # Get the current width and height of the frame
        width = self.winfo_width()
        height = self.winfo_height()

        # Change cursor to indicate horizontal resizing if the cursor is near the right edge
        if event.x > width - self.dragBandWidth:
            self.config(cursor='sb_h_double_arrow')
        else:
            self.config(cursor='')

        # If horizontal resizing is enabled, resize the frame width according to mouse position
        if self.resizeMode == self.HORIZONTAL:
            self.config(width=event.x)



class ResizableFrameRightEdgeScrollV(ResizableFrameRightEdge):
    """
    A frame that can be resized from the right edge and scrolled vertically. Inherits from 
    `ResizableFrameRightEdge` and extends it by adding vertical scrolling capability using 
    a canvas and scrollbar.

    This frame combines the functionality of resizing from the right edge with the ability 
    to display content that can be scrolled vertically.

    Arguments:
        - All arguments accepted by `tk.Frame` are valid, including background, bg, 
          borderwidth, and more.
        
    Example usage:
        root.columnconfigure(0, weight=0)
        
        # Create an instance of the ResizableFrame with scroll capability
        resScrollFrame = ResizableFrameRightEdgeScrollV(root)
        
        # Place the frame on the grid
        resScrollFrame.grid(row=0, column=0, sticky='NWS')
        
        # Add content inside the frame
        frame = tk.Frame(resScrollFrame.scrollFrame, bg='blue')
        frame.grid(row=0, column=0, sticky='NEWS')
    """
    
    def __init__(self, parent, *args, **kw):
        """
        Initializes the ResizableFrameRightEdgeScrollV class, which allows resizing from the 
        right edge and adding vertical scrolling functionality using a canvas and scrollbar.

        Arguments:
            parent (tk.Widget): The parent widget where the frame will be placed.
            *args, **kw: Arguments passed to the parent class constructor.
        """
        super().__init__(parent, *args, **kw)
        
        # Inspired by the solution from Stack Overflow: 
        # https://stackoverflow.com/questions/16188420/tkinter-scrollbar-for-frame
        
        # Configure columns, where column 0 (scrolling canvas) will take available space 
        # and column 1 (scrollbar) has fixed space
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        
        # Create a vertical scrollbar and place it in column 1
        self.vscrollbar = ttk.Scrollbar(self, orient='vertical')
        self.vscrollbar.grid(row=0, column=1, sticky='NWS', padx=(0, self.dragBandWidth), pady=(3, 3))
        
        # Create a canvas for scrolling the content and configure its vertical scrolling
        self.canvas = tk.Canvas(self, highlightthickness=0, yscrollcommand=self.vscrollbar.set)
        self.canvas.grid(row=0, column=0, sticky='NEWS', padx=(3, 3), pady=(3, 3))
        
        # Initially reset the canvas view to the top-left corner
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # Create a frame inside the canvas which will contain the scrollable content
        self.scrollFrame = tk.Frame(self.canvas, bg='red')
        self.scrollFrame.columnconfigure(0, weight=1)
        self.scrollFrame.rowconfigure(0, weight=1)
        
        # Create a window on the canvas for the scrollable frame
        self.scrollFrame_id = self.canvas.create_window(0, 0, window=self.scrollFrame, anchor='nw')

        # Bind mouse events for enabling and disabling mouse wheel scrolling when the mouse enters/exits the frame
        self.bind('<Enter>', self.boundToMouseWheel)
        self.bind('<Leave>', self.unboundToMouseWheel)
        
        # Bind the scrollable frame and canvas to each other for size adjustments
        self.scrollFrame.bind('<Configure>', self._configure_scrollFrame)
        self.canvas.bind('<Configure>', self._configure_canvas)
        
    def _configure_scrollFrame(self, event):
        """
        Adjusts the canvas scroll region based on the size of the inner frame. 
        This ensures that the canvas is able to scroll the entire content of the inner frame.

        Args:
            event (tk.Event): The event triggered when the scrollFrame is resized.
        """
        # Get the size of the scrollable frame
        size = (self.scrollFrame.winfo_reqwidth(), self.scrollFrame.winfo_reqheight())
        
        # Update the scrollable region of the canvas based on the scrollFrame size
        self.canvas.config(scrollregion="0 0 %s %s" % size)
        
        # If the scrollFrame's width is different from the canvas, update canvas width
        if self.scrollFrame.winfo_reqwidth() != self.canvas.winfo_width():
            self.canvas.config(width=self.scrollFrame.winfo_reqwidth())

    def _configure_canvas(self, event):
        """
        Updates the width of the scrollable frame to match the width of the canvas, 
        ensuring that the frame fills the canvas.

        Args:
            event (tk.Event): The event triggered when the canvas is resized.
        """
        # If the width of the canvas is different from the scrollFrame, update the frame's width
        if self.scrollFrame.winfo_reqwidth() != self.canvas.winfo_width():
            self.canvas.itemconfigure(self.scrollFrame_id, width=self.canvas.winfo_width())
        
    def boundToMouseWheel(self, event):
        """
        Binds the mouse wheel event to enable scrolling when the mouse is inside the frame.
        
        Args:
            event (tk.Event): The event triggered when the mouse enters the frame.
        """
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def unboundToMouseWheel(self, event):
        """
        Unbinds the mouse wheel event when the mouse leaves the frame, stopping the scroll.
        
        Args:
            event (tk.Event): The event triggered when the mouse leaves the frame.
        """
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        """
        Handles the mouse wheel scrolling. The frame will scroll only if its height 
        exceeds the height of the canvas, otherwise no scrolling occurs.
        
        Args:
            event (tk.Event): The mouse wheel event.
        """
        # Get the height of the scrollable frame and canvas
        scrollFrameLength = self.scrollFrame.winfo_height()
        canvasLength = self.canvas.winfo_height()

        # If the scrollable frame is taller than the canvas, scroll the content
        if scrollFrameLength > canvasLength:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")



class ResizableFrameLeftEdge(ResizableFrame):
    """
    A frame that can be resized from the left edge. Inherits from `ResizableFrame` 
    and allows the frame to be resized by dragging its left edge.

    Arguments:
        - All arguments accepted by `tk.Frame` are valid, including background, bg, 
          borderwidth, and more.

    Example usage:
        root.columnconfigure(0, weight=0)

        # Create an instance of the ResizableFrame that can be resized from the left edge
        resFrame = ResizableFrameLeftEdge(root, background="blue", width=100, height=100)

        # Place the frame in the grid layout
        resFrame.grid(row=0, column=0, sticky='NWS')
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initializes the ResizableFrameLeftEdge class, which allows resizing from the left edge.
        
        Arguments:
            *args, **kwargs: Arguments passed to the parent class constructor.
        """
        super().__init__(*args, **kwargs)

    def StartResize(self, event):
        """
        Sets the resize mode to horizontal resizing if the left mouse button is clicked 
        near the left edge of the frame. The frame can only be resized horizontally from 
        the left edge.

        Args:
            event (tk.Event): The event triggered by clicking the mouse button.
        """
        # Extract the width of the frame
        width = self.winfo_width()

        # If the mouse click is close to the left edge, allow horizontal resizing
        if event.x < self.dragBandWidth:
            self.resizeMode = self.HORIZONTAL
        else:
            self.resizeMode = self.NONE

    def MonitorCursorPosition(self, event):
        """
        Monitors the position of the cursor and changes the cursor icon if it is close to 
        the left edge of the frame. If horizontal resizing is allowed, the frame will resize 
        as the cursor moves.

        Args:
            event (tk.Event): The event triggered by mouse movement.
        """
        # Extract the width and height of the frame
        width = self.winfo_width()
        height = self.winfo_height()

        # If the cursor is close to the left edge, change the cursor to a resize icon
        if event.x < self.dragBandWidth:
            self.config(cursor='sb_h_double_arrow')
        else:
            self.config(cursor='')

        # If horizontal resizing is allowed, resize the frame with the cursor's position
        if self.resizeMode == self.HORIZONTAL:
            self.config(width=width - event.x)



class ResizableFrameTopEdge(ResizableFrame):
    """
    A frame that can be resized from the top edge. Inherits from `ResizableFrame` 
    and allows the frame to be resized by dragging its top edge.

    Arguments:
        - All arguments accepted by `tk.Frame` are valid, including background, bg, 
          borderwidth, and more.

    Example usage:
        root.columnconfigure(0, weight=0)

        # Create an instance of the ResizableFrame that can be resized from the top edge
        resFrame = ResizableFrameTopEdge(root, background="blue", width=100, height=100)

        # Place the frame in the grid layout
        resFrame.grid(row=0, column=0, sticky='NES')
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initializes the ResizableFrameTopEdge class, which allows resizing from the top edge.
        
        Arguments:
            *args, **kwargs: Arguments passed to the parent class constructor.
        """
        super().__init__(*args, **kwargs)

    def StartResize(self, event):
        """
        Sets the resize mode to vertical resizing if the left mouse button is clicked 
        near the top edge of the frame. The frame can only be resized vertically from 
        the top edge.

        Args:
            event (tk.Event): The event triggered by clicking the mouse button.
        """
        # Extract the width of the frame
        width = self.winfo_width()

        # If the mouse click is close to the top edge, allow vertical resizing
        if event.y < self.dragBandWidth:
            self.resizeMode = self.VERTICAL
        else:
            self.resizeMode = self.NONE

    def MonitorCursorPosition(self, event):
        """
        Monitors the position of the cursor and changes the cursor icon if it is close to 
        the top edge of the frame. If vertical resizing is allowed, the frame will resize 
        as the cursor moves.

        Args:
            event (tk.Event): The event triggered by mouse movement.
        """
        # Extract the width and height of the frame
        width = self.winfo_width()
        height = self.winfo_height()

        # If the cursor is close to the top edge, change the cursor to a resize icon
        if event.y < self.dragBandWidth:
            self.config(cursor='sb_v_double_arrow')
        else:
            self.config(cursor='')

        # If vertical resizing is allowed, resize the frame with the cursor's position
        if self.resizeMode == self.VERTICAL:
            self.config(height=height - event.y)
