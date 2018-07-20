holidays=(5,16,27)
d=int(input('enter a date'))

if 0<d<32:
    if d in holidays:
        print('it is a holiday')
    else:
        print('it is not a holiday')
else:
    print('enter appropriate date')
