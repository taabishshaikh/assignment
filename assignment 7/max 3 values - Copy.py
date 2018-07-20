D={'a':10,'b':20,'c':42,'d':40,'e':15,'f':18,}
D1=list(D.values())
print(D1)
D1.sort()
max1=D1[len(D1)-1]
max2=D1[len(D1)-2]
max3=D1[len(D1)-3]
print (max1,max2,max3)
