name = input("Enter the name: ")

with open("user.txt","w") as f:
    f.write(name)
print("Name writter to user.txt")