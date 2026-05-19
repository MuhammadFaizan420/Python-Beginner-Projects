number = 7536

def int_reverse_order(number):
    while number>0:
        digit = number%10
        number = number//10
        print(digit,end=" ")

int_reverse_order(7536)


    