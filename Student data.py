list = []

def insert_data():
    while True:
        prn = input("Enter PRN (or type quit to exit):")
        if prn == 'quit':
            break
        name = input("Enter student name:")
        m1 = input("Enter marks of subject 1:")
        m2 = input("Enter marks of subject 2:")
        m3 = input("Enter marks of subject 3:")

        student = { "prn":prn,
                    "name":name,
                    "marks1":m1,
                    "marks2":m2,
                    "marks3":m3  }

        list.append(student)


def display():
    find_name = input("Enter name of student whose data you want:")
    for data in list:
        if data["name"].lower() == find_name.lower():
            print(f'PRN: {data["prn"]} | Name: {data["name"]} | Marks of Sub1: {data["marks1"]} | Marks of Sub2: {data["marks2"]} | Marks of Sub3: {data["marks3"]}')
            break

def delete_data():
    find_name = input("Enter name of student whose data you want:")
    for data in list:
        if data["name"].lower() == find_name.lower():
            list.remove(data)
            break

    print("Data deleted successfully")


while True:
    print("1.Insert data\n2.Display data\n3.Delete data\n4.Exit.")
    choice = int(input("Enter your choice(1/2/3/4):"))
    if choice == 1:
        insert_data()  #When you type quit in this function, ee already function ni baare lai jai che tane. Etle aya biju break add nthi kairu because that makes us leave this while loop as well.
        print(list)
    elif choice == 2:
        display()
        break
    elif choice == 3:
        delete_data()
        break
    elif choice == 4:
        break
    else:
        print("Enter valid choice")

