name = input("Add an another name: ")

with open("user.txt","a") as f:
    f.write("\n"+name)
print("Add name to user.txt")