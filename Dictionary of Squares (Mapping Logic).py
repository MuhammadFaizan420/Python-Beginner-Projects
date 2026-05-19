##solution 1
##square ={}
##for i in range(1,11):
##    square[i]=i*i
##print(square)

##solution 2
squares={x: x**2 for x in range(1,11)}
print(squares)


## This is apart from solution as it shows list. Just a testing on Lambda and map.
##square = list(map(lambda x: x**2, range(1,11)))
##print(square)