w=input('enter the sentence: ')
word= input ('enter the word: ')
x=w.upper()
y=word.upper()
if y in x:
    print ('word',y,':',x.count(y))
else:
    print ('the word',y,'is not present')
    
