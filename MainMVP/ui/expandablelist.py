from tkinter import ttk

class ExpandableList(ttk.Frame):
    def __init__(self,parent, dict , rowCounter)->None:
        super().__init__(parent)
        # Input panel 

        # Extract the info from the dictionary and save them in the object 
        self.name = dict["name"]
        self.descr = dict["description"]
        self.img = dict["image"]
        self.type = dict["type"]
        self.value = dict["value"]
        self.rowPosition = rowCounter

        self.allEntries = []

        self.addButton = ttk.Button(self,text='Add',command = self.addEntry)
        self.addButton.grid(row=0,column=0,sticky='W')

        self.firstEntry = ErasableEntry(self)
        self.firstEntry.grid(row=1,column=0)
        self.allEntries.append(self.firstEntry)


    def addEntry(self):
        ent = ErasableEntry(self)
        entryPosition = len(self.allEntries)+1
        ent.grid(row = entryPosition,column=0)
        self.allEntries.append( ent )
     

class ErasableEntry(ttk.Frame):
    def __init__(self,parent)->None:
        super().__init__(parent)

        self.firstEntry = ttk.Entry(self,width = 20)
        self.firstEntry.grid(row=1,column=0)

        self.eraseButton = ttk.Button(self,text='X',width = 5,command=self.destroy)
        self.eraseButton.grid(row=1,column=1)
