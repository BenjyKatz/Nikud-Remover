# Nikud-Remover
 Author: Benjamin Katz 
 Phone: +12017448809(whatsapp)
 Email: benjykatz12@gmail.com
 Written Summer 2022

 The NR.py program takes a document with nikud and outputs a document with the nikud removed. The outputed ducument adds appropreiate vavim and yudim to change the chaser to maleh. The algorithm used to generate this output checks a large dictionary for every chaser word and replaces it with its maleh counterpart(These dictionaries are found in the ChaserToMalehDicts folder). In the event that a word is not in the dictionary, the algorithm looks for all posibilities of adding and not adding the yudim and vavim and sees which is most likely by checking dictionaries in the Milon folder. This part of the algorithm works with the lowest level of accuracy so it is best to minimize dictionary misses.

There are utility webscraping programs that were used to get specific Nikud and Non Nikud data from the internet.