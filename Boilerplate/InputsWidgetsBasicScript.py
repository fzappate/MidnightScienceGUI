import tkinter as tk
from tkinter import ttk 

import geargeninputs 

def printToScreen(input):
    # input: this is an input object
    input.printDictionaryToScreen()

def printToTxt(input):
    # input: this is an input object

    input.printDictionaryToTxt()



# Root 
root = tk.Tk()
root.title("Inputs Widget") 
# root.geometry('600x400')
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)


# Inputs frame
inputs_frame = ttk.Frame(root)
inputs_frame.grid(row=0,column=0,sticky='N')

# Create the object with the data of the test input collection 
testInput = geargeninputs.TestInputWidget(inputs_frame)

# Buttons frame
buttons_frame = ttk.Frame(root)
buttons_frame.grid(row=1,column=0)


btn1_button = ttk.Button(buttons_frame,text='toTxt', command = lambda: printToTxt(testInput))
btn1_button.grid(row=0,column=0)

btn2_button = ttk.Button(buttons_frame,text='toScreen', command = lambda: printToScreen(testInput))
btn2_button.grid(row=0,column=1)


root.mainloop()