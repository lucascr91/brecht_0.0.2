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


class Fourth_window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Brecht 0.0.2')
        self.resizable(False, False)

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

class Canonical(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)


root = Fourth_window()
#FRAMES
quit_w4 = Quit_Frame(root, 'Start new session', combine_funcs(sort_words, show_word))
quit_w4.pack(side = 'left')

text_w4 = Canonical(root)
text_w4.pack(side = 'top', fill = 'both', expand = True)

button_w4 = Button_Frame(root)
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



text = br.Text('user_text.txt')




root.mainloop()

