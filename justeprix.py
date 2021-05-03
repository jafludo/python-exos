import random
randomnumber = str(random.randint(0, 10))
print(randomnumber)
inputnumber = input('Choice a number between 0 : 10')
while inputnumber != randomnumber:
    if inputnumber < randomnumber :
        print("plus")
        inputnumber = input('Choice a number between 0 : 10')

    elif inputnumber == randomnumber:
        print("GG")
        break

    else:
        print("moins")
        inputnumber = input('Choice a number between 0 : 10')
