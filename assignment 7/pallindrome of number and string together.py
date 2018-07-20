def pal_of_string (w):
    l=list(w)
    l.reverse()
    w="".join(l)
    return w

def pal_of_num(no):
    rev=0
    while no!=0:
        r=no%10
        rev=rev*10+r
        no=no//10
    return rev
x=int(input('''choose data type
for 'number' press '1' and for 'word' use 2:'''))

if x==1:
            num=int(input('enter a number:'))
            if num== pal_of_num (num):
                print('It is pallindrome')
            elif num!=pal_of_num(num):
                print('It is not pallindrome')
            else:
                print('Enter a number')
            
elif x==2:
            W=input('enter a word')
            t=W.upper()
            if t==pal_of_string(t):
                print('It is pallindrome')
            elif W!=pal_of_string(W):
                print('It is not pallindrome')
            else:
                print('Enter a word')
else:
            print('choose appropriate data type')
            
