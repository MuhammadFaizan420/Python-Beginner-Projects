## Write a program that calculates the factorial of a given number  ##

n = 5
fact=1

for i in range(1,n+1):
    if i==0:
        continue
    fact = fact*i    
print(fact)
