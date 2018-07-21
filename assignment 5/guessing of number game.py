from random import randint
print ('''INTRUCTION:
1) guess number between 1 to 6 only'
2) you have got three chance''')
ans=True

while ans==True:
    s=int(input('press 1 to begin: '))
    if (s==1):
        for i in range (1,4):
            print ('chance',i)    
            n1=int(input('Guess 1st number: '))
            n2=int(input('Guess 2nd number: '))
            
            if (0<n1<7 and 0<n2<7):
                ans=False
                if (n1==randint(1,6) or n2==randint(1,6)):
                    print ('you won 100 dollars')
                elif (n1==randint(1,6) and n2==randint(1,6)):
                    print ('you won 500 dollars')
                else:
                    print ('you lost')
            else:
                   print ('Enter appropriate guess')
                   ans=True
                   break
        print ('Game over')
    else:
        print('Retry')
