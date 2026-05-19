##start_count = 6

##while start_count>0:
 ##   start_count = start_count-1
   ## if start_count ==0:
   ##     pass
    ##    print("Blast Off!")
    ##else:
    ##    print(start_count,end=" ")

import time

count = 5

while count > 0:
    print(count,end =" ")
    # Pause the program for 1 second
    time.sleep(1)
    # Decrement the counter
    count -= 1

print("Blast off!")
