text = "hello world from python"

texts = text.split()
capitalize_word = []

for word in texts:
     capitalize_word.append(word.capitalize())

result = " ".join(capitalize_word)
print(result)
