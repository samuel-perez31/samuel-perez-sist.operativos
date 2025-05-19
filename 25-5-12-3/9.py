t=0
n0=0
p3=0
while t != -100:
    t = int(input("Ingrese la temperatura: "))
    if t < 0:
        n0 += 1
    elif t >= 30:
        p3 += 1
print("Temperaturas menores a 0:", n0)
print("Temperaturas mayores o iguales a 30:", p3)