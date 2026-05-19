
##s1 = number1[::-1]
##s2 = number2[::-1]
##if s1 == number1:
    ##print(f'Number {number1} is palindrom')
##else:
 ##   print(f'Number {number1} is not palindrom')

##if s2 == number2:
##    print(f'Number {number2} is palindrom')
##else:
##    print(f'Number {number2} is not palindrom')

def palindrom_check(n):
    strnumber1 = str(n)
    strnumber= strnumber1[::-1]
    if strnumber== strnumber1:
        print(f'Number {n} is Palindrom')
    else:
        print(f'Number {n} is not Palidrome')
        

palindrom_check(121)
palindrom_check(125)