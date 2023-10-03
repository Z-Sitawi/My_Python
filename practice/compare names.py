i = j = 0
names = []
ordered = True

while True:
    x = int(input("How many names you want to compare?\nType in Here: "))
    if x == 1 or x == 0:
        print("You have to enter 2 names or more!\nLet's try again.\n.\n..\n...")

    else:
        while i < x:
            name = str(input(f"Enter nom{i + 1}: "))
            name = name.upper()
            names.insert(i, name)
            i += 1

        print(names)
        while j < (x - 1):
            if names[j] > names[j + 1]:
                ordered = False  # If names are not ordered, set the flag to False
            j += 1

        if ordered:
            print("\n==> Names are ordered alphabetically.")
            break
        else:
            print("\n==>Names are not ordered alphabetically.")
            break