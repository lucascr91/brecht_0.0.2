#!/usr/bin/env python
# coding: utf-8

# In[2]:


doc = nlp(text)


# In[3]:


verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]

verbs


# In[ ]:


pickle_in = open('lista_voc.pkl', 'rb')
lista_voc = pickle.load(pickle_in)


# In[ ]:


unique_voc = list(set(lista_voc))
unique_txt = list(set(lista_nouns_t))


# In[ ]:


intersection = [i for i in unique_txt if i in unique_voc]


# In[ ]:


rz = len(intersection)/len(lista_nouns_t)


# In[ ]:


print("I identify " + str(len(lista_nouns_t)) + " unique words.")
print('You know ' + str(round(rz*100,2)) + '% of them')
print('How many words do you wanna play now?')
m= int(input())


# ### Abrindo o dicionário

# In[ ]:


pickle_in = open('dict.pickle', 'rb')
my_dct = pickle.load(pickle_in)


# ### Abrindo lista de não encontrados

# In[ ]:


pickle_in2 = open('lista_not_found.pkl', 'rb')
lista_not_found = pickle.load(pickle_in2)


# ### Salvando o dicionário atualizado

# In[7]:


pickle_out = open('brecht_dict.pkl', 'wb')
pickle.dump(brecht_dict, pickle_out)
pickle_out.close()


# ### Selecionando palavras encontradas

# In[ ]:


current_dict = {k: my_dct[k] for k in word_vector_final if k in my_dct}


# In[ ]:


print('I could not find the meaning of '+ str(len(word_vector)-len(current_dict)) + ' words.' + '\n' +
'So you will play the game with ' + str(len(current_dict)) )


# In[ ]:


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
            lista_voc.append(somenoun)
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

# In[ ]:


pickle_out = open('lista_voc.pkl', 'wb')
pickle.dump(list(set(lista_voc)), pickle_out)
pickle_out.close()


# In[ ]:


print('Now you know ' + str(len(list(set(lista_voc)))) + ' words in German')


# ### Criando um vetor com o número de palavras solicitadas pelo usuário a partir do número total de palavras do texto

# In[ ]:


s = random.sample(list(range(0,len(lista_nouns_t))),m)


# In[ ]:


word_vector = itemgetter(*s)(lista_nouns_t)


# ### Selecionando palavras que não tem no dicionário

# In[ ]:


lista_nodict = [i for i in word_vector if i not in list(my_dct.keys())]


# In[ ]:


print('I need to download the meaning of ' + str(len(lista_nodict)) + ' words')


# In[ ]:


word_vector_final = list(set(word_vector)-set(lista_not_found)-set(lista_voc))


# ### Salvando lista de não encontrados atualizada

# In[1]:


pickle_out = open('brecht_lista_not_found.pkl', 'wb')
pickle.dump(list(set(brecht_not_found)), pickle_out)
pickle_out.close()

