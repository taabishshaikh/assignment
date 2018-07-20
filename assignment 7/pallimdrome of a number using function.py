
def pall (no):
    rev=0
    while no!=0:
        r=no%10
        rev=rev*10+r
        no=no//10
    return rev
num=int(input('enter a number:'))
if num == pall(num):
    print ('number is pallindrome')
else:
    print('number is not pallindrome')
