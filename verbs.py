
# coding: utf-8

# In[8]:


from pattern.de import parse, split
from pattern.de import gender, MALE, FEMALE, NEUTRAL, Text, Sentence, WORD, POS, CHUNK, PNP, REL, LEMMA
from pattern.de import parsetree
from pattern.de import conjugate
from pattern.de import INFINITIVE, PRESENT, SG, SUBJUNCTIVE
import random
from operator import itemgetter
import pickle
from gensim.utils import deaccent


# In[9]:


from selenium import webdriver


# In[10]:


print('Please, enter the txt file')
arquivo = input()

f =open(arquivo, 'r', encoding = 'utf-8')
g = f.read()
f.close()


# In[11]:


txt = parsetree(g, tags=True, chunk = False)


# In[12]:


sents = txt.sentences


# In[13]:


lista_elements = list(set([conjugate(str(sents[i].verbs[0]), INFINITIVE) for i in range(0,len(sents)) 
                         if sents[i].verbs != []]))
lista_verbos_t = [i for i in lista_elements if i.isalpha()]


# In[14]:


print("I identify " + str(len(lista_verbos_t)) + " verbs")
print('How many words do you wanna play now?')
m= int(input())


# ### Abrindo o dicionário

# In[15]:


pickle_in = open('dict.pickle', 'rb')
my_dct = pickle.load(pickle_in)


# ### Abrindo lista de não encontrados

# In[16]:


pickle_in2 = open('list.pkl', 'rb')
lista_not_found = pickle.load(pickle_in2)


# ### Criando um vetor com o número de palavras solicitadas pelo usuário a partir do número total de palavras do texto

# In[17]:


s = random.sample(list(range(0,len(lista_verbos_t))),m)


# In[18]:


word_vector = itemgetter(*s)(lista_verbos_t)


# ### Selecionando palavras que não tem no dicionário

# In[19]:


lista_nodict = [i for i in word_vector if i not in list(my_dct.keys())]


# In[20]:


print('I need to download the meaning of ' + str(len(lista_nodict)) + ' verbs')


# In[21]:


word_vector_final = [i for i in word_vector if i not in lista_not_found]


# ### Fazendo upgrade no dicionário com as palavras que faltam

# In[22]:


for n in word_vector_final:
    if n not in my_dct.keys():
        d = deaccent(n)
        driver = webdriver.Firefox()
        driver.get('https://www.collinsdictionary.com/dictionary/german-english/{}'.format(d))
        word = driver.find_elements_by_xpath('//div[@class="sense"]')
        if word!=[]:
            my_dct[n] = word[0].text
        else:
            lista_not_found.append(d)
        driver.close()


# ### Salvando lista de não encontrados atualizada

# In[23]:


pickle_out = open('list.pkl', 'wb')
pickle.dump(lista_not_found, pickle_out)
pickle_out.close()


# ### Salvando o dicionário atualizado

# In[24]:


pickle_out = open('dict.pickle', 'wb')
pickle.dump(my_dct, pickle_out)
pickle_out.close()


# ### Selecionando palavras encontradas

# In[25]:


current_dict = {k: my_dct[k] for k in word_vector if k in my_dct}


# In[26]:


print('I could not find the meaning of '+ str(len(word_vector)-len(current_dict)) + ' words.' + '\n' +
'So you will play the game with ' + str(len(current_dict)) )


# In[27]:


answer2 = 'Ja'

while answer2 == 'Ja':
    my_dct2 = current_dict.copy()
    someverb = random.sample(my_dct2.keys(), 1)[0]
    while someverb !='':
        print('Do you know the meaning of the noun "{}"?'.format(someverb))
        answer1 = input()
        if answer1 == 'Nein':
            print(my_dct2[someverb])
            someverb = random.sample(my_dct2.keys(), 1)[0]
        else:
            del my_dct2[someverb]
            if my_dct2 !={}:
                someverb = random.sample(my_dct2.keys(), 1)[0]
            else:
                print('Congratulations! You know all nouns from this text!')
                someverb =''
            
    print('Do you want to play this game again?')
    answer2 = input()
else:
    print("Bye!")

