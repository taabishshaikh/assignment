
#recursive function
''' a function which calls itself again and again
is called as recursive function'''
#WAP to find sum of 'n' natural numbers

'''def summa (no):
    if (no==1):
        return 1
    else:
        return (no+summa(no-1))
print (summa(99))'''
#wap to find factorial of given number using recursive function
def facto (no):
    if (no==1):
        return 1
    else:
        return (no*facto(no-1))
print (facto(994))
