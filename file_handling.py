file = open("names.txt","a")

while True:
    name = input("Enter name to be added:")
    file.write(name+ "\n")
    choice = input("DO you wish to enter more names? (yes/no): ")
    if choice == "no":
        break

file = open("names.txt","r")
lines = file.readlines()

for line in lines:
    print(line.strip())
