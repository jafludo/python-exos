import random
listeppc = ['pierre','papier','ciseaux']
score = 0
def genppc():
    randomnumber = random.randint(0, 2)
    returnia = listeppc[randomnumber]
    print(returnia)
    return returnia
def verify(iachoix,userchoix):
    global score
    if userchoix == 'pierre':
        if iachoix == 'pierre':
            print('égalité')
        if iachoix == 'papier':
            score -= 5
        if iachoix == 'ciseaux':
            score += 5
    if userchoix == 'papier':
        if iachoix == 'pierre':
            score += 5
        if iachoix == 'papier':
            print('égalité')
        if iachoix == 'ciseaux':
            score -= 5
    if userchoix == 'ciseaux':
        if iachoix == 'pierre':
            score -= 5
        if iachoix == 'papier':
            score += 5
        if iachoix == 'ciseaux':
            print('égalité')
def resultat():
    global score
    print(score)

while(1):
    userchoix = input('pierre,papier,ciseaux ?')
    iachoice = genppc()
    verify(iachoice,userchoix)
    resultat()


