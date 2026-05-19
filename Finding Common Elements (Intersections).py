list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

##solution 1
##common = set(list_a) & set(list_b)
##print(common)

##solution2
##common =[]
##for item in list_a:
##    if item in list_b:
##        common.append(item)
##print(common)

##solution 3

common = [item for item in list_a if item in list_b]
print(common)