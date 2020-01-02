#!/usr/bin/env python
# coding: utf-8



doc = nlp(text)

text_words = [token.lemma_ for token in doc if token.pos_ == "VERB"]


pickle_in = open('dictionaries/brecht_uservocab.pkl', 'rb')
brecht_uservocab = pickle.load(pickle_in)

unique_voc = list(set(brecht_uservocab))
unique_txt = list(set(text_words))

intersection = [i for i in unique_txt if i in unique_voc]

rz = len(intersection)/len(text_words)

print("I identify " + str(len(text_words)) + " unique words.")
print('You know ' + str(round(rz*100,2)) + '% of them')
print('How many words do you wanna play now?')
m= int(input())


pickle_in = open('dict.pickle', 'rb')
my_dct = pickle.load(pickle_in)


# ### Abrindo lista de não encontrados
pickle_in2 = open('lista_not_found.pkl', 'rb')
lista_not_found = pickle.load(pickle_in2)


# ### Salvando o dicionário atualizado
pickle_out = open('brecht_dict.pkl', 'wb')
pickle.dump(brecht_dict, pickle_out)
pickle_out.close()


current_dict = {k: my_dct[k] for k in word_vector_final if k in my_dct}


print('I could not find the meaning of '+ str(len(word_vector)-len(current_dict)) + ' words.' + '\n' +
'So you will play the game with ' + str(len(current_dict)) )



answer2 = 'Ja'

while answer2 == 'Ja':
    my_dct2 = current_dict.copy()
    somenoun = random.sample(my_dct2.keys(), 1)[0]
    while somenoun !='':
        print('Do you know the meaning of the word "{}"?'.format(somenoun))
        answer1 = input()
        if answer1 == 'Nein':
            print(Fore.YELLOW + my_dct2[somenoun])
            print(Style.RESET_ALL)
            somenoun = random.sample(my_dct2.keys(), 1)[0]
        elif answer1 == 'vocabulary':
            dictionaries/brecht_uservocab.append(somenoun)
            del my_dct2[somenoun]
            if my_dct2 !={}:
                somenoun = random.sample(my_dct2.keys(), 1)[0]
            else:
                print('Congratulations! You know all words from this text!')
                somenoun =''
        elif answer1 == 'wichtig':
            f = open('wichtig.txt', 'r')
            h = f.read()
            f.close()
            l = h + ' '+ str(somenoun)
            f = open('wichtig.txt', 'w')
            f.write(l)
            f.close()         
            
#             del my_dct2[somenoun]
            if my_dct2 !={}:
                somenoun = random.sample(my_dct2.keys(), 1)[0]
            else:
                print('Congratulations! You know all words from this text!')
                somenoun =''
        else:
            del my_dct2[somenoun]
            if my_dct2 !={}:
                somenoun = random.sample(my_dct2.keys(), 1)[0]
            else:
                print('Congratulations! You know all words from this text!')
                somenoun =''
            
    print('Do you want to play this game again?')
    answer2 = input()
else:
    print("Bye!")


# ### Salvando vocabulário (lista)

pickle_out = open('dictionaries/brecht_uservocab.pkl', 'wb')
pickle.dump(list(set(dictionaries/brecht_uservocab)), pickle_out)
pickle_out.close()

print('Now you know ' + str(len(list(set(dictionaries/brecht_uservocab)))) + ' words in German')

s = random.sample(list(range(0,len(text_words_t))),m)

word_vector = itemgetter(*s)(text_words_t)


# ### Selecionando palavras que não tem no dicionário

lista_nodict = [i for i in word_vector if i not in list(my_dct.keys())]


print('I need to download the meaning of ' + str(len(lista_nodict)) + ' words')

word_vector_final = list(set(word_vector)-set(lista_not_found)-set(dictionaries/brecht_uservocab))


# ### Salvando lista de não encontrados atualizada

pickle_out = open('brecht_lista_not_found.pkl', 'wb')
pickle.dump(list(set(brecht_not_found)), pickle_out)
pickle_out.close()

