notas = []
c = 0
while c < 5:
    nota = int(input("Ingrese la nota del alumno: "))
    if nota >= 1 and nota <= 10:
        c += 1
        notas.append(nota)
promedio = sum(notas)/5
if promedio > 7:
    print("El promedio es: ", promedio, "/ Aprobado")
else:
    print("El promedio no aprueba")