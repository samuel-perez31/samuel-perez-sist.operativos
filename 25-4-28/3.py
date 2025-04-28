print("MENÚ RESTAURANTE 😜")
print("""1. Hamburguesa
2. Pizza
3. Ensalada
4. Salir""")

c = int(input("> "))

if c == 1:
    print("Hamburguesa")
elif c == 2:
    print("Pizza")
elif c == 3:
    print("Ensalada")
else:
    print("Saliendo")
    exit()