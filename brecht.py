#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pickle
import spacy
from selenium import webdri
nlp = spacy.load('de')


# ## Opening local dictionary

# In[2]:


pickle_in = open('brecht_dict.pkl', 'rb')
brecht_dict = pickle.load(pickle_in)


# ## Opening not found list

# In[4]:


pickle_in2 = open('brecht_lista_not_found.pkl', 'rb')
lista_not_found = pickle.load(pickle_in2)


# In[63]:


class Text():
    def __init__(self, file):
        self.file = file
    @property
    def actual_text(self):
        f =open(self.file, 'r', encoding = 'utf-8')
        text = f.read()
        f.close()
        
        return text
    
    @property
    def doc(self):
        parsed_text = nlp(self.actual_text)
        
        return parsed_text
        
    @property
    def verbs(self):
        verbs = [token.lemma_ for token in self.doc if token.pos_ == "VERB"]
        
        return verbs
    
    @property
    def nouns(self):
        nouns = [token.lemma_ for token in self.doc if token.pos_ == "NOUN"]
        
        return nouns


# In[42]:


class Words():
    def __init__(self, value, g_class, first_meaning = True):
        self.value = value
        self.g_class = g_class
        self.first_meaning = first_meaning
    #attribute meaning
    meaning = ''
    #is the word in my local dictionary?
    @property
    def meaning(self):
        if self.value in brecht_dict.keys():
            return brecht_dict[self.value]
        #so, get it it online
        else:
            driver = webdriver.Firefox()
            driver.get('https://de.thefreedictionary.com/{}'.format(self.value))
            word = driver.find_elements_by_xpath('//div[@id="Definition"]')
            if word!=[]:
                brecht_dict[self.value] = word[0].text
                if self.first_meaning:
                    return word[0].text[:word[0].text.find('2.')]
                else:
                    return word[0].text
            else:
                lista_not_found.append(self.value)
                return print('I could not find this word')
            driver.close()
        #method to print value
        def __str__(self):
            return self.value


# In[ ]:


if __name__ == '__main__': # para testar no terminal
    word1 = Words('Beispiel', g_class = 'noun')
    print(word1)
    print(word1.g_class)

