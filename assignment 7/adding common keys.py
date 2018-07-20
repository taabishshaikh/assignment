D1={'a':10,'b':20,'c':30,'d':40}
D2={'c':12, 'e':15, 'f':18}
D={}

for each in D1.keys():
    if each in D2:
        D.setdefault(each,D1[each]+D2[each])
    else:
        D.setdefault(each,D1[each])

for each in D2.keys():
    if each not in D:
        D.setdefault(each,D2[each])

print (D)
