#!/usr/bin/env python
# coding: utf-8

## This file contains the classes used in the game
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle
import spacy
import tkinter as tk
from tkinter import ttk

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH


lang = 'DE'

nlp = spacy.load(lang.lower())

# ## Opening local dictionary
pickle_in = open('dictionaries_{0}/brecht_dict_{0}.pkl'.format(lang), 'rb')
brecht_dict = pickle.load(pickle_in)


# ## Opening not found list
pickle_in2 = open('dictionaries_{0}/brecht_lista_not_found_{0}.pkl'.format(lang), 'rb')
lista_not_found = pickle.load(pickle_in2)

class Text():
    def __init__(self, file):
        self.file = file

    @property
    def actual_text(self):
        f = open(self.file, 'r', encoding='utf-8')
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

    @property
    def adjectives(self):
        adjectives = [token.lemma_ for token in self.doc if token.pos_ == "ADJ"]
        return adjectives


class Words():
    def __init__(self, value, first_meaning=True):
        self.value = value
        self.first_meaning = first_meaning
    # attribute meaning
    @property
    def meaning(self):
        # is the word in my local dictionary?
        if self.value in brecht_dict.keys():
            return brecht_dict[self.value]
        # so, get it it online
        else:
            driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options
                         )  
            driver.get('https://de.thefreedictionary.com/{}'.format(self.value))
            word = driver.find_elements_by_xpath('//div[@id="Definition"]')
            if word != []:
                brecht_dict[self.value] = word[0].text
                if self.first_meaning:
                    return word[0].text[:word[0].text.find('2.')]
                    driver.close()
                else:
                    return word[0].text
                    driver.close()
            else:
                lista_not_found.append(self.value)
                # return print('I could not find the word '+self.value)
                driver.close()
        # method to print value

        def __str__(self):
            return self.value

if __name__ == '__main__':  # para testar no terminal
    word1 = Words('Beispiel')
    print(word1)
    print(word1)