class ieee754_gen:
    def __init__(self,decimalvalue):
        self.decimalvalue = decimalvalue
        
    def ieee8(self):
          def binaryOfFraction(fraction):
              binary = str()
              while (fraction):
                  fraction *= 2
                  if (fraction >= 1):
                      int_part = 1
                      fraction -= 1
                  else:
                      int_part = 0
                  binary += str(int_part)
                  if(len(binary)==5):
                          break       
              return binary
              
          def floatingPoint(real_no):
               sign_bit = 0
               if(real_no < 0):
                   sign_bit = 1
               real_no = abs(real_no)
               int_str = bin(int(real_no))[2 :6]
               #print(int_str)

               fraction_str = binaryOfFraction(real_no - int(real_no))

               if(int(real_no)==0):
                   ind = fraction_str.index('1')
                   exp_str = bin((3 - (ind + 1)) )[2 : ]
                   mant_str =fraction_str[ind + 1:]
               else:
                   ind = int_str.index('1')
                   exp_str = bin((len(int_str) - ind - 1) + 3)[2 : ]
                   mant_str = int_str[ind + 1 : ] + fraction_str
               #print(mant_str)    
               mant_str = (mant_str + ('0' * (4 - len(mant_str))))[ : 4]
               #print(mant_str)
               return sign_bit, exp_str, mant_str
      
      
          sign_bit, exp_str, mant_str = floatingPoint(self.decimalvalue)
          ieee_8 = str(sign_bit) + '|' + exp_str + '|' + mant_str
          print("IEEE 754 8 bit representation of 1259.125 is :")
          print(ieee_8) 
          
          
    def ieee16(self):
          def binaryOfFraction(fraction):
              binary = str()
              while (fraction):
                  fraction *= 2
                  if (fraction >= 1):
                      int_part = 1
                      fraction -= 1
                  else:
                      int_part = 0
                  binary += str(int_part)
                  if(len(binary)==11):
                          break
              return binary
    
          def floatingPoint(real_no):
               sign_bit = 0
               if(real_no < 0):
                   sign_bit = 1
               real_no = abs(real_no)
               int_str = bin(int(real_no))[2 : 12]

               fraction_str = binaryOfFraction(real_no - int(real_no))

               if(int(real_no)==0):
                   ind = fraction_str.index('1')
                   exp_str = bin((15 - (ind + 1)) )[2 : ]
                   mant_str =fraction_str[ind + 1:]
               else:
                   ind = int_str.index('1')
                   exp_str = bin((len(int_str) - ind - 1) + 15)[2 : ]
                   mant_str = int_str[ind + 1 : ] + fraction_str
               mant_str = (mant_str + ('0' * (10 - len(mant_str))))[ :10]
               return sign_bit, exp_str, mant_str


          sign_bit, exp_str, mant_str = floatingPoint(self.decimalvalue)
          ieee_16 = str(sign_bit) + '|' + exp_str + '|' + mant_str
          print("IEEE 754 16 bit representation of 1259.125 is :")
          print(ieee_16) 

           


    def ieee32(self):
          def binaryOfFraction(fraction):
              binary = str()
              while (fraction):
                  fraction *= 2
                  if (fraction >= 1):
                      int_part = 1
                      fraction -= 1
                  else:
                      int_part = 0
                  binary += str(int_part)
                  if(len(binary)==24):
                          break
              return binary

    

          def floatingPoint(real_no):
               sign_bit = 0
               if(real_no < 0):
                   sign_bit = 1
               real_no = abs(real_no)
               int_str = bin(int(real_no))[2 : ]

               fraction_str = binaryOfFraction(real_no - int(real_no))

               if(int(real_no)==0):
                   ind = fraction_str.index('1')
                   exp_str = bin((127 - (ind + 1)) )[2 : ]
                   mant_str =fraction_str[ind + 1:]
               else:
                   ind = int_str.index('1')
                   exp_str = bin((len(int_str) - ind - 1) + 127)[2 : ]
                   mant_str = int_str[ind + 1 : ] + fraction_str
               mant_str = mant_str + ('0' * (23 - len(mant_str)))
               return sign_bit, exp_str, mant_str

          sign_bit, exp_str, mant_str = floatingPoint(self.decimalvalue)
          ieee_32 = str(sign_bit) + '|' + exp_str + '|' + mant_str
          print("IEEE 754 32 representation of 1259.125 is :")
          print(ieee_32)
     

    def ieee64(self):
          def binaryOfFraction(fraction):
              binary = str()
              while (fraction):
                  fraction *= 2
                  if (fraction >= 1):
                      int_part = 1
                      fraction -= 1
                  else:
                      int_part = 0
                  binary += str(int_part)
                  if(len(binary)==53):
                          break
              return binary



          def floatingPoint(real_no):
                sign_bit = 0
                if(real_no < 0):
                    sign_bit = 1
                real_no = abs(real_no)
                int_str = bin(int(real_no))[2 : ]

                fraction_str = binaryOfFraction(real_no - int(real_no))

                if(int(real_no)==0):
                    ind = fraction_str.index('1')
                    exp_str = bin((1023 - (ind + 1)) )[2 : ]
                    mant_str =fraction_str[ind + 1:]
                else:
                    ind = int_str.index('1')
                    exp_str = bin((len(int_str) - ind - 1) + 1023)[2 : ]
                    mant_str = int_str[ind + 1 : ] + fraction_str
                mant_str = mant_str + ('0' * (52 - len(mant_str)))
                return sign_bit, exp_str, mant_str

          sign_bit, exp_str, mant_str = floatingPoint(self.decimalvalue)
          ieee_64 = str(sign_bit) + '|' + exp_str + '|' + mant_str
          print("IEEE 754 64 representation of 1259.125 is :")
          print(ieee_64)

x1=ieee754_gen(1259.125)
x1.ieee8()
x1.ieee16()
x1.ieee32()
x1.ieee64()



 
