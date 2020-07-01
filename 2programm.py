import math
x=0
i=0
while x<=0.5: 
 y= (2.5*(pow(x,3)))/(math.exp(2*x)+2)
 i=i+1
 print ('y[',i,']=  ' , y)
 x+=0.1
 print()
