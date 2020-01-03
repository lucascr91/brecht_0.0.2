#!/usr/bin/env python
# coding: utf-8

import pickle
import spacy
import brecht_de as br

text = br.Text('user_text.txt')

text_words = [token.lemma_ for token in text.doc if token.pos_ == "VERB"]

lang = 'DE'

pickle_in = open('dictionaries_{0}/brecht_uservocab_{0}.pkl'.format(lang), 'rb')
brecht_uservocab = pickle.load(pickle_in)

unique_voc = list(set(brecht_uservocab))
unique_txt = list(set(text_words))

intersection = [i for i in unique_txt if i in unique_voc]

rz = len(intersection)/len(text_words)

print("I identify " + str(len(text_words)) + " unique words.")
print('You know ' + str(round(rz*100,2)) + '% of them')
print('How many words do you wanna play now?')
m= int(input())


# Abre dicionário local
pickle_in = open('dictionaries_{0}/brecht_dict_{0}'.format(lang), 'rb')
brecht_dict = pickle.load(pickle_in)


# Abre lista de não encontrados
pickle_in2 = open('dictionaries_{0}/lista_not_found_{0}.pkl'.format(lang), 'rb')
lista_not_found = pickle.load(pickle_in2)

# Adiciona palavras ao dicionário local
for word in text_words:
    brecht_dict[word] = br.Words(word).meaning

# Salvando o dicionário atualizado
pickle_out = open('dictionaries_{0}/brecht_dict_{0}'.format(lang), 'wb')
pickle.dump(brecht_dict, pickle_out)
pickle_out.close()


current_dict = {k: brecht_dict[k] for k in text_words if k in brecht_dict}


print('I could not find the meaning of '+ str(len(text_words)-len(current_dict)) + ' words.' + '\n' +
'So you will play the game with ' + str(len(current_dict)) )



answer2 = 'Ja'

while answer2 == 'Ja':
    brecht_dict2 = current_dict.copy()
    somenoun = random.sample(brecht_dict2.keys(), 1)[0]
    while somenoun !='':
        print('Do you know the meaning of the word "{}"?'.format(somenoun))
        answer1 = input()
        if answer1 == 'Nein':
            print(Fore.YELLOW + brecht_dict2[somenoun])
            print(Style.RESET_ALL)
            somenoun = random.sample(brecht_dict2.keys(), 1)[0]
        elif answer1 == 'vocabulary':
            dictionaries/brecht_uservocab.append(somenoun)
            del brecht_dict2[somenoun]
            if brecht_dict2 !={}:
                somenoun = random.sample(brecht_dict2.keys(), 1)[0]
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
    answer2 = input()
else:
    print("Bye!")


# ### Salvando vocabulário (lista)

pickle_out = open('dictionaries/brecht_uservocab.pkl', 'wb')
pickle.dump(list(set(dictionaries/brecht_uservocab)), pickle_out)
pickle_out.close()

if lang=='DE':
    print('Now you know ' + str(len(list(set(brecht_uservocab)))) + ' words in German')
elif lang =='FR':
    print('Now you know ' + str(len(list(set(brecht_uservocab)))) + ' words in French')
elif lang == 'EN':
    print('Now you know ' + str(len(list(set(brecht_uservocab)))) + ' words in English')



# ### Salvando lista de não encontrados atualizada

pickle_out = open('brecht_lista_not_found.pkl', 'wb')
pickle.dump(list(set(brecht_not_found)), pickle_out)
pickle_out.close()

