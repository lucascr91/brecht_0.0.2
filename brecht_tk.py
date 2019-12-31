import tkinter as tk
from tkinter import ttk
import brecht as br

def create_instance():
    global text
    text = br.Text(user_text.get())

def print_verbs():
    global verbs
    verbs = text.verbs

    return text_widget.insert("1.0", str(verbs))


root = tk.Tk()
root.geometry('600x400')
root.title('Brecht 0.0.2')
root.resizable(False, False)

# for m in range(3):
#     root.rowconfigure(m, weight =1)

# root.columnconfigure(0, weight = 4)
# root.columnconfigure(1, weight = 1)
# root.columnconfigure(2, weight = 4)





user_text = tk.StringVar()

#********************************************FRAMES**********************************

#FRAME BUTTONS
Button_Frame = ttk.Frame(root)
Button_Frame.grid(sticky = 'NS')

#FRAME TEXT
Text_Frame = ttk.Frame(root)
Text_Frame.grid(row =0, column =1, sticky = 'NS')

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


#BUTTON GO
go_button = ttk.Button(Button_Frame, text = 'Go', command = create_instance)
go_button.grid(row = 1, column = 0, sticky = 'WE', columnspan = 2)

#BUTTON LIST VERBS
verbs_button = ttk.Button(Button_Frame, text = 'List Verbs', command = print_verbs)
verbs_button.grid(row = 2, column = 0, sticky = 'WE', columnspan = 2)

#BUTTON QUIT
quit_button = ttk.Button(Button_Frame, text = 'Quit', command = root.destroy)
quit_button.grid(row = 3, column = 0, sticky = 'WE', columnspan = 2)

root.mainloop()

