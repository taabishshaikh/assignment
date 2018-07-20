D={'a':10,'b':20,'c':42,'d':40,'e':15,'f':18,}
D1=list(D.values())
print(D1)
i=0
while i!=3:
    print(max(D1))
    D1.remove(max(D1))
    i=i+1

