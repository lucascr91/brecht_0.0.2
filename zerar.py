#zerar dicionários locais

import pickle

languages = ['DE', 'FR', 'EN']

for lang in languages:

    #Dicionário local
    brecht_dict = {}

    # Lista de palavras não encontradas
    brecht_not_found = []

    #Vocabulário do usuário
    user_vocab = []

    #Palavras marcadas como importantes pelo usuário
    user_important = []


    #dicionario
    pickle_out = open('dictionaries_{0}/brecht_dict_{0}.pkl'.format(lang), 'wb')
    pickle.dump(brecht_dict, pickle_out)
    pickle_out.close()

        #not found
    pickle_out = open('dictionaries_{0}/brecht_lista_not_found_{0}.pkl'.format(lang), 'wb')
    pickle.dump(list(set(brecht_not_found)), pickle_out)
    pickle_out.close()

    #user_vocab
    pickle_out = open('dictionaries_{0}/brecht_uservocab_{0}.pkl'.format(lang), 'wb')
    pickle.dump(user_vocab, pickle_out)
    pickle_out.close()

    #user_important
    pickle_out = open('dictionaries_{0}/brecht_userimportant_{0}.pkl'.format(lang), 'wb')
    pickle.dump(user_important, pickle_out)
    pickle_out.close()

