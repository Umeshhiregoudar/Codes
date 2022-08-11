Taylor Series expansion
e^x = 1 + x + x2/2! + x3/3! + ...

n=int(input("Enter the value of\n"))
Enter the value of
2
x=int(input("Enter the value of x\n"))
Enter the value of x
2
fact=1
for i in range(1,n+1):
    fact=fact + (x**i)/math.factorial(i)
print(fact)
5.0