###Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, 
# and their sum.####

number= 11

for i in range(number):
    if i==0:
      continue
    else:
      print("current number",i,"previous number",i-1,"SUM",i+(i-1))