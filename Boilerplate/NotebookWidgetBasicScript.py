import tkinter as tk
from tkinter import ttk 

# Root 
root = tk.Tk()
root.title("Notebook Widget") 
root.geometry('600x400')

# Make sure that the notebook expands in the whole root
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

# Create tab notebook 
tab_notebook = ttk.Notebook(root)
tab_notebook.grid(row=0,column=0)

# Create the tabs (frame)
tab1 = ttk.Frame(tab_notebook)
tab2 = ttk.Frame(tab_notebook)
tab3 = ttk.Frame(tab_notebook)
# Add the tabs (frame) to the notebook
tab_notebook.add(tab1, text='Gear Generator')
tab_notebook.add(tab2, text='Geometry Processor')
tab_notebook.add(tab3, text='Multics')
tab_notebook.pack(expand=1, fill="both")

# Create the labels
lab1 = ttk.Label(tab1,text="table 1")
lab1.grid(row=0,column=0)

lab2 = ttk.Label(tab2,text="table 2")
lab2.grid(row=0,column=0)

lab3 = ttk.Label(tab3,text="table 3")
lab3.grid(row=0,column=0)



root.mainloop()