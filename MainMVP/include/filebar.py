from tkinter import ttk


class FileBar(ttk.Frame):
    '''File bar class containing all the buttons of the file bar.'''

    def __init__(self, parent)->None:
        '''Initialize the file bar object.'''
        
        super().__init__(parent)
        file_button = ttk.Button(self, text='File')
        file_button.grid(row=0, column=0)