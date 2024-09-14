import tkinter as tk
from tkinter import ttk 

import notebook
# Root 
root = tk.Tk()
root.title("Notebook Widget") 
root.geometry('600x400')


notebook = notebook.NotebookWidget(root)



root.mainloop()