# guess the number

import random
x = random.randrange(1, 11)
print("==> You have 5 chances to guess the right number", "==> The numbers are from 1 to 10", sep="\n")

i = 0
while i != 5:
    i = i + 1
    a = int(input("Enter the number here: "))
    if a < 1 or a > 10:
        print("This input is not allowed")
    if x == a:
        print("You Won")
        break
else:
    print("You Lost")