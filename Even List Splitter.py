numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]

even = []
odd = []

for number in numbers:
    if number%2==0:
       even.append(number)
    else:
        odd.append(number)
print("Even Numbers:",even)
print("Odd Numbers:",odd)

