
# coding: utf-8

# In[1]:


from pattern.de import parse, split
from pattern.de import gender, MALE, FEMALE, NEUTRAL, Text, Sentence, WORD, POS, CHUNK, PNP, REL, LEMMA
from pattern.de import parsetree
from pattern.de import conjugate
from pattern.de import INFINITIVE, PRESENT, SG, SUBJUNCTIVE
import random
from operator import itemgetter
import pickle
from gensim.utils import deaccent
import colorama
from colorama import Fore
from colorama import Style


# In[2]:


from selenium import webdriver


# In[3]:


print('Please, enter the txt file')
arquivo = input()

f =open(arquivo, 'r', encoding = 'utf-8')
g = f.read()
f.close()


# In[4]:


txt = parsetree(g, tags=True, chunk = False)


# In[5]:


sents = txt.sentences


# In[6]:


lista_elements = list(set([sents[i].words[j].string 
                           for i in range(0,len(sents)) 
                           for j in range(0,len(sents[i].words))]))
lista_nouns_t = [deaccent(i.lower()) for i in lista_elements if i.isalpha()]


# ### Abrindo vocabulário

# In[7]:


pickle_in = open('lista_voc.pkl', 'rb')
lista_voc = pickle.load(pickle_in)


# In[15]:


unique_voc = list(set(lista_voc))
unique_txt = list(set(lista_nouns_t))


# In[16]:


intersection = [i for i in unique_txt if i in unique_voc]


# In[18]:


rz = len(intersection)/len(lista_nouns_t)


# In[19]:


print("I identify " + str(len(lista_nouns_t)) + " unique words.")
print('You know ' + str(round(rz*100,2)) + '% of them')
print('How many words do you wanna play now?')
m= int(input())


# ### Abrindo o dicionário

# In[88]:


pickle_in = open('dict.pickle', 'rb')
my_dct = pickle.load(pickle_in)


# ### Abrindo lista de não encontrados

# In[89]:


pickle_in2 = open('lista_not_found.pkl', 'rb')
lista_not_found = pickle.load(pickle_in2)


# ### Criando um vetor com o número de palavras solicitadas pelo usuário a partir do número total de palavras do texto

# In[90]:


s = random.sample(list(range(0,len(lista_nouns_t))),m)


# In[91]:


word_vector = itemgetter(*s)(lista_nouns_t)


# ### Selecionando palavras que não tem no dicionário

# In[92]:


lista_nodict = [i for i in word_vector if i not in list(my_dct.keys())]


# In[93]:


print('I need to download the meaning of ' + str(len(lista_nodict)) + ' words')


# In[94]:


word_vector_final = list(set(word_vector)-set(lista_not_found)-set(lista_voc))


# ### Fazendo upgrade no dicionário com as palavras que faltam

# In[95]:


if list(set(word_vector_final)-set(my_dct.keys()))!=[]:
    for n in list(set(word_vector_final)-set(my_dct.keys())):
            driver = webdriver.Firefox()
            driver.get('https://www.collinsdictionary.com/dictionary/german-english/{}'.format(n))
            word = driver.find_elements_by_xpath('//div[@class="sense"]')
            if word!=[]:
                my_dct[n] = word[0].text
            else:
                lista_not_found.append(n)
            driver.close()


# ### Salvando lista de não encontrados atualizada

# In[96]:


pickle_out = open('lista_not_found.pkl', 'wb')
pickle.dump(list(set(lista_not_found)), pickle_out)
pickle_out.close()


# ### Salvando o dicionário atualizado

# In[97]:


pickle_out = open('dict.pickle', 'wb')
pickle.dump(my_dct, pickle_out)
pickle_out.close()


# ### Selecionando palavras encontradas

# In[98]:


current_dict = {k: my_dct[k] for k in word_vector_final if k in my_dct}


# In[99]:


print('I could not find the meaning of '+ str(len(word_vector)-len(current_dict)) + ' words.' + '\n' +
'So you will play the game with ' + str(len(current_dict)) )


# In[100]:


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

# In[101]:


pickle_out = open('lista_voc.pkl', 'wb')
pickle.dump(list(set(lista_voc)), pickle_out)
pickle_out.close()


# In[102]:


print('Now you know ' + str(len(list(set(lista_voc)))) + ' words in German')

