vasosdia = 0
dia = 0
while dia < 7:
    vasos = int(input("Cuantos vasos tomaste hoy?: "))
    vasosdia += vasos
    dia += 1
print("La cantidad de vasos por dia es: ", round(vasosdia/7,2))
if vasosdia/7 < 8:
    print("Deberias tomar mas agua")
