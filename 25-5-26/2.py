tc = 0
cc = 0

while True:
    l = int(input("Ingresar litros cargados (0 para salir) > "))
    if l == 0:
        break
    elif l < 5:
        print("Sospecha de error o recarga mínima")
    tc += l
    cc += 1
    
print("Total cargado:", tc)
print("Promedio por carga:", tc/cc)