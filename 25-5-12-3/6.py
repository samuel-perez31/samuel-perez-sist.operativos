p = "admin"
a = False
for i in range(3):
    c = input("Ingrese la contraseña: ")
    if c == p:
        print("Contraseña correcta")
        a = True
        break
    else:
        print("Contraseña incorrecta")
if a == False:
    print("Acceso bloqueado")