estudiantes={}

def registrar_estudiante():
    global estudiantes

    id_est=input("Ingrese la id del estudiante: ")
    nom_est=str(input("Ingrese el nombre del estudiante: "))
    carrera_progra=input("Ingrese la carrera/programa académico: ")
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
    print(f"Bienvenido {estudiantes[id_buscar]['Nombre']}")

    if id_buscar in estudiantes:
        val_aprobado="Perdido"
        todas_notas=[]
        curso_nom=str(input("Ingrese del curso a añadir: "))
        nota_curso=int(input(f"Ingrese la nota de {curso_nom}: : "))
        todas_notas.append(nota_curso)

        if nota_curso>=61:
            val_aprobado="Aprobado"

        notas[curso_nom]={
            "Nota":nota_curso,
            "Valor_aprobacion":val_aprobado,
            #"Suma":sum(todas_notas)
        }

        estudiantes[id_buscar]["Curso"].update(notas)
    else:
        print("No se ha encontrado al estudiante")


def consultar_est(buscador):
#Tambien como calculador de promedio

    if buscador in estudiantes:
        print(f"\nNombre del estudiante: {estudiantes[buscador]['Nombre']}")
        print(f"Carrera: {estudiantes[buscador]['Carrera']}")

        if not estudiantes[buscador]["Curso"]:
            print("No se ha encontrado ningun curso")

        else:
            for curso_nom, valor in estudiantes[buscador]['Curso'].items():
                print(f"Curso: {curso_nom}, nota: {valor['Nota']}")
            promedio=len(estudiantes[buscador]['Curso'])


while True:

    print("\n---PORTAL ACADÉMICO---")
    print("\n1. Agregar estudiante")
    print("2. Agregar curso con nota")
    print("3. Consultar estudiante")
    print("4. Calcular promedio")
    print("5. Verificación de aprobación")
    print("6. Mostrar todos los registros")
    print("7. Salir")

    opcion=input("Seleccione una opción: ")

    match opcion:
        case "1":
            print("\nEscogio 'Agregar estudiantes' ")
            registrar_estudiante()
            print("Estudiante agregado exitosamente")

        case "2":
            print("\nEscogio 'Agregar cursos con nota' ")
            todo_notas()
            print("Curso agregado exitosamente")

        case "3":
            print("\nEscogio 'Consultar estudiantes' ")
            id_pa_buscar=input("Ingrese su ID de estudiante: ")
            consultar_est(id_pa_buscar)




