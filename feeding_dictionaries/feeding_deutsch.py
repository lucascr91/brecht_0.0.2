#!/usr/bin/env python
# coding: utf-8

import pickle
import spacy
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('/home/popper/projects/brecht_0.0.2')
import brecht_de as br

text = br.Text('/home/popper/projects/brecht_0.0.2/feeding_dictionaries/Mann_Buddenbrooks.txt')

adj = [token.lemma_ for token in text.doc if token.pos_ == "ADJ"]
nouns = [token.lemma_ for token in text.doc if token.pos_ == "NOUN"]
verbs = [token.lemma_ for token in text.doc if token.pos_ == "VERB"]

text_words = list(set(adj + nouns + verbs))

lang = 'DE'


# Abre dicionário local
pickle_in = open('/home/popper/projects/brecht_0.0.2/dictionaries_{0}/brecht_dict_{0}.pkl'.format(lang), 'rb')
brecht_dict = pickle.load(pickle_in)


# Abre lista de não encontrados
pickle_in2 = open('/home/popper/projects/brecht_0.0.2/dictionaries_{0}/brecht_lista_not_found_{0}.pkl'.format(lang), 'rb')
lista_not_found = pickle.load(pickle_in2)

# Adiciona palavras ao dicionário local
for word in text_words:
    print('The local German dictionary has now ' + str(len(brecht_dict.keys())) + 'words')
    brecht_dict[word] = br.Words(word).meaning
    pickle_out = open('/home/popper/projects/brecht_0.0.2/dictionaries_{0}/brecht_dict_{0}.pkl'.format(lang), 'wb')
    pickle.dump(brecht_dict, pickle_out)
    pickle_out.close()