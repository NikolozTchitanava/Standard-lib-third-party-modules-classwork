import random
comppoints=0
userpoints=0
while 1==1:
    print('''score is:  
     your points:''',userpoints,'''
     programs points:''',comppoints)
    user=int(input('''eneter your choice:
                1-Rock
                2-Paper
                3-Scissor
            '''))
    
    comp=random.randint(1,3)
    def compchose(comp):
        if comp== 1:
            return("Rock")
        elif comp==2:
            return("Paper")
        else:
            return("Scissor")
    print("program chose-",compchose(comp))
    if comp == user :
        print("draw")
    elif comp==1:
        if user ==2:
            print("you win")
            userpoints+=1
        else:
            print("you lose")
            comppoints+=1

    elif comp==2:
        if user ==3:
            print("you win")
            userpoints+=1
        else:
            print("you lose")
            comppoints+=1
    elif comp==3:
        if user ==1:
            print("you win")
            userpoints+=1
        else:
            print("you lose")
            comppoints+=1


