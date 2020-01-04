import tkinter as tk
from tkinter import ttk
import brecht_de as br
import tkinter.font as font
import pickle
import random
from time import sleep

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

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def callback(event):
    global answer1
    #print(event)
    answer1 = event.widget['text']



def stats():
    global text_words

    text = br.Text('user_text.txt')

    adj = [token.lemma_ for token in text.doc if token.pos_ == "ADJ"]
    nouns = [token.lemma_ for token in text.doc if token.pos_ == "NOUN"]
    verbs = [token.lemma_ for token in text.doc if token.pos_ == "VERB"]

    text_words = adj + nouns + verbs


    unique_voc = list(set(brecht_uservocab))
    unique_txt = list(set(text_words))

    intersection = [i for i in unique_txt if i in unique_voc]

    rz = len(intersection)/len(text_words)

    return text_widget4.insert('1.0', "I identify " + str(len(text_words)) + " unique words. \n"+
    'You know ' + str(round(rz*100,2)) + '% of them \n')

def words_founded():
    global selected_words
    global current_dict

    m=5
    selected_words = random.sample(text_words, m)

    # Adiciona palavras ao dicionário local
    for word in selected_words:
        brecht_dict[word] = br.Words(word).meaning

    # Salvando o dicionário atualizado
    pickle_out = open('dictionaries_{0}/brecht_dict_{0}'.format(lang), 'wb')
    pickle.dump(brecht_dict, pickle_out)
    pickle_out.close()


    current_dict = {k: brecht_dict[k] for k in text_words if k in brecht_dict}

    current_dict = {k:v for k, v in current_dict.items() if v!=None}
    
    gen = enumerate([i for i in selected_words if i not in current_dict])

    if len(selected_words)>len(current_dict):
        return text_widget4.insert('4.0', 'I could not find the meaning of the following '+ str(len(selected_words)-len(current_dict)) + ' words.')
        for index, word in gen:
            text_widget4.insert('{}.0'.format(str(4+index)), str(index+1)+')'+ word)

        text_widget4.insert('{}.0'.format(str(len(gen))),'So you will play the game with ' + str(len(current_dict)) )
    else:
        return text_widget4.insert('4.0',"I found the meaning of all " + str(m)+ " words. Let's begin!")

def start_game():
    sleep(3)
    text_widget4.delete('1.0', 'end')
    while True:
        brecht_dict2 = current_dict.copy()
        somenoun = random.sample(brecht_dict2.keys(), 1)[0]
        while somenoun !='':
            text_widget4.insert('1.0','Do you know the meaning of the word "{}"?'.format(somenoun))
            if answer1 == 'No':
                text_widget4.insert('2.0',brecht_dict2[somenoun])
                somenoun = random.sample(brecht_dict2.keys(), 1)[0]
            elif answer1 =='Vocabulary':
                brecht_uservocab.append(somenoun)
                del brecht_dict2[somenoun]
                if brecht_dict2 !={}:
                    somenoun = random.sample(brecht_dict2.keys(), 1)[0]
                else:
                    text_widget4.delete('1.0', 'end')
                    text_widget4.tag_configure("center", justify='center')
                    text_widget4.insert('1.0','Congratulations! You know all words from this text!')
                    somenoun =''
            elif answer1=='Important':
                brecht_userimportant.append(somenoun)
                if brecht_dict2 !={}:
                    somenoun = random.sample(brecht_dict2.keys(), 1)[0]
                else:
                    text_widget4.delete('1.0', 'end')
                    text_widget4.tag_configure("center", justify='center')
                    text_widget4.insert('1.0','Congratulations! You know all words from this text!')
                    somenoun =''                
                if brecht_dict2 !={}:
                    somenoun = random.sample(brecht_dict2.keys(), 1)[0]
                else:
                    text_widget4.delete('1.0', 'end')
                    text_widget4.tag_configure("center", justify='center')
                    text_widget4.insert('1.0','Congratulations! You know all words from this text!')
                    somenoun =''
            else:
                del brecht_dict2[somenoun]
                if brecht_dict2 !={}:
                    somenoun = random.sample(brecht_dict2.keys(), 1)[0]
                else:
                    text_widget4.delete('1.0', 'end')
                    text_widget4.tag_configure("center", justify='center')
                    text_widget4.insert('1.0','Congratulations! You know all words from this text!')
                    somenoun =''   
        text_widget4.delete('1.0', 'end')
        text_widget4.tag_configure("center", justify='center')
        text_widget4.insert('1.0','Do you want to play this game again?')
        if answer2=='No':
            print("Bye!")
            break
        else:
            continue

class Fourth_window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Brecht 0.0.2')
        self.resizable(False, False)

class Button_Frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        #BUTTON YES
        button1 = ttk.Button(self, text = 'Yes')
        button1.bind('<Button-1>', callback)
        button1.pack(side = 'left', padx =5, pady = 5, fill = 'x')


        #BUTTON NO
        button2 = ttk.Button(self, text = 'No')
        button2.bind('<Button-2>', callback)
        button2.pack(side = 'left', padx =5, pady = 5, fill = 'x')


        #BUTTON VOCABULARY
        button3 = ttk.Button(self, text = 'Vocabulary')
        button3.bind('<Button-3>', callback)
        button3.pack(side = 'left', padx =5, pady = 5, fill = 'x')


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
# for n in ['1','2', '3']:
#     button_w4.bind('<Button-{}>'.format(n), function_so)

quit_w4 = Quit_Frame(root, 'Start', combine_funcs(stats, words_founded, start_game))
quit_w4.pack(side = 'right')

#WIDGETS
text_widget4 = tk.Text(text_w4)
text_widget4.pack()



text = br.Text('user_text.txt')




root.mainloop()

