import time

while True:
    print("\nDo you want to proceed in this process?")
    answer = input("Type in YES/NO: ")

    if answer == "YES" or answer == "yes":
        class St:

            def __init__(self, nom, lastname, age, email, note):
                self.name = nom
                self.lastname = lastname
                self.age = age
                self.email = email
                self.note = note

            def modify(self):
                element = input("Enter what the element to modify: name, lastname, age, email, or note: ")

                if element == "name":
                    mod = input("\nEnter your modification: ")
                    self.name = mod
                elif element == "lastname":
                    mod = input("\nEnter your modification: ")
                    self.lastname = mod
                elif element == "age":
                    mod = input("\nEnter your modification: ")
                    self.age = mod
                elif element == "email":
                    mod = input("\nEnter your modification: ")
                    self.email = mod
                elif element == "note":
                    mod = input("\nEnter your modification: ")
                    self.note = mod
                else:
                    print("Processing...")
                    time.sleep(2)
                    print("Sorry! Can't find the element you want to modify\nLet's try again")

            def display(self):
                print("\nName:", self.name, "\nLastname:", self.lastname, "\nAge:", self.age, "\nEmail:", self.email,
                      "\nNote:",
                      self.note, "\n")

            def listall(self):
                print("____ "+self.name, self.lastname, self.age, self.email, self.note, sep=" ____ | ____ ",
                      end=" ____\n")


        s1 = St("Badr", "Aaichaou", 20, "badr.aaichaou@gmail.com", 18)
        s2 = St("Taha", "Ben Hadi", 18, "bennhadi_taha@gmail.com", 19)
        s3 = St("Hoda", "El Fatih", 18, "1234el_fatihi@gmail.com", 15)

        print("\nEnter your command:\n")
        print("==> D: To Display the current student's info."+"\n==> M: To Modify the student's info.")
        print("==> L: To list all the student's info.\n")

        command = input("Type in D/M/L: ")

        if command == "l" or command == "L":
            print("______ Name ______", " ____ Lastname ____", " ____ Age ____ ",
                  " ________________ Email _______________",
                  " ____ Note ____ ", "\n")
            s1.listall()
            s2.listall()
            s3.listall()

        if command == "m" or command == "M" or command == "d" or command == "D":
            print("\nEnter the student ID (Ex: s1/s2/s3...)")
            s = input("Type in: ")

            if (s == "s1" or s == "S1") and (command == "D" or command == "d"):  # s1 display
                s1.display()
            elif (s == "s1" or s == "S1") and (command == "M" or command == "m"):  # s1 modify
                s1.modify()
                while True:
                    print("Do you want to modify another element:")
                    answer = input("Type in YES/NO: ")

                    if answer == "YES" or answer == "yes":
                        s1.modify()
                    elif answer == "NO" or answer == "no":
                        break
                    else:
                        print("Processing...")
                        time.sleep(2)
                        print("Sorry! Can't Understand.\nLet's try again")
                        break

                print("\nDo you want to display the modification?")
                answer = input("Type in YES/NO: ")
                if answer == "YES" or answer == "yes":
                    s1.display()
                elif answer == "NO" or answer == "no":
                    break
                else:
                    print("Processing...")
                    time.sleep(2)
                    print("Sorry! Can't Understand.\nLet's try again")

            elif (s == "s2" or s == "S2") and (command == "D" or command == "d"):  # s2 display
                s2.display()
            elif (s == "s2" or s == "S2") and (command == "M" or command == "m"):  # s2 modify
                s2.modify()
                while True:
                    print("Do you want to modify another element:")
                    answer = input("Type in YES/NO: ")

                    if answer == "YES" or answer == "yes":
                        s2.modify()
                    elif answer == "NO" or answer == "no":
                        break
                    else:
                        print("Processing...")
                        time.sleep(2)
                        print("Sorry! Can't Understand.\nLet's try again")
                        break

                print("\nDo you want to display the modification?")
                answer = input("Type in YES/NO: ")
                if answer == "YES" or answer == "yes":
                    s2.display()
                elif answer == "NO" or answer == "no":
                    break
                else:
                    print("Processing...")
                    time.sleep(2)
                    print("Sorry! Can't Understand.\nLet's try again")

            elif (s == "s3" or s == "S3") and (command == "D" or command == "d"):  # s3 display
                s3.display()
            elif (s == "s3" or s == "S3") and (command == "M" or command == "m"):  # s3 modify
                s3.modify()
                while True:
                    print("Do you want to modify another element:")
                    answer = input("Type in YES/NO: ")

                    if answer == "YES" or answer == "yes":
                        s3.modify()
                    elif answer == "NO" or answer == "no":
                        break
                    else:
                        print("Processing...")
                        time.sleep(2)
                        print("Sorry! Can't Understand.\nLet's try again")
                        break

                print("\nDo you want to display the modification?")
                answer = input("Type in YES/NO: ")
                if answer == "YES" or answer == "yes":
                    s3.display()
                elif answer == "NO" or answer == "no":
                    break
                else:
                    print("Processing...")
                    time.sleep(2)
                    print("Sorry! Can't Understand.\nLet's try again")

            else:
                print("Processing...")
                time.sleep(2)
                print("Sorry! Can't Understand.\nLet's try again")

    elif answer == "NO" or answer == "no":  # Exit the loop if "NO" is entered
        print("The Program is Terminating...")
        time.sleep(2)
        break

    else:  # if the user didn't enter neither yes nor no.
        print("Processing...")
        time.sleep(2)
        print("Sorry! Can't Understand.\nLet's try again")