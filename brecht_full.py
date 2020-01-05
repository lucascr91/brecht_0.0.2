import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from PIL import ImageTk, Image
from time import sleep
from ttkthemes import ThemedStyle
from tkinter.font import Font
import webbrowser
import random
import pickle

lang = 'DE'


# Abre dicionário local
pickle_in = open('dictionaries_{0}/brecht_dict_{0}.pkl'.format(lang), 'rb')
brecht_dict = pickle.load(pickle_in)

#Abre vocabulário do usuário
pickle_in = open('dictionaries_{0}/brecht_uservocab_{0}.pkl'.format(lang), 'rb')
brecht_uservocab = pickle.load(pickle_in)

#Abre palavras marcadas como importantes pelo usuário
pickle_in = open('dictionaries_{0}/brecht_userimportant_{0}.pkl'.format(lang), 'rb')
brecht_userimportant = pickle.load(pickle_in)

# Abre lista de não encontrados
pickle_in2 = open('dictionaries_{0}/brecht_lista_not_found_{0}.pkl'.format(lang), 'rb')
brecht_not_found = pickle.load(pickle_in2)

def hl_callback(event):
    webbrowser.open_new("http://lucascr.com.br/")

def task():
    sleep(4)
    Loading_Frame.destroy()

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
        print('Hi, my actual fucking name is ' + str(selected_language))

def create_instance(*args):
    global text
    global text_words
    text = br.Text('user_text.txt')
    adj = text.adjectives
    nouns = text.nouns
    verbs = text.verbs

    text_words = adj + nouns + verbs

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
def sort_words():
    global selected_words
    selected_words = random.sample(text_words, 5)

def callback(event):
    if event.widget['text']=='Skip':
        text_widget4.delete('1.0', 'end')
        selected_words.remove(selected_words[0])
        show_word()
    elif event.widget['text']=='Show me':
        text_widget4.delete('1.0', 'end')
        meaning = br.Words(selected_words[0]).meaning
        brecht_dict[selected_words[0]] = meaning
        selected_words.remove(selected_words[0])
        return text_widget4.insert('1.0', 'Here is the meaning: \n'+
        meaning)
        # Salvando o dicionário atualizado
        pickle_out = open('dictionaries_{0}/brecht_dict_{0}'.format(lang), 'wb')
        pickle.dump(brecht_dict, pickle_out)
        pickle_out.close()

def show_word():
    if len(selected_words)>0:
        text_widget4.delete('1.0', 'end')
        text_widget4.insert('1.0', '{}'.format(selected_words[0]), ["red_text","center_text", 'font20'])
        text_widget4.place(relx=0.5, rely=0.5, anchor='n')
    else:
        text_widget4.delete('1.0', 'end')
        text_widget4.insert('1.0', 'Congratulations! You finish the 5 words')


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
    def __init__(self, container, label_1, function_1, next_button = True):
        super().__init__(container)
        self.label_1 = label_1
        self.function_1 = function_1
        self.next_button = next_button

        n_button = ttk.Button(self, text = label_1, command = function_1)
        n_button.pack(side = 'left', padx =5, pady = 5, fill = 'x')

        if next_button:
            m_button = ttk.Button(self, text = 'Next', command = show_word)
            m_button.pack(side = 'left', padx =5, pady = 5, fill = 'x')

        quit_button = ttk.Button(self, text = 'Quit', command = root.destroy)
        quit_button.pack(side = 'left', padx =5, pady = 5, fill = 'x')

class Button_Frame(ttk.Frame):
    def __init__(self, container, window = 2):
        super().__init__(container)
        self.window = window

        if window == 2:
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
        elif window == 4:
            button1 = ttk.Button(self, text = 'Show me')
            container.bind('<Button-1>', callback) 
            button1.pack(side = 'top')

            button2 = ttk.Button(self, text = 'Skip')
            container.bind('<Button-2>', callback) 
            button2.pack(side = 'top')

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

