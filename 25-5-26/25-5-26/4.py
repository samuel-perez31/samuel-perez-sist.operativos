ca = 0
cd = 0

for i in range(10):
    n = int(input("Ingresar nota > "))
    if n < 6:
        cd +=1
    else:
        ca +=1

print("Aprobados:",ca,"/ Desaprobados:", cd)