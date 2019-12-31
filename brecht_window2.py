import tkinter as tk
from tkinter import ttk
import brecht as br

root = tk.Tk()
# root.geometry('600x400')
root.title('Brecht 0.0.2')
root.resizable(False, False)

user_text = tk.StringVar()

def create_instance():
    global text
    text = br.Text(user_text.get())

#********************************************FRAMES**********************************

#FRAME BUTTONS
Button_Frame = ttk.Frame(root)
Button_Frame.grid(sticky = 'ns')

#FRAME TEXT
Text_Frame = ttk.Frame(root)
Text_Frame.grid(row =0, column =1, sticky = 'ns')

#********************************************WIDGETS**********************************


#WIDGET LABEL
name_label = ttk.Label(Button_Frame, text='Text: ')
name_label.grid(row =0, column = 0)

#WIDGET ENTRY
name_entry = ttk.Entry(Button_Frame, textvariable = user_text)
name_entry.grid(row = 0, column = 1)
name_entry.focus()

#WIDGET TEXT
text_widget = tk.Text(Text_Frame) 
text_widget.grid()

#********************************************BUTTONS**********************************


#BUTTON OPEN LOCAL FILE
go_button = ttk.Button(Button_Frame, text = 'Go', command = create_instance)
go_button.grid(row = 1, column = 0, sticky = 'WE', columnspan = 2)

#BUTTON UPLOAD FILE
go_button = ttk.Button(Button_Frame, text = 'Go', command = create_instance)
go_button.grid(row = 1, column = 0, sticky = 'WE', columnspan = 2)

#PASTE TEXT
go_button = ttk.Button(Button_Frame, text = 'Go', command = create_instance)
go_button.grid(row = 1, column = 0, sticky = 'WE', columnspan = 2)

#BUTTON QUIT
quit_button = ttk.Button(Button_Frame, text = 'Quit', command = root.destroy)
quit_button.grid(row = 6, column = 0, sticky = 'WE', columnspan = 2)


#********************************************SCROLLBAR**********************************

text_scroll = ttk.Scrollbar(Text_Frame, orient = 'vertical', command = text_widget.yview)
text_scroll.grid(row =0, column = 2, sticky = 'ns')
text_widget['yscrollcommand'] = text_scroll.set


root.mainloop()

