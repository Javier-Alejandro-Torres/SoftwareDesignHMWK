import os

def main():
    a=True

    while a:
        try:

            print("*******************Directory********************\n")
            print("1. Add new record\n")
            print("2. Delete a record\n")
            print("3. Look for a record by mail and age\n")
            print("4. List on screen all record information\n")
            opc = int(input("You choose: "))

            if(opc==1):
                Add_New_Record()

            elif (opc == 2):
                Delete_New_Record()

            elif (opc == 3):
                Search_Record()

            elif (opc == 4):
                List_All_Info()

        except:
            print("Try again")


def Add_New_Record():
    f = open("Directory.txt", "a")

    Nombre = input("Nombre: ")
    f.write('Nombre: %s' %Nombre )

    Email = input("Email: ")
    f.write(', Email: %s'%Email )

    Age = input("Age: ")
    f.write(', Age: %s'%Age )

    Country = input("Country: ")
    f.write(', Country: %s'%Country +os.linesep)

    f.close()


def Delete_New_Record():
    new_file = open("Directory.txt")

    output = []
    Delete = input("Nombre: ")

    for line in new_file:
        if not Delete in line:
            output.append(line)

    new_file.close()
    new_file = open("Directory.txt", 'w')
    new_file.writelines(output)
    new_file.close()




def Search_Record():

    new_file = open("Directory.txt")
    lines = new_file.readlines()

    Mail = input("Email: ")
    Age1 = input("Age: ")

    for line in lines:
        if Mail in line:
            if Age1 in line:

                print(line)


def List_All_Info():
    f = open("Directory.txt", "r")
    print(f.read())


if __name__ == '__main__':
    main()