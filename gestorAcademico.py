estudiantes={}

def registrar_estudiante():
    global estudiantes
    while True:
        id_est=input("Ingrese la id del estudiante: ")
        if len(id_est.strip())==0:
            print("El valor no puede quedar vacío")
        else:
            if id_est not in estudiantes:
                break
            else:
                print("Esta ID de estudiante ya existe")
                continue
    while True:
        nom_est=str(input("Ingrese el nombre del estudiante: "))
        if len(nom_est.strip())==0:
            print("El valor no puede quedar vacío")
        else:
            break
    while True:
        carrera_progra=input("Ingrese la carrera/programa académico: ")
        if len(carrera_progra.strip())==0:
            print("El valor no puede quedar vacío")
        else:
            break

    estudiantes[id_est]={
        "ID":id_est,
        "Nombre":nom_est,
        "Carrera":carrera_progra,
        "Curso":{}
    }

def todo_notas():
#Agregador de notas y verificador de aprobación
    global estudiantes
    notas={}
    id_buscar=input("Ingrese su ID de estudiante: ")

    if id_buscar in estudiantes:
        print(f"Bienvenido {estudiantes[id_buscar]['Nombre']}")
        val_aprobado="Perdido"
        while True:
            curso_nom=(input("Ingrese el curso a añadir: ")).lower()
            if len(curso_nom.strip())==0:
                print("El espacio no puede quedar vacío")
            else:
                if curso_nom not in estudiantes[id_buscar]['Curso']:
                    break
                else:
                    print("El curso ya esta registrado")
                    continue

        while True:
            try:
                nota_curso=int(input(f"Ingrese la nota de {curso_nom}: "))
                if nota_curso < 0 or nota_curso > 100:
                    print("La nota no estra dentro del rango de 0 a 100")
                else:
                    break
            except ValueError:
                print(f"El valor de la nota de {curso_nom} no es valido")

            except Exception as e:
                print(f"A ocurrido un error inesperado {e}")

        if nota_curso>=61:
            val_aprobado="Aprobado"

        notas[curso_nom]={
            "Nota":nota_curso,
            "Valor_aprobacion":val_aprobado,
        }
        estudiantes[id_buscar]["Curso"].update(notas)
    else:
        print("No se ha encontrado al estudiante")


def consultar_est(buscador):
#Tambien como calculador de promedio con ayuda del bucle de impresión de notas
    if buscador in estudiantes:
        print(f"\nNombre del estudiante: {estudiantes[buscador]['Nombre']}")
        print(f"Carrera: {estudiantes[buscador]['Carrera']}")

        if not estudiantes[buscador]["Curso"]:
            print("No se ha encontrado ningun curso")

        else:
            suma_notas = 0
            for curso_nom, valor in estudiantes[buscador]['Curso'].items():
                print(f"Curso: {curso_nom}, nota: {valor['Nota']}")
                suma_notas+=valor['Nota'] #Permite ir sumando a la variable de suma el valor de cada nota al pasar por el ciclo

            promedio=suma_notas/len(estudiantes[buscador]['Curso'])
            print(f"Su promedio es de: {round(promedio,2)}")
    else:
        print("No se ha encontrado al estudiante")

def verificador(buscador):
    if buscador in estudiantes:
        print(f"\nNotas del estudiante {estudiantes[buscador]['Nombre']}")
        for curso_nom, valor in estudiantes[buscador]['Curso'].items():
            print(f"Curso: {curso_nom} - {valor['Valor_aprobacion']}")
    else:
        print("No se ha encontrado al estudiante")


def mostrar_estudiantes():
    for id_estudiante, valor in estudiantes.items():
        print(f"ID del estudiante: {id_estudiante}")
        print(f"Nombre del estudiante: {valor['Nombre']}")
        print(f"Carrera: {valor['Carrera']}")

        for curso_nom, temp in valor['Curso'].items():
            print(f"Curso: {curso_nom} | Nota: {temp['Nota']}")


while True:

    print("\n---PORTAL ACADÉMICO---")
    print("\n1. Agregar estudiante")
    print("2. Agregar curso con nota")
    print("3. Consultar estudiante y su promedio")
    print("4. Verificación de aprobación")
    print("5. Mostrar todos los registros")
    print("6. Salir")

    opcion=input("Seleccione una opción: ")

    match opcion:
        case "1":
            print("\nEscogio 'Agregar estudiantes' ")
            registrar_estudiante()
            print("Estudiante agregado exitosamente")

        case "2":
            if len(estudiantes) > 0:
                print("\nEscogio 'Agregar cursos con nota' ")
                todo_notas()
                print("Curso agregado exitosamente")
            else:
                print("No se ha agregado ningun registro")

        case "3":
            if len(estudiantes) > 0:
                print("\nEscogio 'Consultar estudiantes' ")
                id_pa_buscar=input("Ingrese su ID de estudiante: ")
                consultar_est(id_pa_buscar)
            else:
                print("No se ha agregado ningun registro")

        case "4":
            if len(estudiantes) > 0:
                print("\nEscogio 'Verificación de aprobación' ")
                id_pa_buscar = input("Ingrese su ID de estudiante: ")
                verificador(id_pa_buscar)
            else:
                print("No se ha agregado ningun registro")

        case "5":
            if len(estudiantes) > 0:
                print("\nEscogio 'Mostrar registros' ")
                mostrar_estudiantes()
            else:
                print("No se ha agregado ningun registro")

        case "6":
            print("\nSaliendo del programa...")
            break

        case _:
            print("\nOpción no valida")



