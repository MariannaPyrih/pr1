import math
 
mas = [11, 0, 14, -9, -3, 4, 3, 1, -2, 0 ,13, 4, 15, 1]
min, max = 0, 0


for i in range(1, len(mas)) :
    if mas[i] > mas[max] : max = i

    if mas[i] < mas[min] : min = i
print("max="+str(max))
print("min="+str(min))
    
if min < max : 
    print('Sum = ',sum(mas[min  : max +1]))
else :
    print('Sum = ',sum(mas[max  : min +1]))
    
