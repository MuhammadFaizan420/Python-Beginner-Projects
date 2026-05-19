### Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000,
#  return their product; otherwise, return their sum.####

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

a = n1+n2
b = n1*n2

if b >= 1000:
    print(a)
else: 
    print(b)


