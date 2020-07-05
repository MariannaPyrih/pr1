import math
import itertools

def y(x, n):
        return ((2*n - 1)/math.factorial(n)*pow(2,n)*pow(x,n))
p=0.0001
a=-1
b=1
n=0
i=0
for x in itertools.count(start=a, step=0.2):
    if x>b:
        break
    tmp = y( x, n )
    res = tmp
    while ( abs( tmp ) >= p ):
        n+= 1
        i+=1
        tmp= y(x, n)
        res+= tmp
    print("x=",x)
    print( "Результат: ", res )
    #print( "Перевірка: ",  1/math.sqrt(1+x) )
print( "Iтерацій:", n)
