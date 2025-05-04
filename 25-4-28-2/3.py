def agregar_tarea():
    tarea = input("Ingresa la tarea: ")
    print()
    for i in estados:
        print(i, estados[i])
    estado = input("Ingresa el estado de la tarea: ")
    
    tar.append(tarea)
    est.append(estados[estado])

def actualizar_tarea():
    print("Tareas:")
    for i in range(len(tar)):
        print(f"{i+1}. {tar[i]} - {est[i]}")
    print()
    tarea_num = int(input("Ingresa el número de la tarea a actualizar: ")) - 1
    print()
    if 0 <= tarea_num < len(tar):
        print("Estados:")
        for i in estados:
            print(i, estados[i])
        estado = input("Ingresa el nuevo estado de la tarea: ")
        est[tarea_num] = estados[estado]
    else:
        print("Número de tarea inválido.")

def ver_tareas():
    print("Tareas:")
    for i in range(len(tar)):
        print(f"{i+1}. {tar[i]} - {est[i]}")
        
def eliminar_tarea():
    print("Tareas:")
    for i in range(len(tar)):
        print(f"{i+1}. {tar[i]} - {est[i]}")
    print()
    tarea_num = int(input("Ingresa el número de la tarea a eliminar: ")) - 1
    if 0 <= tarea_num < len(tar):
        tar.pop(tarea_num)
        est.pop(tarea_num)
    else:
        print("Número de tarea inválido.")



estados = {
    "1": "Pendiente",
    "2": "En progreso",
    "3": "Completada",
}

tar = []
est = []

print("Organizador de tareas")

while True:
    print()
    print("--------------------------")
    print("1. Agregar tarea")
    print("2. Actualizar tarea")
    print("3. Ver tareas")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("--------------------------")

    print()
    n = int(input(">  "))
    print()

    if n == 1:
        agregar_tarea()
        print()
        print("Tarea agregada")
    elif n == 2:
        actualizar_tarea()
        print()
        print("Tarea actualizada")
    elif n == 3:
        ver_tareas()
        print()
    elif n == 4:
        eliminar_tarea()
        print()
        print("Tarea eliminada")
    elif n == 5:
        exit()