Taylore series Exapnsion of sin(x)


import math
n=int(input("For how many values you are calculating\n"))
value=0
for n in range(0,n+1):
    value=value + (((-1)**n)/math.factorial((2*n)+1))*(x**((2*n)+1))
print(value)