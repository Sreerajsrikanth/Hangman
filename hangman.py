from random import choice, randint

def wordfun():

    wordlist=["Sree","Raj", "Dollu", "Avinash","Power","Piking","Lower"]
    return choice(wordlist)
word=wordfun()
guessed=""
turns=len(word)*1.5
while True:
    inp=input("\nMake a guess")
    turns=turns-1
    if inp in word:
        guessed=guessed + inp
    unguessed=0
    for i in word:
        if i in guessed:
            print(i,end="")
        else:
            unguessed+=1
            print("*",end="")
