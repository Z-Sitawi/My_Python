i = j = 0
names = []
ordered = True

while True:
    try:
        x = int(input("How many names you want to compare?\nType in Here: "))
        if x < 2:
            print("You have to enter 2 names or more!\nLet's try again.\n.\n..\n...")

        elif x >= 2:
            while i < x:
                name = str(input(f"Enter nom{i + 1}: "))
                name = name.upper()
                names.append(name)
                i += 1

            while j < (x - 1):
                if names[j] > names[j + 1]:
                    ordered = False  # If names are not ordered, set the flag to False
                j += 1

            if ordered:
                print("\n==> Names are ordered alphabetically.")
                names.clear()
                print(names)
                break
            else:
                print("\n==>Names are not ordered alphabetically.")
                break

    except ValueError:
        print("Invalid input! Please enter a valid number for the number of names.")