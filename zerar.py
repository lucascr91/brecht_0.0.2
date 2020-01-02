#zerar dicionários locais

import pickle

#************************************Deutsch dictionaries*************************************

# Lista de palavras não encontradas
brecht_not_found_DE = []

#Dicionário local
brecht_dict_DE = {}

#Vocabulário do usuário
user_vocab_DE = {}

#not found
pickle_out = open('dictionaries_DE/brecht_lista_not_found_DE.pkl', 'wb')
pickle.dump(list(set(brecht_not_found_DE)), pickle_out)
pickle_out.close()

#dicionario
pickle_out = open('dictionaries_DE/brecht_dict_DE.pkl', 'wb')
pickle.dump(brecht_dict_DE, pickle_out)
pickle_out.close()

#user_vocab
pickle_out = open('dictionaries_DE/brecht_uservocab_DE.pkl', 'wb')
pickle.dump(brecht_dict_DE, pickle_out)
pickle_out.close()

#************************************French dictionaries*************************************

# Lista de palavras não encontradas
brecht_not_found_FR = []

#Dicionário local
brecht_dict_FR = {}

#Vocabulário do usuário
user_vocab_FR = {}

#not found
pickle_out = open('dictionaries_FR/brecht_lista_not_found_FR.pkl', 'wb')
pickle.dump(list(set(brecht_not_found_FR)), pickle_out)
pickle_out.close()

#dicionario
pickle_out = open('dictionaries_FR/brecht_dict_FR.pkl', 'wb')
pickle.dump(brecht_dict_FR, pickle_out)
pickle_out.close()

#user_vocab
pickle_out = open('dictionaries_FR/brecht_uservocab_FR.pkl', 'wb')
pickle.dump(brecht_dict_FR, pickle_out)
pickle_out.close()

#************************************English dictionaries*************************************

# Lista de palavras não encontradas
brecht_not_found_ENG = []

#Dicionário local
brecht_dict_ENG = {}

#Vocabulário do usuário
user_vocab_ENG = {}

#not found
pickle_out = open('dictionaries_ENG/brecht_lista_not_found_ENG.pkl', 'wb')
pickle.dump(list(set(brecht_not_found_ENG)), pickle_out)
pickle_out.close()

#dicionario
pickle_out = open('dictionaries_ENG/brecht_dict_ENG.pkl', 'wb')
pickle.dump(brecht_dict_ENG, pickle_out)
pickle_out.close()

#user_vocab
pickle_out = open('dictionaries_ENG/brecht_uservocab_ENG.pkl', 'wb')
pickle.dump(brecht_dict_ENG, pickle_out)
pickle_out.close()

