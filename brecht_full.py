import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from PIL import ImageTk, Image
from time import sleep
from ttkthemes import ThemedStyle
from tkinter.font import Font



def select_lang():
    if selected_language == 1:
        global br
        import brecht_de as br
    elif selected_language == 2:
        global br
        import brecht_en as br
    elif selected_language == 3:
        global br
        import brecht_fr as br
    else:
        print('Hi, my actual name is fucking' + str(selected_language))

def create_instance(*args):
    global text
    text = br.Text('user_text.txt')

def create_file(*args):
    user_input = text_widget2.get("1.0", 'end-1c')
    f = open('user_text.txt', 'w')
    f.write(user_input)
    f.close()

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def print_adjectives():
    global adjectives
    adjectives = text.adjectives
    text_widget3.delete('1.0', 'end')
    return text_widget3.insert("1.0", str(adjectives))

def print_nouns():
    global nouns
    nouns = text.nouns
    text_widget3.delete('1.0', 'end')
    return text_widget3.insert("1.0", str(nouns))

def print_verbs():
    global verbs
    verbs = text.verbs
    text_widget3.delete('1.0', 'end')
    return text_widget3.insert("1.0", str(verbs))

def print_text():
    global actual_txt
    text_widget3.delete('1.0', 'end')
    actual_txt = text.actual_text
    return text_widget3.insert("1.0", str(actual_txt))


class Brecht_Master(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.geometry('600x400')
        self.title('Brecht 0.0.2')
        self.resizable(False, False)
#Style
        style = ThemedStyle(self)
        style.set_theme("arc")

#*************CANONICAL FRAME****************************

class Canonical(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

#*********FRAMES FROM SECOND WINDOW**********************

class Upload_Frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        #WIDGET LABEL
        open_label = ttk.Label(self, text='Open local file: ')
        open_label.pack(side = 'left')

        #WIDGET ENTRY
        open_entry = ttk.Entry(self, textvariable = user_text, font = ('Segoe UI', 15))
        open_entry.pack(side = 'left', fill = 'x')
        open_entry.focus()

#*********FRAMES FROM THIRD WINDOW**************

class Quit_Frame(ttk.Frame):
    def __init__(self, container, label_1, function_1):
        super().__init__(container)
        self.label_1 = label_1
        self.function_1 = function_1

        next_button = ttk.Button(self, text = label_1, command = function_1)
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

class Radio_Frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        option_one = ttk.Radiobutton(
            self,
            text="Deutsch",
            variable=var,
            value=1
        )

        option_two = ttk.Radiobutton(
            self,
            text="English",
            variable=var,
            value=2
        )

        option_three = ttk.Radiobutton(
            self,
            text="Français",
            variable=var,
            value=3
        )

        option_one.pack(side = 'top', padx = 5, pady = 5, fill = 'both')
        option_two.pack(side = 'top', padx = 5, pady = 5, fill = 'both')
        option_three.pack(side = 'top', padx = 5, pady = 5, fill = 'both')

root = Brecht_Master()

# style1 = ttk.Style(window3)
# style1.theme_use('classic')



user_text = tk.StringVar()
font.nametofont('TkDefaultFont').configure(size = 15)

#*********************WINDOW 3******************************
window3 = Canonical(root)
window3.grid(row=0, column=0, sticky="NSEW")
#FRAMES
next_quit = Quit_Frame(window3, 'Next', window3.destroy)
next_quit.pack(side = 'bottom')

button_w3 = Button_Frame(window3)
button_w3.pack(side = 'left')

text_w3 = Canonical(window3)
text_w3.pack(side = 'left')

#WIDGET TEXT
text_widget3 = tk.Text(text_w3)
text_widget3.pack()


text_scroll = ttk.Scrollbar(text_w3, orient = 'vertical', command = text_widget3.yview)
text_scroll.pack(fill ='both', expand = True)
text_widget3['yscrollcommand'] = text_scroll.set


#*********************WINDOW 2******************************

window2 = Canonical(root)
window2.grid(row=0, column=0, sticky="NSEW")

upload = Upload_Frame(window2)
upload.pack(side ='top')

text_w2 = Canonical(window2)
paste_label = ttk.Label(text_w2, text='or paste your text here: ')
paste_label.pack(side = 'top')
text_widget2 = tk.Text(text_w2)
text_widget2.pack(side = 'top')
text_w2.pack(side ='top')

enter_quit = Quit_Frame(window2, 'Send Text', combine_funcs(create_file, create_instance, window2.destroy))
enter_quit.pack(side = 'top')

#*********************WINDOW 1******************************

window1 = Canonical(root)
window1.grid(row=0, column=0, sticky="NSEW")

question = ttk.Label(window1, 
text = 'Please, choose one language to practice:')
question.pack(side = 'top', padx = 5, pady = 40, ipady = 10)

var = tk.IntVar()
var.set(1)

radio_buttons = Radio_Frame(window1)
radio_buttons.pack(side = 'top', ipady = 10, ipadx = 10)


enter_quit = Quit_Frame(window1, 'Next', combine_funcs(select_lang, window1.destroy))
enter_quit.pack(side = 'bottom')

selected_language = var.get()


#******************WELCOME WINDOW***************************

def task():
    sleep(4)
    Loading_Frame.destroy()

style = ttk.Style()
style.configure("TLabel", font=("Times", 16, "bold"))

Loading_Frame = Canonical(root)
Loading_Frame.grid(row=0, column=0, sticky="NSEW")

img = ImageTk.PhotoImage(Image.open('brecht_drawing.jpg'))
panel = tk.Label(Loading_Frame, image = img, bg = 'white')
panel.pack(side = "top", fill = "both", expand = "yes")
label = ttk.Label(Loading_Frame, text="WELCOME", style = 'TLabel')
label.pack()
Loading_Frame.after(200, task)



 #****************END WELCOME WINDOW************************

root.mainloop()

