word_to_be_counted ='Python'
with open("data.txt","r") as f:
    content = f.read()
    word=content.count(word_to_be_counted)
print(f'Occurrences of {word_to_be_counted}:{word}')