#zerar dicionários locais

import pickle

# Lista de palavras não encontradas
brecht_not_found = []

#Dicionário local
brecht_dict = {}

#Vocabulário do usuário
user_vocab = {}

#not found
pickle_out = open('dictionaries/brecht_lista_not_found.pkl', 'wb')
pickle.dump(list(set(brecht_not_found)), pickle_out)
pickle_out.close()

#dicionario
pickle_out = open('dictionaries/brecht_dict.pkl', 'wb')
pickle.dump(brecht_dict, pickle_out)
pickle_out.close()

#user_vocab
pickle_out = open('dictionaries/brecht_uservocab.pkl', 'wb')
pickle.dump(brecht_dict, pickle_out)
pickle_out.close()

