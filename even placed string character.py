#### Display only those characters which are present at an even index number in given string.###

s = "pynative"

for i in range(len(s)):
    if i%2 == 0:
        print(s[i])


##for i, char in enumerate("pynative"):
    ##if i%2 == 0:
        ##print(char)