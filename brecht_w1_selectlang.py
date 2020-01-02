import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle


class Brecht_Master(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.geometry('600x400')
        self.title('Brecht 0.0.2')
        self.resizable(False, False)
#Style
        style = ThemedStyle(self)
        style.set_theme("arc")

root = Brecht_Master()

storage_variable = tk.StringVar()

option_one = ttk.Radiobutton(
	root,
	text="Deutsch",
	variable=storage_variable,
	value="de"
)

option_two = ttk.Radiobutton(
	root,
	text="English",
	variable=storage_variable,
	value="en"
)

option_three = ttk.Radiobutton(
	root,
	text="Français",
	variable=storage_variable,
	value="fr"
)

option_one.pack()
option_two.pack()
option_three.pack()

# print(storage_variable.get())

root.mainloop()

print(storage_variable.get())