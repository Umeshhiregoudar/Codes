k=int(input("For how many values you are calculating\n"))
alpa=float(input("Enter the value of alpa\n"))
def calculate_binomial_coefficients():

   Coefficients=[{'Power':0, 'coefficient':1}]

   for i in range (1,k):

       numerator=1

       temp2=temp1.copy()

       for j in range (0,i):

           numerator=numerator*(alpa-j)

       temp2['coefficient']= numerator/math.factorial(i)

       temp2['Power']=i

       Coefficients.append(temp2)

   #print(Coefficients)

   return Coefficients
fx=calculate_binomial_coefficients()
print(fx)
[{'Power': 0, 'coefficient': 1}, {'Power': 1, 'coefficient': 2.0}, {'Power': 2, 'coefficient': 1.0}]
def integration_x(Coefficients):

    int_func_x = []

    for element in Coefficients:

        temp3=element.copy()

        temp3['Power']+=1

        temp3['coefficient'] *=1/temp3['Power']

        int_func_x.append(temp3)

    return int_func_x
intfx=integration_x(fx)
print(intfx)
[{'Power': 1, 'coefficient': 1.0}, {'Power': 2, 'coefficient': 1.0}, {'Power': 3, 'coefficient': 0.3333333333333333}]
value=0
for element in intfx:
    temp5=element.copy()
    value=value+((x)**temp5['Power'])*temp5['coefficient']

    
print(value)
8.666666666666666