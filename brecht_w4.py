import tkinter as tk
from tkinter import ttk
import brecht as br
import tkinter.font as font

class Fourth_window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Brecht 0.0.2')
        self.resizable(False, False)

root = Fourth_window()

text = br.Text('user_text.txt')




root.mainloop()

