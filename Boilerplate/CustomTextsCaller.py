import tkinter as tk
from tkinter import ttk 

import customtext

# Root 
root = tk.Tk()
root.title("Scrollable text") 
root.geometry('600x400')
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

text_frame = ttk.Frame(root)
text_frame.columnconfigure(0, weight=1)
text_frame.rowconfigure(0, weight=1)

text_frame.grid(sticky='NEWS')
scrollText = customtext.VerticalScrollText(text_frame)

root.mainloop()