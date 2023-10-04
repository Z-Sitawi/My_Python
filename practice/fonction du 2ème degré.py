import math

print("Ce programme calcule les solutions d'une fonction du 2ème degré.")
print("A la forme: ax² + bx + c = 0\n")

a = int(input("Entre la valure de a: "))
b = int(input("Entre la valure de b: "))
c = int(input("Entre la valure de c: "))

print(f"votre fonction est: {a}x² + {b}x + {c} = 0\n")

delta = (b ** 2) - (4 * a * c)

if delta == 0:
    x = -b / (2 * a)
    print(f"Δ = 0 la solution réelle de cette fonction est: x = {x:.2f}")

elif delta > 0:
    delta_root = math.sqrt(delta)

    x1 = (-b - delta_root) / (2 * a)

    x2 = (-b + delta_root) / (2 * a)

    print(f"Δ > 0 la solution réelle de cette fonction est:\nx1 = {x1:.2f}\nx2 = {x2:.2f}")

else:
    print("Δ < 0 n'a pas de solution réelle.")