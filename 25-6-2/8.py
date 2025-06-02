promedio = []
diamayor = 0
diamenor = 6000

for i in range(7):
    min = int(input("Ingresa los minutos del dia: "))
    promedio.append(min)
    if min > diamayor:
        diamayor += min
    elif min < diamenor:
        diamenor = min
sumpromedio = sum(promedio)  
promedio = sumpromedio/7
print(f'El promedio es {promedio}')
print("El dia con mas actividad fue con",diamayor,"minutos")
print("El dia con menos actividad fue con",diamenor,"minutos")