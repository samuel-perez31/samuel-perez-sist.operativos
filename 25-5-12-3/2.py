niños = 0
adolescentes = 0
adultos = 0
edad = -1
while edad != 0:
    edad = int(input("Ingrese una edad (ingrese 0 para finalizar): "))
    if edad < 13:
        niños += 1
    elif edad >= 13 and edad <= 17:
        adolescentes += 1
    elif edad >= 18:
        adultos += 1
print("Hay", niños, "Niños, ",adolescentes,"adolescentes y ",adultos,"adultos")