D1={'a':10,'b':20,'c':30,'d':40}
D2={'c':12, 'e':15, 'f':18}
D={}

for each1 in D1.keys():
    for each2 in D2.keys():
        
        if each1==each2:
            s=D1.get(each1)+D2.get(each2)
            D.setdefault(each2,s)
            
            
        
        
        else:
            D.setdefault(each1,D1.get(each1))
           

print (D)

