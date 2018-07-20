#Library
import math

n=float(input('Enter a number: '))
sq=math.sqrt(n)
if ((sq%1)>=0.5):
    a=math.ceil(sq)
    print (a)
   
else:
    a=round (sq)
print (a)


