import random
numerosecreto = random.randint(1, 10)
intentos = 0
intentojugador = 0
print("Tienes 3 intentos para adivinar el numero secreto")

while intentos < 3:
    intentojugador = int(input("Ingresa un numero del 1 al 10: "))
    if intentojugador == numerosecreto:
        print("Felicidades, adivinaste el numero")
        break
    else:
        intentos += 1
        print("Numero erroneo")