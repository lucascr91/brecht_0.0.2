import tkinter as tk
from tkinter import ttk
import brecht as br

root = tk.Tk()
# root.geometry('600x400')
root.title('Brecht 0.0.2')
root.resizable(False, False)

user_text = tk.StringVar()

f = open('user_text.txt', 'r')
user_text = f.read()
f.close()

text = br.Text(user_text)

def print_adjectives():
    global adjectives
    adjectives = text.adjectives
    return text_widget.insert("1.0", str(adjectives))

def print_nouns():
    global nouns
    nouns = text.nouns
    return text_widget.insert("1.0", str(nouns))

def print_verbs():
    global verbs
    verbs = text.verbs
    return text_widget.insert("1.0", str(verbs))

def print_text():
    global actual_txt
    actual_txt = text.actual_text
    return text_widget.insert("1.0", str(actual_txt))

#********************************************FRAMES**********************************

#FRAME TEXT
EnterQuit_Frame = ttk.Frame(root, padding = (30,15))
EnterQuit_Frame.pack(side = 'bottom')

#FRAME BUTTONS
Button_Frame = ttk.Frame(root, padding = (30,15))
Button_Frame.pack(side = 'left')

#FRAME TEXT
Text_Frame = ttk.Frame(root, padding = (30,15))
Text_Frame.pack(side = 'left')


#********************************************WIDGETS**********************************

#WIDGET TEXT
text_widget = tk.Text(Text_Frame) 
text_widget.pack()

#********************************************BUTTONS**********************************

#BUTTON LIST ADJECTIVES
adj_button = ttk.Button(Button_Frame, text = 'List Adjectives', command = print_adjectives)
adj_button.pack(side = 'top')

#BUTTON LIST NOUNS
nouns_button = ttk.Button(Button_Frame, text = 'List Nouns', command = print_nouns)
nouns_button.pack(side = 'top')

#BUTTON LIST VERBS
verbs_button = ttk.Button(Button_Frame, text = 'List Verbs', command = print_verbs)
verbs_button.pack(side = 'top')

#BUTTON FULL TEXT
text_button = ttk.Button(Button_Frame, text = 'Full Text', command = print_text)
text_button.pack(side = 'top')

#BUTTON NEXT
quit_button = ttk.Button(EnterQuit_Frame, text = 'Next', command = root.destroy)
quit_button.pack(side = 'left')

#BUTTON QUIT
quit_button = ttk.Button(EnterQuit_Frame, text = 'Quit', command = root.destroy)
quit_button.pack(side = 'left')


#********************************************SCROLLBAR**********************************

text_scroll = ttk.Scrollbar(Text_Frame, orient = 'vertical', command = text_widget.yview)
text_scroll.pack(fill ='both', expand = True)
text_widget['yscrollcommand'] = text_scroll.set


root.mainloop()

