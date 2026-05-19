income = 45000
taxPayable =0
print("Given Income:" ,income)
if income<= 10000:
    taxPayable =0
elif income<=20000:
    taxPayable = ((income-10000)*0.10)
else:
    taxPayable = 0+(10000*.10)
    taxPayable+= (income-20000)*.20
print("Total Tax:",taxPayable)