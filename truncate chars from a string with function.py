##Write a function to remove characters from a string starting from index 0 up to n and return a new string.##
def remove_chars(w,n):
    print("original string:",w)

    res = w[n:]
    return res

print("Removing chars from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
