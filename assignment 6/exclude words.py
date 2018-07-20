#exclude words
ex=['is', 'am' , 'are' , 'of' , 'as' , 'on' , 'a']

st=input ('enter the sentence: ')
l=st.lower().split()
new_list=[]

for each in l:
    if  each not in ex:
        new_list.append(each)
        
print(" ".join(new_list))
