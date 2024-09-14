import tkinter as tk
from tkinter import ttk 

# Root 
root = tk.Tk()
root.title("Scrollable text") 
root.geometry('600x400')
root.columnconfigure(0,weight=1)

# Text
text = tk.Text(root,height = 8)
text.grid(column =0, row=0,sticky='EW')
text.insert('1.0','Please eneter a comment')
# text['state']='disabled'

# Scroll bar 
text_scroll = ttk.Scrollbar(root, orient='vertical',command = text.yview)
text_scroll.grid(row=0,column=1,sticky='NS')

# Link the text to the scroll bar
text['yscrollcommand'] = text_scroll.set
root.mainloop()