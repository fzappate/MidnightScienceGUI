import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global FolderPath
    filename = filedialog.askdirectory()
    FolderPath.set(filename)
    change_text(filename)
    print(filename)

def change_text(txt):
   text.delete(0,tk.END)
   text.insert(0,txt)


root = tk.Tk()
root.title("Gear Generator")
root.columnconfigure(0,weight=1)
root.geometry('600x400')

folder_path = tk.StringVar()

pathFrame = ttk.Frame(root)
pathFrame.grid(row=0,column=0, sticky='EW')
pathFrame.columnconfigure(0,weight=1)
pathFrame.columnconfigure(1,weight=0)

text = ttk.Entry(pathFrame)
text.grid(row=0,column=0,sticky = "EW")

navigate = ttk.Button(text="Browse", command= browse_button)
navigate.grid(row=0, column=1)


root.mainloop()







# # Root grid configuration
# root.columnconfigure(0, weight=0)
# root.columnconfigure(1, weight=1)

# controlFrame = ttk.Frame


# root.mainloop()