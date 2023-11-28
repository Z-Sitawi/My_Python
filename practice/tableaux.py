import numpy as np

# Ex: 1

table = np.zeros(7, dtype="int")
print(table)

# Ex: 2

t1 = np.array([4, 8, 7, 9, 1, 5, 4, 6])
t2 = np.array([7, 6, 5, 2, 1, 3, 7, 4])

t3 = np.zeros(8, dtype="int")

for i in range(8):
    t3[i] = t1[i] + t2[i]

print(t3)


# Ex: 3


tab1 = np.array([4, 8, 7, 12])
tab2 = np.array([3, 6])

some = 0
for i in range(2):
    for j in range(4):
        some = some + (tab2[i] * tab1[j])

print("Le Schtroumpf sera : 3 * 4 + 3 * 8 + 3 * 7 + 3 * 12 + 6 * 4 + 6 * 8 + 6 * 7 + 6 * 12 =", some)


# Ex: 4

n = int(input("combien de chiffres vas-tu entrer dans le premier tableau? ==> : "))
T1 = np.zeros(n, dtype="int")
for i in range(n):
    num = int(input(f"Entre le nombre {i+1}: "))
    T1[i] = num

pair = 0
for j in range(0, n):
    if T1[j] % 2 == 0:
        pair = pair + 1
unpair = n - pair

a = b = 0
T2 = np.zeros(pair, dtype="int")
T3 = np.zeros(unpair, dtype="int")
for x in range(n):
    if T1[x] % 2 == 0:
        T2[a] = T1[x]
        a = a + 1
    else:
        T3[b] = T1[x]
        b = b + 1

print(f"\noriginal: {T1}", f"pair: {T2}", f"unpair: {T3}", sep="\n")

# Ex: 5

n = int(input("Entrer le nombre des val: "))
tab = np.zeros(n, dtype="int")

for i in range(n):
    tab[i] = int(input(f"Entrer nombre {i+1}: "))

v = tab[0] + 1
x = False
for i in range(1, n):
    if v == tab[i]:
        v = tab[i] + 1
        x = True
    else:
        x = False
        break

if x:
    print("Ses éléments sont tous consécutifs.")
else:
    print("Ses éléments sont pas consécutifs.")

# Ex: 5

n = int(input("combien de chiffres vas-tu entrer dans le premier tableau? ==> : "))
table = np.zeros(n, dtype="int")

for i in range(n):
    num = int(input(f"Entre le nombre {i+1}: "))
    table[i] = num

for i in range(1, n):
    key = table[i]
    j = i - 1

    while j >= 0 and key > table[j]:
        table[j + 1] = table[j]
        j = j - 1
    table[j + 1] = key

print(table)

for i in range(n):
    num = int(input(f"Entre le nombre {i+1}: "))
    table[i] = num

for i in range(1, n):
    key = table[i]
    j = i - 1

    while j >= 0 and key < table[j]:
        table[j + 1] = table[j]
        j = j - 1
    table[j + 1] = key

print(table)