class Button_Frame_w4(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        button1 = ttk.Button(self, text = 'Show me')
        container.bind('<Button-1>', callback) 
        button1.pack(side = 'left')

        button2 = ttk.Button(self, text = 'Skip')
        container.bind('<Button-2>', callback) 
        button2.pack(side = 'left')


class Quit_Frame_w4(ttk.Frame):
    def __init__(self, container, label_1, function_1):
        super().__init__(container)
        self.label_1 = label_1
        self.function_1 = function_1

        n_button = ttk.Button(self, text = label_1, command = function_1)
        n_button.pack(side = 'top', padx =5, pady = 5, fill = 'x')
        
        next_button = ttk.Button(self, text = 'Next', command = show_word)
        next_button.pack(side = 'top', padx =5, pady = 5, fill = 'x')

        quit_button = ttk.Button(self, text = 'Quit', command = root.destroy)
        quit_button.pack(side = 'top', padx =5, pady = 5, fill = 'x')

root = Brecht_Master()

# style1 = ttk.Style(window3)
# style1.theme_use('classic')



user_text = tk.StringVar()
font.nametofont('TkDefaultFont').configure(size = 15)

#*********************WINDOW 4******************************
window4 = Canonical(root)
window4.grid(row=0, column=0, sticky="NSEW")
#FRAMES
quit_w4 = Quit_Frame_w4(window4, 'Start new session', combine_funcs(sort_words, show_word))
quit_w4.pack(side = 'left')

text_w4 = Canonical(window4)
text_w4.pack(side = 'top', fill = 'both', expand = True)

button_w4 = Button_Frame_w4(window4)
button_w4.pack(side = 'bottom')


#WIDGETS
text_widget4 = tk.Text(text_w4)
text_widget4.insert('1.0', '''Hi, here a couple of instructions to play this game. The game is organized in sessions. 
On each session, Brecht will show you 5 words. When you see one word that you already know, hit "SKIP" button and this word will not be show again.
If you don't know the presented word, hit "SHOW ME" button and Brecht will show you the word meaning and translation to English. 
When you finish with the 5 words, just hit "START NEW SESSION" to play the game again with new words.''', 'font14')
text_widget4.tag_configure('font20', font=('Times',20))
text_widget4.tag_configure('font14', font=('Times',14))
text_widget4.tag_configure("red_text", foreground ='red')
text_widget4.tag_configure("center_text", justify ='center')
text_widget4.pack()


#*********************WINDOW 3******************************
window3 = Canonical(root)
window3.grid(row=0, column=0, sticky="NSEW")
#FRAMES
next_quit = Quit_Frame(window3, 'Next', window3.destroy, next_button= False)
next_quit.pack(side = 'bottom')

button_w3 = Button_Frame(window3)
button_w3.pack(side = 'left')

text_w3 = Canonical(window3)
text_w3.pack(side = 'left')

#WIDGET TEXT
text_widget3 = tk.Text(text_w3)
text_widget3.config(font=('Times',16))
text_widget3.pack()


text_scroll = ttk.Scrollbar(text_w3, orient = 'vertical', command = text_widget3.yview)
text_scroll.pack(fill ='both', expand = True)
text_widget3['yscrollcommand'] = text_scroll.set


#*********************WINDOW 2******************************

window2 = Canonical(root)
window2.grid(row=0, column=0, sticky="NSEW")

text_w2 = Canonical(window2)
paste_label = ttk.Label(text_w2, text='Paste your text here: ')
paste_label.pack(side = 'top', pady = 20)
text_widget2 = tk.Text(text_w2)
text_widget2.config(font=('Times',16))
text_widget2.pack(side = 'top')
text_w2.pack(side ='top')

enter_quit = Quit_Frame(window2, 'Send Text', combine_funcs(create_file, create_instance, window2.destroy), next_button= False)
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


enter_quit = Quit_Frame(window1, 'Next', combine_funcs(select_lang, window1.destroy), next_button= False)
enter_quit.pack(side = 'bottom')

selected_language = var.get()


#******************WELCOME WINDOW***************************

# style = ttk.Style()
# style.configure("TLabel", font=("Times", 16, "bold"))

Loading_Frame = Canonical(root)
Loading_Frame.grid(row=0, column=0, sticky="NSEW")

img = ImageTk.PhotoImage(Image.open('brecht_drawing_welcome.jpg'))
panel = tk.Label(Loading_Frame, image = img, bg = 'white')
panel.pack(side = "top", fill = "both", expand = "yes")
link1 = tk.Label(Loading_Frame, text="Lucas Cavalcanti Rodrigues", 
fg="blue", bg = 'white', cursor = 'hand2')
link1.config(font=("Courier", 8))
Loading_Frame.bind("<Button-1>", hl_callback)
link1.pack(side = 'right')
description = tk.Label(Loading_Frame, text="Brecht was developed by ", bg = 'white')
description.config(font=("Courier", 8))
description.pack(side = 'right')
Loading_Frame.after(200, task)



 #****************END WELCOME WINDOW************************

root.mainloop()

