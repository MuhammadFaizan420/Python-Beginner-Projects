text = "apple banana apple cherry banana apple"

## splitting the text into list by split() function
texts = text.split()

## defining the empty set to get numbers against words.
frequency ={}

for word in texts:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
print(frequency)