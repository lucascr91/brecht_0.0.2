# Brecht 0.0.2


![alt text](https://github.com/lucascr91/brecht_0.0.2/blob/master/brecht_drawing.jpg?raw=true)
#### A game to learn how to read in German


Brecht is a simple game that I have been developing to help me to learn how to
 read in German. Despite having a complex grammar, I believe the true challenge for learning German, on the perspective of a Latin language native, is the Wortzschtaz (i.e., the vocabulary). That's why this game has an exclusive focus on building vocabulary. More specifically, its purpose is to present you all unknown words of a previously selected text that you want to read, then let you play with them until you have enough knowledge of the meaning of most new words. After playing the game, you are supposed to be ready to actually read the text.
 
 [Here](https://github.com/lucascr91/brecht_0.0.1) you can find an early version of this game. I developed this version when I was in my very
   beginner as a Python programmer, I am still a beginner, but I guess I have learned a few tricks since that first attempt. The version 0.0.1 is just
     an interactive game which runs in terminal. It selects all words, and go on asking the player if she/he already knows that word. On negative
       answers to this question, the program presents the translation of the word that it gets from the Deutsch version of the online [collins dictionary](https://www.collinsdictionary.com/dictionary/english-german). After the game, the words whose meaning the player now has marked as known words are saved and will not show in the next time she/he plays it.

Besides this core model, the first version also has some additional features. For example, the player could play only with words that her/him has marked as "important" in all her/his previous sections.

Besides this README file, this repository also contains a TASKS files whose main intent is list all the tasks that must be achieve in order to finish the project. If you are considering to be a contributor of Brecht 0.0.2, please take a look in the remaining tasks.

This game relies heavily on the python module [Spacy](https://spacy.io/)
