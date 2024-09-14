from tkinter import ttk
import tkinter as tk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


class ExpandableList(ttk.Frame):
    def __init__(self,parent)->None:
        super().__init__(parent)
        # Input panel 
        self.allEntries = []

        self.addButton = ttk.Button(self,text='Add',command = self.addEntry)
        self.addButton.grid(row=0,column=0,sticky='W')

        self.firstEntry = ErasableEntry(self)
        self.firstEntry.grid(row=1,column=0)
        self.allEntries.append(self.firstEntry)


    def addEntry(self):
        ent = ErasableEntry(frame)
        entryPosition = len(self.allEntries)+1
        ent.grid(row = entryPosition,column=0)
        self.allEntries.append( ent )
     

class ErasableEntry(ttk.Frame):
    def __init__(self,parent)->None:
        super().__init__(parent)

        self.firstEntry = tk.Entry(self,width = 20)
        self.firstEntry.grid(row=1,column=0)

        self.eraseButton = ttk.Button(self,text='X',width = 5,command=self.destroy)
        self.eraseButton.grid(row=1,column=1)


# Root 
#Window
root = tk.Tk()
root.geometry("800x700")
root.title("Account Overview")

#Title_Frame
frame = tk.Frame(root, bg='#b1b7ba')
frame.grid(row=0,column=0)

# Frame content
list = ExpandableList(frame)
list.grid(row=0,column=0)

root.mainloop()