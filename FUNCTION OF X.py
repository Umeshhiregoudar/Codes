class function_of_x:

    def __init__(self, n, x,alpa,p,sign):

       self.value_n = n

       self.value_x = x

       self.value_alpa = alpa

       self.value_p = p

       self.value_sign = sign





    def facto(self,num):
       if num == 0:
           return 1
       return num * self.facto(num-1)



    def ex(self):

       value=1

       Coefficients=[{'power':0,'Coefficient':1}]

       temp1={'power':0,'Coefficient':0}

       for i in range(1,self.value_n+1):

           temp2=temp1.copy()

           temp2['Coefficient']=1/self.facto(i)

           temp2['power']=i

           Coefficients.append(temp2)

           x1=self.facto(i) 

           value=value + (self.value_x**i)/x1

       print("Exapnsion value of e^x is :",value)

       print("e^x expansion Coefficient:",Coefficients)



    def sin(self):

        temp1={'power':0,'Coefficient':0}

        value=0

        Coefficients=[]

        for i in range(0,self.value_n+1):

            temp2=temp1.copy()

            temp2['Coefficient']=(((-1)**i)/self.facto((2*i)+1))

            temp2['power']=((2*i)+1)

            Coefficients.append(temp2)

            value=value+(((-1)**i)/self.facto((2*i)+1))*(self.value_x**((2*i)+1))

        print("Expansion value of sinx is :",value)

        print("sinx exapansion Coefficients:",Coefficients)





    def binomial(self):

        def calculate_binomial_coefficients():

            Coefficients=[{'Power':0, 'coefficient':1}]

            for i in range (1,self.value_n):

               numerator=1

               temp1={'Power':0, 'coefficient':0}

               temp2=temp1.copy()

               for j in range (0,i):

                   numerator=numerator*(self.value_alpa-j)

               temp2['coefficient']= numerator/self.facto(i)

               temp2['Power']=self.value_p**i

               if(self.value_sign=="negative"):

                   if(i%2 != 0):

                       temp2['coefficient']=temp2['coefficient']*-1

               if(temp2['coefficient']==0):

                   break

               Coefficients.append(temp2)

           #print(Coefficients)

            return Coefficients





        def integration_x(Coefficients):

           int_func_x = []

           for element in Coefficients:

               temp3=element.copy()

               temp3['Power']+=1

               temp3['coefficient'] *=1/temp3['Power']

               int_func_x.append(temp3)

           return int_func_x



        fx=calculate_binomial_coefficients()

        print("fx Coefficients:",fx)



        intfx=integration_x(fx)

        print("Int fx Coefficients:",intfx)

        value=0

        for element in intfx:

            temp5=element.copy()

            value=value+((self.value_x)**temp5['Power'])*temp5['coefficient']

        print("Binomial Exapnsion value:",value*4)



    def logx(self):

        value=0

        for i in range(1,self.value_n+1):

             if (abs(-1+self.value_x)) < 1:

                 value=value + (((-1)**i)*((-1+self.value_x)**i)/i)

             else:

                 value=value + (((-1)**i)*((-1+self.value_x)**-i)/i)

        print("Expansion value of logx:",value)         



    

x=function_of_x(8,3,0.5,2,'negative')

x.ex()

x.sin()           

x.binomial()

x.logx()
