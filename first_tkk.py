import tkinter as tk
from tkinter import ttk

def greet():
    print("Hello, {}!".format(user_name.get()))


root = tk.Tk()
root.geometry('600x400')

user_name = tk.StringVar()

name_label = ttk.Label(root, text='Name: ')
name_label.pack(side='left', padx=(0,10))
name_entry = ttk.Entry(root, width=15, textvariable = user_name)
name_entry.pack(side='left')
name_entry.focus()

greet_button = ttk.Button(root, text = 'Greet', command = greet)
greet_button.pack(side = 'left')

quit_button = ttk.Button(root, text = 'Quit', command = root.destroy)
quit_button.pack(side = 'right')

root.mainloop()