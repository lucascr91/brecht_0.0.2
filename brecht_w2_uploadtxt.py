import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import brecht as br
from PIL import ImageTk, Image
from time import sleep



#******************LOADING WINDOW***************************

def task():
    # The window will stay open until this function call ends.
    sleep(4) # Replace this with the code you want to run
    loading.destroy()

loading = tk.Tk()
loading.geometry('600x400')
loading.title('Brecht 0.0.2')

font.nametofont('TkDefaultFont').configure(size = 15)


label = tk.Label(loading, text="Loading ...")
label.pack()
img = ImageTk.PhotoImage(Image.open('brecht_drawing.jpg'))
panel = tk.Label(loading, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
loading.after(200, task)
loading.mainloop()

 #****************END LOADING WINDOW************************

root = tk.Tk()
root.geometry('600x400')
root.title('Brecht 0.0.2')
root.resizable(False, False)


user_text = tk.StringVar()

def create_instance(*args):
    global text
    text = br.Text(user_text.get())

def create_file(*args):
    user_input = text_entry.get("1.0", 'end-1c')
    f = open('user_text.txt', 'w')
    f.write(user_input)
    f.close

#********************************************FRAMES**********************************
Upload_Frame = ttk.Frame(root, padding = (30,5))
Upload_Frame.pack(side = 'top')

Text_Frame = ttk.Frame(root, padding = (10,15))
Text_Frame.pack(side = 'top')

EnterQuit_Frame = ttk.Frame(root, padding = (30,5))
EnterQuit_Frame.pack(side = 'top')

#********************************************WIDGETS**********************************


#WIDGET LABEL
open_label = ttk.Label(Upload_Frame, text='Open local file: ')
open_label.pack(side = 'left')

#WIDGET ENTRY
open_entry = ttk.Entry(Upload_Frame, textvariable = user_text, font = ('Segoe UI', 15))
open_entry.pack(side = 'left', fill = 'x')
open_entry.focus()


#WIDGET LABEL
paste_label = ttk.Label(Text_Frame, text='or paste your text here: ')
paste_label.pack(side = 'top')

#WIDGET TEXT
text_entry = tk.Text(Text_Frame, height=20, width=40) 
text_entry.pack(side = 'top', fill = 'both')


#BUTTON SEND
quit_button = ttk.Button(EnterQuit_Frame, text = 'Send text', command = create_file)
quit_button.pack(side = 'left',  fill = 'x')

#BUTTON QUIT
quit_button = ttk.Button(EnterQuit_Frame, text = 'Quit', command = root.destroy)
quit_button.pack(side = 'left', fill = 'x')

#********************************************WINFO_CHILDREN**********************************
# for child in Text_Frame.winfo_children:
#     child.pack_configure(padx =5, pady = 5,)

#********************************************SCROLLBAR**********************************

# text_scroll = ttk.Scrollbar(root, orient = 'vertical')
# text_scroll.pack(row =0, column = 2, sticky = 'ns')
# text_entry['yscrollcommand'] = text_scroll.set


root.mainloop()

