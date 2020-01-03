import tkinter as tk
from tkinter import ttk
import random
from time import sleep

def adiciona_pergunta():
    global numero
    numero = random.sample(range(5000),1)[0]
    text_widget4.insert('1.0', '{} é um número é par?\n'.format(str(numero)))
    sleep(4)
    text_widget4.delete('1.0', 'end')

def valida_resposta(bool):
    global numero
    if (bool and (numero % 2) == 0) or (bool == False and (numero % 2) != 0):
        text_widget4.insert('2.0', 'Você está certo!\n')
    else:
        text_widget4.insert('2.0', 'Você está errado!\n')

class Fourth_window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Meu jogo')
        self.resizable(False, False)

class Button_Frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        #BUTTON YES
        yes_button = ttk.Button(self, text = 'Yes', command=lambda: valida_resposta(True))
        yes_button.pack(side = 'left', padx =5, pady = 5, fill = 'x')

        #BUTTON NO
        no_button = ttk.Button(self, text = 'No', command=lambda: valida_resposta(False))
        no_button.pack(side = 'left', padx =5, pady = 5, fill = 'x')

class Quit_Frame(ttk.Frame):

    def __init__(self, container, label_1, function_1):
        super().__init__(container)
        self.label_1 = label_1
        self.function_1 = function_1

        next_button = ttk.Button(self, text = label_1, command = function_1)
        next_button.pack(side = 'top', padx =5, pady = 5, fill = 'x')

        quit_button = ttk.Button(self, text = 'Quit', command = root.destroy)
        quit_button.pack(side = 'top', padx =5, pady = 5, fill = 'x')


root = Fourth_window()
numero = 0 #inicializa a variavel global

text_w4 = ttk.Frame(root)
text_w4.pack(side = 'top', fill = 'both', expand = True)

text_widget4 = tk.Text(text_w4)
text_widget4.pack()

button_w4 = Button_Frame(root)
button_w4.pack(side = 'bottom')


quit_w4 = Quit_Frame(root, 'Start', adiciona_pergunta)
quit_w4.pack(side = 'right')

root.mainloop()