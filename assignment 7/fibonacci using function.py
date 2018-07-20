def fib(n):
    a,b=0,1
    print (a)
    print (b)
    for i in range (1, n-1):
        c=a+b
        print (c)
        a,b=b,c
no=int(input('enter a number'))
fib(no)
