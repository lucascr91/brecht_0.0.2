import tkinter as tk
from tkinter import ttk
import brecht as br
import tkinter.font as font

class Third_window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Brecht 0.0.2')
        self.resizable(False, False)

root = Third_window()

font.nametofont('TkDefaultFont').configure(size = 15)



user_text = tk.StringVar()

text = br.Text('user_text.txt')

def print_adjectives():
    global adjectives
    adjectives = text.adjectives
    text_widget.delete('1.0', 'end')
    return text_widget.insert("1.0", str(adjectives))

def print_nouns():
    global nouns
    nouns = text.nouns
    text_widget.delete('1.0', 'end')
    return text_widget.insert("1.0", str(nouns))

def print_verbs():
    global verbs
    verbs = text.verbs
    text_widget.delete('1.0', 'end')
    return text_widget.insert("1.0", str(verbs))

def print_text():
    global actual_txt
    text_widget.delete('1.0', 'end')
    actual_txt = text.actual_text
    return text_widget.insert("1.0", str(actual_txt))



#********************************************FRAMES**********************************

class EnterQuit_Frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        next_button = ttk.Button(self, text = 'Next', command = root.destroy)
        next_button.pack(side = 'left', padx =5, pady = 5, fill = 'x')

        quit_button = ttk.Button(self, text = 'Quit', command = root.destroy)
        quit_button.pack(side = 'left', padx =5, pady = 5, fill = 'x')

class Button_Frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        #BUTTON LIST ADJECTIVES
        adj_button = ttk.Button(self, text = 'List Adjectives', command = print_adjectives)
        adj_button.pack(side = 'top', padx =5, pady = 5, fill = 'x')

        #BUTTON LIST NOUNS
        nouns_button = ttk.Button(self, text = 'List Nouns', command = print_nouns)
        nouns_button.pack(side = 'top', padx =5, pady = 5, fill = 'x')

        #BUTTON LIST VERBS
        verbs_button = ttk.Button(self, text = 'List Verbs', command = print_verbs)
        verbs_button.pack(side = 'top', padx =5, pady = 5, fill = 'x')

        #BUTTON FULL TEXT
        text_button = ttk.Button(self, text = 'Full Text', command = print_text)
        text_button.pack(side = 'top', padx =5, pady = 5, fill = 'x')

 
class Text_Frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)



#FRAMES
frame1 = EnterQuit_Frame(root)
frame1.pack(side = 'bottom')

frame2 = Button_Frame(root)
frame2.pack(side = 'left')

frame3 = Text_Frame(root)
frame3.pack(side = 'left')

#WIDGET TEXT
text_widget = tk.Text(frame3)
text_widget.pack()


text_scroll = ttk.Scrollbar(frame3, orient = 'vertical', command = text_widget.yview)
text_scroll.pack(fill ='both', expand = True)
text_widget['yscrollcommand'] = text_scroll.set

root.mainloop()

