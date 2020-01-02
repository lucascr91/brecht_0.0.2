# Brecht 0.0.2


![alt text](https://github.com/lucascr91/brecht_0.0.2/blob/master/brecht_drawing.jpg?raw=true)
#### A game to learn how to read in German


Brecht is a simple game that I have been developing to help me to learn how to read in German. Despite having a complex grammar, I believe the true challenge for learning German, on the perspective of a Latin language native, is the Wortzschtaz (i.e., the vocabulary). That's why this game has an exclusive focus on building vocabulary. More specifically, its purpose is to present you all unknown words of a previously selected text that you want to read, then let you play with them until you have enough knowledge of the meaning of most new words. After playing the game, you are supposed to be ready to actually read the text.
 
[Here](https://github.com/lucascr91/brecht_0.0.1) you can find an early version of this game. I developed this version when I was in my very beginner as a Python programmer, I am still a beginner, but I guess I have learned a few tricks since that first attempt. The version 0.0.1 is just an interactive game which runs in terminal. It selects all words, and go on asking the player if she/he already knows that word. On negative answers to this question, the program presents the translation of the word that it gets from the Deutsch version of the online [collins dictionary](https://www.collinsdictionary.com/dictionary/english-german). After the game, the words whose meaning the player now has marked as known words are saved and will not show in the next time she/he plays it.

Besides this core model, the first version also has some additional features. For example, the player could play only with words that her/him has marked as "important" in all her/his previous sections.

While the first version addresses some needs that I think are required in a tool like that, it had also several limitations. That's why I have created a list of improvements that I would like to add to this version. To check this list, read the file IMPROVEMENTS.

I hope that other language love programmers join me in this project. I believe that its basic model can easily be expanded to cover other languages and make the learning of a new language even funnier.


#### How to run Brecht 0.0.2

If you use a Linux distribution and already have Python installed in your PC, just download this repository, open the terminal, go to the directory that you have just downloaded, and run the following command:

```
bash brecht_app.sh
```
Similarly, if you are on Windows, open the conda prompt inside the downloaded directory and run:

```
python brecht_full.py
```


To see the list of python modules you need to run Brecht, see the file REQUIREMENTS



#### How to use Brecht 0.0.2

It's useful to know how Brecht is organized in order to be able to use it. Brecht is divided into four windows. The first window asks the user to chose which language she/he wants to practice. The second demands that the user provide the text she/he wants to read later. In the text upload window, the user can choose one of the following options: 1) open a file already saved within the Brecht's directory, 2) Upload a file, and 3) Paste the text into Brecht. Brecht requires that the file used in options 1 and 2 has a .txt extension.

The third window gives the user several options regarding specific information about the upload text. For instance, in this information window, the user can list the text's words by grammatical class. Finally, the fourth window, which can be accessed by clicking in the button PLAY from the third window, presents the actual game. As stated above, this game consists of showing you all unknown words of the previously selected text, then let you play with them until you have enough knowledge of the meaning of most new words.


#### Further information

Besides the files README, IMPROVEMENTS, and REQUIREMENTS, this repository also contains a TASKS files that lists the tasks to be done in the current stage of the project development. If you are considering to be a contributor of Brecht 0.0.2, please take a look at the remaining tasks.

This game relies heavily on the python module [Spacy](https://spacy.io/)
