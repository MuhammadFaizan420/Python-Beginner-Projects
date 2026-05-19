primes = []

for num in range(2,21):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            primes.append(num)

print(primes[::2])