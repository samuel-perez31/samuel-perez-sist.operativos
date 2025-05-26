t = 0

for i in range(7):
    e = int(input("Minutos de ejercicio > "))
    t += e

print("Promedio diario en la semana:", t/7)

if t/7 < 30:
    print("Se recomienda realizar más actividad")