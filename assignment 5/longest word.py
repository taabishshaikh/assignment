l=[]
for n in range (5):
    l.append(input('enter a word'))
max_len=0
largest_word=''
for each in l:
    if(max_len<len(each)):
        max_len=len(each)
        largest_word=each
print ('the largest word is ',largest_word)
    
