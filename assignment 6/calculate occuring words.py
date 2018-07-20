w=input('enter a sentence: ')

x=w.lower()
w1=x.split(" ")
w2=input('enter word: '.lower())
y=w2.lower()
for each in w1:
    if each==y:
        print (each.upper())
        print(w1.count(each))
        break
    else:
        print('message is not present')
        break
#for loop not going uptil last index
