import tkinter as tk
from tkinter import ttk
import brecht as br

root = tk.Tk()
root.geometry('600x400')
root.title('Brecht 0.0.2')
root.resizable(False, False)

user_text = tk.StringVar()

def create_instance():
    global text
    text = br.Text(user_text.get())

#********************************************FRAMES**********************************
Upload_Frame = ttk.Frame(root)
Upload_Frame.pack(side = 'top')

Text_Frame = ttk.Frame(root)
Text_Frame.pack(side = 'top')

#********************************************WIDGETS**********************************


#WIDGET LABEL
open_label = ttk.Label(Upload_Frame, text='Open local file: ')
open_label.pack(side = 'left')

#WIDGET ENTRY
open_entry = ttk.Entry(Upload_Frame, textvariable = user_text)
open_entry.pack(side = 'left', fill = 'x')
open_entry.focus()


#WIDGET LABEL
paste_label = ttk.Label(Text_Frame, text='Paste: ')
paste_label.pack(side = 'top')

#WIDGET TEXT
text_entry = ttk.Entry(Text_Frame, textvariable = user_text) 
text_entry.pack(side = 'left', fill = 'both')


#BUTTON QUIT
quit_button = ttk.Button(Text_Frame, text = 'Quit', command = root.destroy)
quit_button.pack(side = 'top')


#********************************************SCROLLBAR**********************************

# text_scroll = ttk.Scrollbar(root, orient = 'vertical')
# text_scroll.pack(row =0, column = 2, sticky = 'ns')
# text_entry['yscrollcommand'] = text_scroll.set


root.mainloop()

