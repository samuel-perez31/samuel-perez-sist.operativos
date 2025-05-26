car = 0

while True:
    car = int(input("Carga > "))
    con = int(input("Consumo > "))

    car -= con
    if car < 50*0.07:
        print("Carga insuficiente para 50km")
    
    det = input("Detener (Ingrese 0) > ")
    if det == 0:
        break