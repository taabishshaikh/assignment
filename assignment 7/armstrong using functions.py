num=int(input('enter the number: '))


def armstrong(no):
    s=0
    while(no!=0):

        rem=no%10
        s=s+(rem**3)
        no=no//10
    return s
if (num==(armstrong(num))):
    print('It is armstrong number')
else:
    print ('It is not an armstrong number')

