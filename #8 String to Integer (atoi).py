import re


def myAtoi(s):
    s_digit = s.strip()

        
    if s_digit == "-" or s_digit == "" or s_digit == "+":
        return 0

    s1 = re.match('[^\d]+',(s_digit.lstrip("-")).lstrip("+"))
    print(s1)

    if s1 != None:
        return 0

    else:
        s1 = re.search('\-*\+*\d+',s_digit).group()

    if s1[0:2] == "--" or s1[0:2] == "++" or s1[0:2] == "-+":
        return 0


    result = int(s1)

    if result > 2**31 -1 :
        return 2**31 -1

    if result < -2**31:
        return -2**31
        
    
    return result
        

print(myAtoi("t12+12"))
