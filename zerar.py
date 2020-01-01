#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#zerar dicionários locais

import pickle

brecht_not_found = []
brecht_dict = {}

#not found
pickle_out = open('brecht_lista_not_found.pkl', 'wb')
pickle.dump(list(set(brecht_not_found)), pickle_out)
pickle_out.close()

#dicionario
pickle_out = open('brecht_dict.pkl', 'wb')
pickle.dump(brecht_dict, pickle_out)
pickle_out.close()

