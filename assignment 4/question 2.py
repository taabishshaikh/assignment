# print $$$
#       ***
#       $$$
#       ***

for i in range (1,5):
    for j in range (1,4):
        if(i%2==0):
            print ('*', end = ' ')
        else:
            print ('$', end= ' ')
    print ()
