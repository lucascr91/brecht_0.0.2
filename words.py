#!/usr/bin/env python
# coding: utf-8

import pickle
import brecht_de as br
import random

text = br.Text('user_text.txt')

adj = text.adjectives
nouns = text.nouns
verbs = text.verbs

text_words = adj + nouns + verbs

lang = 'DE'

#Abre vocabulário do usuário
pickle_in = open('dictionaries_{0}/brecht_uservocab_{0}.pkl'.format(lang), 'rb')
brecht_uservocab = pickle.load(pickle_in)

#Abre palavras marcadas como importantes pelo usuário
pickle_in = open('dictionaries_{0}/brecht_userimportant_{0}.pkl'.format(lang), 'rb')
brecht_userimportant = pickle.load(pickle_in)

unique_voc = list(set(brecht_uservocab))
unique_txt = list(set(text_words))

intersection = [i for i in unique_txt if i in unique_voc]

rz = len(intersection)/len(text_words)

print("I identify " + str(len(text_words)) + " unique words.")
print('You know ' + str(round(rz*100,2)) + '% of them')
print('How many words do you wanna play now?')
m= int(input())


# Abre dicionário local
pickle_in = open('dictionaries_{0}/brecht_dict_{0}.pkl'.format(lang), 'rb')
brecht_dict = pickle.load(pickle_in)


# Abre lista de não encontrados
pickle_in2 = open('dictionaries_{0}/brecht_lista_not_found_{0}.pkl'.format(lang), 'rb')
brecht_not_found = pickle.load(pickle_in2)

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

if len(selected_words)>len(current_dict):
    print('I could not find the meaning of the following '+ str(len(selected_words)-len(current_dict)) + ' words.')
    for index, word in enumerate([i for i in selected_words if i not in current_dict]):
        print(str(index+1)+')'+ word)

    print('So you will play the game with ' + str(len(current_dict)) )
else:
    print("I foun the meaning of all " + str(m)+ " words. Let's begin!")



answer2 = 'yes'

while answer2 == 'yes':
    brecht_dict2 = current_dict.copy()
    somenoun = random.sample(brecht_dict2.keys(), 1)[0]
    while somenoun !='':
        print('Do you know the meaning of the word "{}"?'.format(somenoun))
        answer1 = input().lower()
        if answer1 == 'no':
            print(brecht_dict2[somenoun])
            somenoun = random.sample(brecht_dict2.keys(), 1)[0]
        elif answer1 == 'vocabulary':
            brecht_uservocab.append(somenoun)
            del brecht_dict2[somenoun]
            if brecht_dict2 !={}:
                somenoun = random.sample(brecht_dict2.keys(), 1)[0]
            else:
                print('Congratulations! You know all words from this text!')
                somenoun =''
        elif answer1 == 'important':
            brecht_userimportant.append(somenoun)
            if brecht_dict2 !={}:
                somenoun = random.sample(brecht_dict2.keys(), 1)[0]
            else:
                print('Congratulations! You know all words from this text!')
                somenoun =''   
            
#             del brecht_dict2[somenoun]
            if brecht_dict2 !={}:
                somenoun = random.sample(brecht_dict2.keys(), 1)[0]
            else:
                print('Congratulations! You know all words from this text!')
                somenoun =''
        else:
            del brecht_dict2[somenoun]
            if brecht_dict2 !={}:
                somenoun = random.sample(brecht_dict2.keys(), 1)[0]
            else:
                print('Congratulations! You know all words from this text!')
                somenoun =''          
    print('Do you want to play this game again?')
    answer2 = input().lower()
else:
    print("Bye!")


# ### Salvando vocabulário (lista)

pickle_out = open('dictionaries_{0}/brecht_uservocab_{0}.pkl'.format(lang), 'wb')
pickle.dump(list(set(brecht_uservocab)), pickle_out)
pickle_out.close()

if lang=='DE':
    print('Now you know ' + str(len(list(set(brecht_uservocab)))) + ' words in German')
elif lang =='FR':
    print('Now you know ' + str(len(list(set(brecht_uservocab)))) + ' words in French')
elif lang == 'EN':
    print('Now you know ' + str(len(list(set(brecht_uservocab)))) + ' words in English')



# ### Salvando lista de não encontrados atualizada

pickle_out = open('dictionaries_{0}/brecht_lista_not_found{0}.pkl'.format(lang), 'wb')
pickle.dump(list(set(brecht_not_found)), pickle_out)
pickle_out.close()

