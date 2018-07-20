D={}
D.setdefault('maths',int(input('enter your maths marks')))
D.setdefault('chem',int(input('enter your chem marks')))
D.setdefault('phy',int(input('enter your phy marks')))
D.setdefault('mech',int(input('enter your mech marks')))
D.setdefault('java',int(input('enter your java marks')))
print (D)
maximum=0
minimum=100

for each in D.keys():
    if D.get(each) > maximum:
        maximum=D.get(each)
        
print ('maximum marks is:', maximum)

for each in D.keys():
    if D.get(each) < minimum:
        minimum=D.get(each)
print ('minimum marks is:', minimum)
