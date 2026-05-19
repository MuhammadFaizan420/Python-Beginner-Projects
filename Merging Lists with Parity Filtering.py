## define a function which takes multiple arguments
def merge_list(list1,list2):
    ## final list which will be appended from list 1 and list 2
    final_list = []

# Get odd numbers from list1
    for i in list1:
      if i%2!=0:
        final_list.append(i)
        
# Get even numbers from list2
    for j in list2:
        if j%2==0:
           final_list.append(j)

    return final_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("Result:",merge_list(list1,list2))
