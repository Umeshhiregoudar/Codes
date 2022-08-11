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
 
sign_bit, exp_str, mant_str = floatingPoint(1259.125)
ieee_32 = str(sign_bit) + '|' + exp_str + '|' + mant_str
print("IEEE 754 representation of 1259.125 is :")
print(ieee_32)
