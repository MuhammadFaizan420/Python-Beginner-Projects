def exponent(base,expo):
    num = expo
    result =1
    while num>0:
        result= result*base
        num = num -1
    print(base, "raises to the power of", expo, "is:", result)

exponent(2,5)
exponent(5,4)