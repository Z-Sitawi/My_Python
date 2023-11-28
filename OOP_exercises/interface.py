note = [15, 18, 14, 17, 16, 12]
languages = ["Python", "Java", "C++", "Php"]
""" s = 0
for x in note:
    s = s + x
m = s / len(note)
print(f"la moyenne: {m:.2f}")
"""


def change(li, i1, i2):
    if li is list:
        l1 = li.copy()
        first = l1[i1]
        l1[i1] = l1[i2]
        l1[i2] = first
        return l1
    else:
        raise TypeError("argument must be a list")


note2 = [15, 17, 13, 7, 1, 5]


def pair(li):
    pairs = []
    for x in li:
        if x % 2 == 0:
            pairs.append(x)
    if len(pairs) == 0:
        return 0
    return pairs
