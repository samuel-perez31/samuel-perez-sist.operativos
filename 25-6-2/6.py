contraseña = "donpollokingohio77"
intentos = 0
while intentos != 3:
    intentoj = input("Ingresa la contraseña: ")
    if intentoj == contraseña:
        print("acceso permitido")
        break
    else:
        intentos += 1