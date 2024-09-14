from tkinter import ttk
import tkinter as tk
import os 

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass 

class ResizableFrame(tk.Frame):    
    def __init__(self, *args, **kwargs):
        '''
        Initialize a resizable frame that can be resized dragging the right edge.
        
        Valid resource names: background, bd, bg, borderwidth, class, colormap, container, cursor, height, highlightbackground, 
        highlightcolor, highlightthickness, relief, takefocus, visual, width.

        
        -----USAGE-----
            
        root.columnconfigure(0,weight = 0)

        resFrame = ResizableFrame(root, background = "blue",width = 100, height = 100)
        
        resFrame.grid(row = 0, column=0,sticky = 'NWS')
        '''
        super().__init__(*args, **kwargs)
        self.pack_propagate(0)
        self.grid_propagate(0)

        # Resize mode
        self.NONE = 0
        self.HORIZONTAL = 1
        self.VERTICAL = 2

        self.resizeMode = self.NONE
        self.isDragBandHeld = True
        
        self.bind("<ButtonPress-1>", self.StartResize)
        self.bind("<ButtonRelease-1>", self.StopResize)
        self.bind("<Motion>", self.MonitorCursorPosition)

        self.cursor = ''
        self.dragBandWidth = 10


    def StartResize(self, event):
        '''Set the resize mode if the left button of the mouse is clicked close to the right or bottom edge of the frame.'''
        # Extract the size of the frame
        width = self.winfo_width()
        height = self.winfo_height()

        # If the mouse left button is clicked close to the right edge allow horizontal resizing
        if  event.x > width-self.dragBandWidth : 
            self.resizeMode = self.HORIZONTAL       
        else:
            self.resizeMode = self.NONE


    def MonitorCursorPosition(self,event):        
        '''Check whether the cursor is close to the right or bottom edge of the frame.'''
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

        print('width: ', width)
        
        
    

    def StopResize(self, event):
        '''Disable any resize mode and set the standard arrow as cursor.'''
        self.resizeMode = self.NONE
        self.config(cursor='')
 
# Root 
root = tk.Tk()
root.title("Command Widget") 
root.geometry('600x400')
root.columnconfigure(0,weight = 0)
root.columnconfigure(1,weight = 1)
root.rowconfigure(0,weight = 1)

# Resizable frame
resFrame = ResizableFrame(root, width = 10)
# resFrame.pack(fill="both", expand=1)
resFrame.grid(row = 0, column=0,sticky = 'NWS')
# resFrame.columnconfigure(0,weight = 1)

# To insert notebook uncomment from here --> ======================
tab_notebook = ttk.Notebook(resFrame)
# Implement frames inside the notebook
tab1 = ttk.Frame(tab_notebook)
tab2 = ttk.Frame(tab_notebook)
tab_notebook.add(tab1, text='Tab1',sticky='news')
tab_notebook.add(tab2, text='Tab2',sticky='news')
tab_notebook.pack(expand=True, fill="both",padx=(0,10))
# <-- =============================================================
# btn = tk.Button(resFrame,text = 'ciaociao')
# btn.pack(expand=True,fill='both',padx=(0,10))
# btn.grid(row = 0,column=0,sticky= 'NEWS')

frame1 = tk.Frame(root, bg= "red",width = 100, height = 100)
frame1.grid(row = 0, column = 1,sticky = 'NEWS')

root.mainloop()