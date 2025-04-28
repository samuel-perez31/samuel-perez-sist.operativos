d = int(input("Ingresa un número > "))

if d >= 1 and d <= 5:
    print("Día laborable")
elif d == 6 or d == 7:
    print("Fin de semana")
else:
    print("Número inválido")