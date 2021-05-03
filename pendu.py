import random
import numpy as np
vies = 7
mottodisplay = []
etat = True
mot_IAchoice = ""
listmots = ['abeille','serpent','saucisson','table','chaise','clavier','bois']
def choicemot():
    global mottodisplay
    randomnumber = random.randint(0, len(listmots))
    motchoice = listmots[randomnumber]
    print("Mot choice by computer :"+motchoice)
    for index in range(len(motchoice)):
        mottodisplay.append("_")
    return motchoice
def askuserletter():
    global vies
    global mottodisplay
    global mot_IAchoice
    global etat 
    userchoix = input('Choice a letter : ')
    try:
        values = np.array(mot_IAchoice)
        il = np.where(values == userchoix)
        print(il)
        index_letter = mot_IAchoice.index(userchoix)
        if index_letter >= 0:
            print(userchoix)
            print(index_letter)
            del mottodisplay[index_letter]
            mottodisplay.insert(index_letter, userchoix)
    except ValueError:
        print("-1 vie")
        vies -= 1
        if(vies <= 0):
            etat = False
        print(vies)
    
def display():
    global etat
    print(mottodisplay)
    if(etat == False):
        print("Vous avez perdu !")
mot_IAchoice = choicemot()
while(etat):
    askuserletter()
    display()

