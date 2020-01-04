import tkinter as tk
from tkinter import ttk
import brecht_de as br
import tkinter.font as font
import pickle
import random
from time import sleep

lang = 'DE'


text = br.Text('user_text.txt')

adj = text.adjectives
nouns = text.nouns
verbs = text.verbs

text_words = adj + nouns + verbs



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

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def sort_words():
    global selected_words
    selected_words = random.sample(text_words, 5)

def callback(event):
    if event.widget['text']=='Yes':
        text_widget4.delete('1.0', 'end')
        show_word(1)
    elif event.widget['text']=='No':
        text_widget4.delete('1.0', 'end')
        return text_widget4.insert('1.0', 'Here is the meaning: \n'+
        br.Words(selected_words[0]).meaning)
    elif event.widget['text']=='Vocabulary':
        brecht_uservocab.append(selected_words[0])
        text_widget4.delete('1.0', 'end')
        return text_widget4.insert('1.0', 'This word is now part of your vocabulary and it will not be show again')

def show_word(index = 0):
    text_widget4.insert('1.0', 'Do you know the meaning of the word {}?'.format(selected_words[index]))
    

class Fourth_window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Brecht 0.0.2')
        self.resizable(False, False)

class Button_Frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        button1 = ttk.Button(self, text = 'Yes')
        container.bind('<Button-1>', callback) 
        button1.pack(side = 'left')

        button2 = ttk.Button(self, text = 'No')
        container.bind('<Button-2>', callback) 
        button2.pack(side = 'left')

        button3 = ttk.Button(self, text = 'Vocabulary')
        container.bind('<Button-3>', callback) 
        button3.pack(side = 'left')


class Quit_Frame(ttk.Frame):
    def __init__(self, container, label_1, function_1):
        super().__init__(container)
        self.label_1 = label_1
        self.function_1 = function_1

        next_button = ttk.Button(self, text = label_1, command = function_1)
        next_button.pack(side = 'top', padx =5, pady = 5, fill = 'x')

        quit_button = ttk.Button(self, text = 'Quit', command = root.destroy)
        quit_button.pack(side = 'top', padx =5, pady = 5, fill = 'x')

class Canonical(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)


root = Fourth_window()
#FRAMES
text_w4 = Canonical(root)
text_w4.pack(side = 'top', fill = 'both', expand = True)

button_w4 = Button_Frame(root)
button_w4.pack(side = 'bottom')

quit_w4 = Quit_Frame(root, 'Start', combine_funcs(sort_words, show_word))
quit_w4.pack(side = 'right')

#WIDGETS
text_widget4 = tk.Text(text_w4)
text_widget4.pack()



text = br.Text('user_text.txt')




root.mainloop()

